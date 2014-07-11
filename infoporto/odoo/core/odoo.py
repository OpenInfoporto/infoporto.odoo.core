from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
import xmlrpclib

from infoporto.odoo.core.interfaces import IOdooSettings


class TestView(BrowserView):
    template = ViewPageTemplateFile('browser/view.pt')

    def __call__(self):
        config = getUtility(IRegistry).forInterface(IOdooSettings)
        oo = OdooInstance(config)
        return self.template()


class OdooInstance():

    def __init__(self, config=False):
        if not config:
            config = getUtility(IRegistry).forInterface(IOdooSettings)

        self.host = config.odoo_hostname or 'http://localhost:8069'
        self.user = config.odoo_username or 'admin'
        self.pwd = config.odoo_password or 'admin'
        self.db = config.odoo_database or 'odootest'

        self.connect()

    def connect(self):
        sock = xmlrpclib.ServerProxy('%s/xmlrpc/common' % self.host)
        self.uid = sock.login(self.db, self.user, self.pwd)
        self.sock = xmlrpclib.ServerProxy('%s/xmlrpc/object' % self.host)

        return True

    def search(self, model, filters):
        ids = self.sock.execute(self.db, self.uid, self.pwd, model, 'search', filters)
        return ids

    def read(self, model, ids, fields):
        results = self.sock.execute(self.db, self.uid, self.pwd, model, 'read', ids, fields)
        return results

    def create(self, model, data):
        result = self.sock.execute(self.db, self.uid, self.pwd, model, 'create', data)
        return result
