import wx

from api.ODMconnection import dbconnection
#TODO get rid of *
from api.ODM2.services.readService import *
from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog
from src.wizard.controller.frmAddNewActionsPanel import AddNewActionsPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel

from ObjectListView import ObjectListView, ColumnDefn

class ActionsSelectPanel(SeriesSelectPanel):
    '''
    '''
    def __init__( self, parent):
        super(ActionsSelectPanel, self).__init__(parent)
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Code', 'left', 120, 'SamplingFeatureCode'),
            ColumnDefn('Name', 'left', 120, 'SamplingFeatureName'),
            ColumnDefn('Type', 'left', 120, 'SamplingFeatureTypeCV'),
            ColumnDefn('Description', 'left', 120, 'SamplingFeatureDescription'),
            ColumnDefn('Geotype', 'left', 120, 'SamplingFeatureGeotypeCV'),
            ColumnDefn('Elevation', 'left', 120, 'Elevation_m'),
        ])
        self.list_ctrl.SetObjects(self.getSeriesData())

    def getSeriesData(self):
        #read = self.db.getReadSession()
        #return read.getSamplingFeatures()
        pass

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, u'Create New Action')
        newActionsPanel = AddNewActionsPanelController(dlg)
        dlg.addPanel(newActionsPanel)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            print 'OK'
        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


