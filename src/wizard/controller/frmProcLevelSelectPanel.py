import wx

from api.ODMconnection import dbconnection
#TODO get rid of *
from api.ODM2.services.readService import *
from src.controllers.Database import Database
from src.wizard.controller.frmAddNewProcLevelPanel \
    import AddNewProcLevelPanelController
from src.wizard.controller.frmSeriesSelectPanel \
    import SeriesSelectPanel
from src.wizard.controller.frmNewSeriesDialog \
    import NewSeriesDialog
from ObjectListView import ObjectListView, ColumnDefn

class ProcLevelSelectPanel(SeriesSelectPanel):
    def __init__( self, parent):
        super(ProcLevelSelectPanel, self).__init__(parent,
            "Processing Level")
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Code', 'left', 120,
                'ProcessingLevelCode'),
            ColumnDefn('Definition', 'left', 120,
                'Definition'),
            ColumnDefn('Explaination', 'left', 120,
                'Explaination'),
        ])
        self.list_ctrl.SetObjects(self.getSeriesData())
        if not self.parent.database:
            self.new_button.Enable(False)

    def getSeriesData(self):
        if self.parent.database:
            read = self.parent.database.getReadSession()
            return read.getProcessingLevels()
        return []

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self,
            u'Create New Processing Level')
        newProcLevelPanel = AddNewProcLevelPanelController(dlg,
            self.parent.database)
        dlg.addPanel(newProcLevelPanel)
        dlg.CenterOnScreen()

        if dlg.ShowModal() == wx.ID_OK:
            self.list_ctrl.SetObjects(self.getSeriesData())
        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


