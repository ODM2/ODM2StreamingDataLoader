import wx

from src.wizard.view.clsAddNewUnitPanel import AddNewUnitPanelView
from odm2api.ODM2.models import Units



class AddNewUnitPanelController(AddNewUnitPanelView):
    def __init__(self, daddy, db, type = None):
        super(AddNewUnitPanelController, self).__init__(daddy)
        self.parent = daddy
        self.db = db

        self.units = None
        
        self.populateFields(type)
        
    def populateFields(self, type = None):
       read = self.db.getReadSession()

       # units = [i.Name for i in read.getCVUnitsTypes()]
       units = [i.Name for i in read.getCVs(type="Units Type")]
       if type:
           if type in units:
               units = [type]
       self.m_comboBox13.AppendItems(units)

    def onOK(self, event):
        if not self.Validate():
            self.Refresh()
            return
        else:
            self.getFieldValues()
            try:
                write = self.db.getWriteSession()
                unit = Units(UnitsTypeCV=self.unitsType,
                    UnitsAbbreviation=self.unitsAbr,
                    UnitsName=self.unitsName,
                    UnitsLink=self.unitsLink)
                self.unit=write.createUnit(unit)

                if type(self.parent.parent).__name__ =="UnitSelectPanel":
                    #this part is for selecting the new value in a list. should only be run when generated fromx
                    self.parent.parent.list_ctrl.SetObjects(self.parent.parent.getSeriesData())
                    length = self.parent.parent.list_ctrl.GetItemCount.im_self.ItemCount - 1
                    self.parent.parent.list_ctrl.Focus(length)
                    self.parent.parent.list_ctrl.Select(length, 1)

            except Exception as e:
                print e

        event.Skip()

    def getFieldValues(self):
        self.unitsName = str(self.m_textCtrl26.GetValue())
        self.unitsType = str(self.m_comboBox13.GetStringSelection())
        self.unitsAbr = str(self.m_textCtrl261.GetValue())

        if str(self.m_textCtrl29.GetValue()) == '':
            self.unitsLink = None
        else:
            self.unitsLink = str(self.m_textCtrl29.GetValue())

