
import wx

from src.wizard.view.clsAddNewUnitPanel import AddNewUnitPanelView

class AddNewUnitPanelController(AddNewUnitPanelView):
    def __init__(self, daddy, db, **kwargs):
        super(AddNewUnitPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        self.db = db
        
        self.populateFields()
        
    def populateFields(self):
       read = self.db.getReadSession()

       units = [i.Name for i in read.getCVUnitsTypes()]
       self.m_comboBox13.AppendItems(units)
