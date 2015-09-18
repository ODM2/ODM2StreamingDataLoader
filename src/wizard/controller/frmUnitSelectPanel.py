import wx

from api.ODMconnection import dbconnection
#TODO get rid of *
from api.ODM2.services.readService import *

from src.wizard.controller.frmAddNewUnitPanel import AddNewUnitPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel

from ObjectListView import ObjectListView, ColumnDefn

class UnitSelectPanel(SeriesSelectPanel):
    '''
    '''
    def __init__( self, parent, label):
        super(UnitSelectPanel, self).__init__(parent, label)
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Abbreviation', 'left', 120, 'UnitsAbbreviation'),
            ColumnDefn('Name', 'left', 120, 'UnitsName'),
            ColumnDefn('Type', 'left', 120, 'UnitsTypeCV'),
            ColumnDefn('Link', 'left', 120, 'UnitsLink'),
        ])
        self.list_ctrl.SetObjects(self.getSeriesData())

    def getSeriesData(self):
        # TODO use real time credentials.
        session_factory = dbconnection.createConnection('mysql', 'jws.uwrl.usu.edu', 'odm2', 'ODM', 'ODM123!!')
        session = session_factory.getSession()
        read = ReadODM2(session_factory)
        return read.getUnits()
    
    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, u'Create New ' + self.label)
        newUnitPanel = AddNewUnitPanelController(dlg)
        dlg.addPanel(newUnitPanel)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            print 'OK'
        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


