# coding: utf-8
from pool import Pool, PoolElement, Template, extractString


class Zone(PoolElement):
    METHODS = {
    }

    XML_TYPES = {
        'id': int,
        'name': extractString,
        'template': ['TEMPLATE', Template],
    }

    ELEMENT_NAME = 'ZONE'

    def __init__(self, xml, client):
        super(Zone, self).__init__(xml, client)
        self._convert_types()

    def __repr__(self):
        return '<oca.Zone("%s")>' % self.name


class ZonePool(Pool):
    METHODS = {
        'info': 'zonepool.info',
    }

    def __init__(self, client):
        super(ZonePool, self).__init__('ZONE_POOL', 'ZONE', client)

    def _factory(self, xml):
        c = Zone(xml, self.client)
        return c
