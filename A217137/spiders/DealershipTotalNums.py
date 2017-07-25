from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Dealershiptotalnums(BasePortiaSpider):
    name = "DealershipTotalNums"
    allowed_domains = [
        u'www.bmwrockville.com',
        u'www.bmwofcatonsville.com',
        u'www.bmwofsilverspring.com',
        u'www.northwestbmw.com',
        u'www.passportbmw.com',
        u'www.bmwoftowson.com',
        u'www.bmwofbelair.com',
        u'www.bmwofannapolis.com']
    start_urls = [
        u'https://www.bmwrockville.com/new-inventory/index.htm?search=&model=i3&normalExteriorColor=&normalInteriorColor=&internetPrice=&accountId=bmwofrockvillemd&saveFacetState=true&lastFacetInteracted=inventory-listing1-facet-anchor-accountId-1',
        u'https://www.bmwoftowson.com/new-inventory/index.htm?search=&model=i3&accountId=bmwstore&saveFacetState=true&lastFacetInteracted=inventory-listing1-facet-anchor-accountId-2',
        u'https://www.bmwofbelair.com/new-inventory/index.htm?search=&model=i3&normalExteriorColor=&accountId=bmwofbelair&saveFacetState=true&lastFacetInteracted=inventory-listing1-facet-anchor-accountId-0',
        u'https://www.northwestbmw.com/new-inventory/index.htm?search=&superModel=BMW+i&bodyStyle=Sedan&engine=&trim=&normalTransmission=&saveFacetState=true&lastFacetInteracted=inventory-listing1-facet-anchor-bodyStyle-1',
        u'http://www.bmwofcatonsville.com/new-inventory/index.htm?search=&saveFacetState=true&model=i3&lastFacetInteracted=inventory-listing1-facet-anchor-model-15',
        u'http://www.bmwofsilverspring.com/new-inventory/index.htm?search=&saveFacetState=true&model=i3&payment-selection=payment-panel-paymentLoan&lastFacetInteracted=inventory-listing1-facet-anchor-model-11',
        u'http://www.bmwofannapolis.com/new-inventory/index.htm?search=&saveFacetState=true&model=i3&lastFacetInteracted=inventory-listing1-facet-anchor-model-16',
        u'http://www.passportbmw.com/searchnew.aspx?Model=i3']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=('.*')
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PortiaItem,
                   None,
                   u'body',
                   [Field(u'Location',
                          '.ddc-header > .ddc-content > .vcard > .fn > .org *::text',
                          []),
                       Field(u'#_of_cars',
                             '.ddc-wrapper > .ddc-container > .page-bd > .inventory-listing-default > .yui3-g > .yui3-u-3-4 > .ddc-content > .yui3-g > .yui3-u-1 > .ddc-content > .selections > .facet-breadcrumb-title > .vehicle-count *::text',
                             [])]),
              Item(PortiaItem,
                   None,
                   u'body',
                   [Field(u'Location',
                          '.ddc-header > .ddc-content > .vcard > .fn > .org *::text',
                          []),
                    Field(u'#_of_cars',
                          '.ddc-wrapper > .ddc-container > .page-bd > .inventory-listing-default > .yui3-g > .yui3-u-3-4 > .ddc-content > .yui3-g > .yui3-u-1 > .ddc-content > .selections > .facet-breadcrumb-title > .vehicle-count *::text',
                          [])]),
              Item(PortiaItem,
                   None,
                   u'.brand > .col-xs-12',
                   [Field(u'Location',
                          '.dealerName *::text',
                          [])])]]
