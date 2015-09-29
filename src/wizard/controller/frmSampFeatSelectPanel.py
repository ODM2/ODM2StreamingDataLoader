import wx

from api.ODMconnection import dbconnection
#TODO get rid of *
from api.ODM2.services.readService import *

from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog

from src.wizard.controller.frmAddNewSampFeatPanel import AddNewSampFeatPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel

from ObjectListView import ObjectListView, ColumnDefn

class SampFeatSelectPanel(SeriesSelectPanel):
    '''
    '''
    def __init__( self, parent, label):
        super(SampFeatSelectPanel, self).__init__(parent, label)
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
        read = self.db.getReadSession()
        return read.getSamplingFeatures()
    
    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, u'Create New ' + self.label)
        newSampFeatPanel = AddNewSampFeatPanelController(dlg)
        dlg.addPanel(newSampFeatPanel)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            print 'OK'
            # TODO
            # Add a Sampling Feature to the Database.
            
            # Refresh List.
            self.list_ctrl.SetObjects(self.getSeriesData())

        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


