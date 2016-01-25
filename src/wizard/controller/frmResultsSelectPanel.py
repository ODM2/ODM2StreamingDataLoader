import wx

from odm2api.ODMconnection import dbconnection
#TODO get rid of *
from odm2api.ODM2.services.readService import *
from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog
from src.wizard.controller.frmAddNewResultsPanel import AddNewResultsPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel

from src.wizard.view.clsResultPage import ResultPageView

from ObjectListView import ObjectListView, ColumnDefn

class ResultsSelectPanel(SeriesSelectPanel):
    '''
    '''
    def __init__( self, parent, label):
        super(ResultsSelectPanel, self).__init__(parent, label)
        self.list_ctrl.Show(False)
        self.new_button.Show(False) 
        sizer = self.GetSizer()
        sizer.Add(ResultPageView, 0, wx.ALL, 5)

    def getSeriesData(self):
        read = self.db.getReadSession()
        return read.getResults()
    
    def onButtonAdd(self, event):
        event.Skip()
    
    def __del__( self ):
        pass


