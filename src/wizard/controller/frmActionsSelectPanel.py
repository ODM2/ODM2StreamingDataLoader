import wx

from odm2api.ODMconnection import dbconnection
#TODO get rid of *
from odm2api.ODM2.services.readService import *
from src.wizard.controller.frmNewSeriesDialog \
    import NewSeriesDialog
from src.wizard.controller.frmAddNewActionsPanel \
    import AddNewActionsPanelController
from src.wizard.controller.frmSeriesSelectPanel \
    import SeriesSelectPanel

from ObjectListView import ObjectListView, ColumnDefn

class ActionsSelectPanel(SeriesSelectPanel):
    def __init__( self, parent):
        super(ActionsSelectPanel, self).__init__(parent,
            "Action")
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Id', 'left', 70,
                'ActionID'),
            ColumnDefn('Type', 'left', 100,
                'ActionTypeCV'),
            ColumnDefn('Description', 'left', 500,
                'ActionDescription'),
            ColumnDefn('Method Id', 'left', 90,
                'MethodID'),
            ColumnDefn('Begin Time', 'left', 125,
                'BeginDateTime'),
            ColumnDefn('End Time', 'left', 125,
                'EndDateTime'),
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
            return read.getActions()
        return []

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self,
            u'Create New Action')
        newActionsPanel = AddNewActionsPanelController(dlg,
            self.parent.database)
        dlg.addPanel(newActionsPanel)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            pass;
            #self.list_ctrl.SetObjects(self.getSeriesData())

        #else:
        #    pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


