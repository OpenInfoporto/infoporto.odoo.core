import zope.interface
from infoporto.odoo.core.interfaces import IOdoo


class Basic(object):
    zope.interface.implements(IOdoo)
