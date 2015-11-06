import wx

from api.ODMconnection import dbconnection
#TODO get rid of *
from api.ODM2.services.readService import *
#from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog
#from src.wizard.controller.frmAddNewResultsPanel import AddNewResultsPanelController
#from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel

from src.wizard.view.clsResultPage import ResultPageView

from ObjectListView import ObjectListView, ColumnDefn

class ResultSummaryPanel(ResultPageView):
    def __init__( self, parent):
        super(ResultSummaryPanel, self).__init__(parent)

    def getSeriesData(self):
        read = self.parent.database.getReadSession()
        return read.getResults()
    
    def onButtonAdd(self, event):
        event.Skip()
    


