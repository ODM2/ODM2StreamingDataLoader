import wx

#from api.ODMconnection import dbconnection
#TODO get rid of *
#from api.ODM2.services.readService import *

from src.wizard.controller.frmAddNewUnitPanel \
    import AddNewUnitPanelController
from src.wizard.controller.frmSeriesSelectPanel \
    import SeriesSelectPanel
from ObjectListView import ObjectListView, ColumnDefn
from src.wizard.controller.frmNewSeriesDialog \
    import NewSeriesDialog

class UnitSelectPanel(SeriesSelectPanel):
    def __init__( self, parent):
        super(UnitSelectPanel, self).__init__(parent,
            "Unit")
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Abbreviation', 'left', 120,
                'UnitsAbbreviation'),
            ColumnDefn('Name', 'left', 120,
                'UnitsName'),
            ColumnDefn('Type', 'left', 120,
                'UnitsTypeCV'),
            ColumnDefn('Link', 'left', 120,
                'UnitsLink'),
        ])
        self.list_ctrl.SetObjects(self.getSeriesData())
        if not self.parent.database:
            self.new_button.Enable(False)
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.enable)
        #self.list_ctrl.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.disable)
        self.Bind(wx.EVT_SHOW, self.onShow)

    def onShow(self, event):
        if self.list_ctrl.GetSelectedObject():
            self.parent.btnNext.Enable(True)  
        else:
            self.parent.btnNext.Enable(False)  
        event.Skip()
  
    def enable(self, event):
        self.parent.btnNext.Enable(True)
        event.Skip()
    
    def disable(self, event):
        self.parent.btnNext.Enable(False)
        event.Skip()

    def getSeriesData(self):
        if self.parent.database:
            read = self.parent.database.getReadSession()
            return read.getUnits()
        return []

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self,
            u'Create New Unit')
        newUnitPanel = AddNewUnitPanelController(dlg,
            self.parent.database)
        dlg.addPanel(newUnitPanel)
        dlg.CenterOnScreen()

        if dlg.ShowModal() == wx.ID_OK:
            #self.list_ctrl.SetObjects(self.getSeriesData())
            pass;
        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


