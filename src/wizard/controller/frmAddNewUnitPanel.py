import wx

from src.wizard.view.clsAddNewUnitPanel import AddNewUnitPanelView
from odm2api.ODM2.models import Units


class AddNewUnitPanelController(AddNewUnitPanelView):
    def __init__(self, daddy, db):
        super(AddNewUnitPanelController, self).__init__(daddy)
        self.parent = daddy
        self.db = db

        self.units = None
        
        self.populateFields()
        
    def populateFields(self):
       read = self.db.getReadSession()

       # units = [i.Name for i in read.getCVUnitsTypes()]
       units = [i.Name for i in read.getCVs(type="Units Type")]
       self.m_comboBox13.AppendItems(units)

    def onOK(self, event):
        if not self.Validate():
            self.Refresh()
            return
        self.getFieldValues()
        try:
            write = self.db.getWriteSession()
            unit = Units(
                UnitsTypeCV=self.unitsType,
                UnitsAbbreviation=self.unitsAbr,
                UnitsName=self.unitsName,
                UnitsLink=self.unitsLink
            )

            write.createUnit(unit)

            self.units = unit

        except Exception as error:
            print error

        event.Skip()

    def getFieldValues(self):
        self.unitsName = str(self.m_textCtrl26.GetValue())
        self.unitsType = str(self.m_comboBox13.GetStringSelection())
        self.unitsAbr = str(self.m_textCtrl261.GetValue())

        if str(self.m_textCtrl29.GetValue()) == '':
            self.unitsLink = None
        else:
            self.unitsLink = str(self.m_textCtrl29.GetValue())

