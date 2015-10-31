import wx

from api.ODMconnection import dbconnection
#TODO get rid of *
from api.ODM2.services.readService import *
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
        '''
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('ID', 'left', 120, 'ResultID'),
            ColumnDefn('UUID', 'left', 120, 'ResultUUID'),
            ColumnDefn('Type', 'left', 120, 'ResultTypeCV'),
            ColumnDefn('Variable ID', 'left', 120, 'VariableID'),
            ColumnDefn('Units ID', 'left', 120, 'UnitsID'),
        ])
        self.list_ctrl.SetObjects(self.getSeriesData())
        '''
        self.list_ctrl.Show(False)
        self.new_button.Show(False) 
        sizer = self.GetSizer()
        sizer.Add(ResultPageView, 0, wx.ALL, 5)

    def getSeriesData(self):
        read = self.db.getReadSession()
        return read.getResults()
    
    def onButtonAdd(self, event):
        '''
        dlg = NewSeriesDialog(self, u'Create New ' + self.label)
        newResultsPanel = AddNewResultsPanelController(dlg)
        dlg.addPanel(newResultsPanel)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            print 'OK'
        else:
            pass
        dlg.Destroy()
        '''
        event.Skip()
    
    def __del__( self ):
        pass


