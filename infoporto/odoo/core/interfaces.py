from zope import schema
from zope.interface import Interface

from infoporto.odoo.core import _


class IOdoo(Interface):
    pass

class IOdooSettings(Interface):

    odoo_hostname  = schema.URI(title=_(u"Hostname"),
                    description=_(u"http://localhost:8069"),
                    required=False
                    )

    odoo_username = schema.TextLine(title=_(u"Username"),
                    required=False)

    odoo_password = schema.Password(title=_(u"Password"),
                    required=False)

    odoo_database = schema.TextLine(title=_(u"Database"),
                    required=False)
