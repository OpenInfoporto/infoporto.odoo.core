from plone.app.registry.browser import controlpanel

from infoporto.odoo.core.interfaces import IOdooSettings
from infoporto.odoo.core import _


class OdooSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IOdooSettings
    label = _(u"Odoo settings")

    def __init__(self, a, b):
        super(OdooSettingsEditForm, self).__init__(a, b)

    def updateFields(self):
        super(OdooSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(OdooSettingsEditForm, self).updateWidgets()

    def applyChanges(self, data):
        return super(OdooSettingsEditForm, self).applyChanges(data)


class OdooSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = OdooSettingsEditForm

