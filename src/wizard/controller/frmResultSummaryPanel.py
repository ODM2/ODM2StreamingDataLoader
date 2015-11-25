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
        self.Bind(wx.EVT_SHOW, self.onShow)
        self.parent = parent
    
    def getSeriesData(self):
        read = self.parent.database.getReadSession()
        return read.getResults()
    
    def onButtonAdd(self, event):
        event.Skip()
    
    def onShow(self, event):
        if event.GetShow() is True:
            for i in self.parent.getSelections():
                if "SamplingFeatures" in str(i):
                    self.getSamplingFeatureSummary(i)
                elif "Variables" in str(i):
                    self.getVariablesSummary(i)
                elif "Units" in str(i):
                    self.getUnitsSummary(i)
                elif "ProcessingLevels" in str(i):
                    self.getProcessingLevelSummary(i)
                elif "Actions" in str(i):
                    self.getActionsSummary(i)
        event.Skip()

    def getSamplingFeatureSummary(self, obj):
        self.txtSum.Freeze()
        
        self.txtSum.BeginBold()
        self.txtSum.BeginUnderline()
        self.txtSum.WriteText("Sampling Feature")
        self.txtSum.EndBold()
        self.txtSum.EndUnderline()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Code: ")
        self.txtSum.BeginItalic()
        self.txtSum.WriteText(str(obj.SamplingFeatureCode))
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Name: ")
        self.txtSum.BeginItalic()
        if not obj.SamplingFeatureName:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.SamplingFeatureName))
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Type: ")
        self.txtSum.BeginItalic()
        if not obj.SamplingFeatureTypeCV:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.SamplingFeatureTypeCV))
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Description: ")
        self.txtSum.BeginItalic()
        if not obj.SamplingFeatureDescription:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.SamplingFeatureDescription))
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Geotype: ")
        self.txtSum.BeginItalic()
        if not obj.SamplingFeatureGeotypeCV:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.SamplingFeatureGeotypeCV))
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Elevation: ")
        self.txtSum.BeginItalic()
        if not obj.Elevation_m:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.Elevation_m) + " meters")
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.Thaw()
