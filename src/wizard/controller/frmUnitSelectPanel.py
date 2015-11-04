import wx

#from api.ODMconnection import dbconnection
#TODO get rid of *
#from api.ODM2.services.readService import *

from src.wizard.controller.frmAddNewUnitPanel import AddNewUnitPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel

from ObjectListView import ObjectListView, ColumnDefn
from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog

class UnitSelectPanel(SeriesSelectPanel):
    '''
    '''
    def __init__( self, parent):
        super(UnitSelectPanel, self).__init__(parent)
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Abbreviation', 'left', 120, 'UnitsAbbreviation'),
            ColumnDefn('Name', 'left', 120, 'UnitsName'),
            ColumnDefn('Type', 'left', 120, 'UnitsTypeCV'),
            ColumnDefn('Link', 'left', 120, 'UnitsLink'),
        ])
        self.list_ctrl.SetObjects(self.getSeriesData())

    def getSeriesData(self):
        #read = self.db.getReadSession()
        #return read.getUnits()
        pass
    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, u'Create New Unit')
        newUnitPanel = AddNewUnitPanelController(dlg, self.db)
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


