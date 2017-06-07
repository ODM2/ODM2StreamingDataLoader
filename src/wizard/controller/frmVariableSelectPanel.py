import wx

from odm2api.ODMconnection import dbconnection
#TODO get rid of *
from odm2api.ODM2.services.readService import *

from src.wizard.controller.frmNewSeriesDialog \
    import NewSeriesDialog
from src.wizard.controller.frmAddNewVariablePanel \
    import AddNewVariablePanelController
from src.wizard.controller.frmSeriesSelectPanel \
    import SeriesSelectPanel
from ObjectListView import ObjectListView, ColumnDefn

class VariableSelectPanel(SeriesSelectPanel):
    def __init__( self, parent):
        super(VariableSelectPanel, self).__init__(parent,
            "Variable")
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Code', 'left', 120,
                       'VariableCode'),
            ColumnDefn('Name', 'left', 120,
                       'VariableNameCV'),
            ColumnDefn('Type', 'left', 120,
                       'VariableTypeCV'),
            ColumnDefn('Definition', 'left', 120,
                       'VariableDefinition'),
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
            return read.getVariables()
        return []

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self,
            u'Create New Variable')
        newVariablePanel = AddNewVariablePanelController(dlg,
            self.parent.database)
        dlg.addPanel(newVariablePanel)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            pass
            #self.list_ctrl.SetObjects(self.getSeriesData())
        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


