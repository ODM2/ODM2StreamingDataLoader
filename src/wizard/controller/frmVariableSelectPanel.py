import wx

from api.ODMconnection import dbconnection
#TODO get rid of *
from api.ODM2.services.readService import *

from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog
from src.wizard.controller.frmAddNewVariablePanel import AddNewVariablePanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel

from ObjectListView import ObjectListView, ColumnDefn

class VariableSelectPanel(SeriesSelectPanel):
    '''
    '''
    def __init__( self, parent):
        super(VariableSelectPanel, self).__init__(parent)
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Code', 'left', 120, 'VariableCode'),
            ColumnDefn('Name', 'left', 120, 'VariableName'),
            ColumnDefn('Type', 'left', 120, 'VariableTypeCV'),
            ColumnDefn('Description', 'left', 120, 'VariableDescription'),
        ])
        self.list_ctrl.SetObjects(self.getSeriesData())

    def getSeriesData(self):
        #read = self.db.getReadSession()
        #return read.getVariables()
        pass
    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, u'Create New ...')
        newVariablePanel = AddNewVariablePanelController(dlg, self.db)
        dlg.addPanel(newVariablePanel)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            print 'OK'
        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


