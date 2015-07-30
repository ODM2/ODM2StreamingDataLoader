
import wx

from view.clsDataConfigPanel import DataConfigPanelView

class DataConfigPanelController(DataConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(DataConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        
    def getInput(self):
        return {}

    def populate(self, data={}):
        # Read the file.
        # Delete data if file path was changed.
        # Get column headers and InsertColumn for each of them.
        # Read data into appropriate columns.
        # 
        self.m_listCtrl1.InsertColumn(0, data['data'])

