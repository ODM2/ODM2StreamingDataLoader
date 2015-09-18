import wx

from api.ODMconnection import dbconnection
#TODO get rid of *
from api.ODM2.services.readService import *

from src.wizard.controller.frmAddNewProcLevelPanel import AddNewProcLevelPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel

from ObjectListView import ObjectListView, ColumnDefn

class ProcLevelSelectPanel(SeriesSelectPanel):
    '''
    '''
    def __init__( self, parent, label):
        super(ProcLevelSelectPanel, self).__init__(parent, label)
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Code', 'left', 120, 'ProcessingLevelCode'),
            ColumnDefn('Definition', 'left', 120, 'Definition'),
            ColumnDefn('Explaination', 'left', 120, 'Explaination'),
        ])
        self.list_ctrl.SetObjects(self.getSeriesData())

    def getSeriesData(self):
        # TODO use real time credentials.
        session_factory = dbconnection.createConnection('mysql', 'jws.uwrl.usu.edu', 'odm2', 'ODM', 'ODM123!!')
        session = session_factory.getSession()
        read = ReadODM2(session_factory)
        return read.getProcessingLevels()
    
    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, u'Create New ' + self.label)
        newProcLevelPanel = AddNewProcLevelPanelController(dlg)
        dlg.addPanel(newProcLevelPanel)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            print 'OK'
        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


