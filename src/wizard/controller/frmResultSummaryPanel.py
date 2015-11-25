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
   
        self.fontColor = wx.Colour(67, 79, 112)

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
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.WriteText(str(obj.SamplingFeatureCode))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()

        self.txtSum.WriteText("Name: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.SamplingFeatureName:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.SamplingFeatureName))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Type: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        if not obj.SamplingFeatureTypeCV:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.SamplingFeatureTypeCV))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Description: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.SamplingFeatureDescription:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.SamplingFeatureDescription))
        self.txtSum.EndItalic()
        self.txtSum.EndTextColour()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Geotype: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.SamplingFeatureGeotypeCV:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.SamplingFeatureGeotypeCV))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Elevation: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        if not obj.Elevation_m:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.Elevation_m) + " meters")
        self.txtSum.EndItalic()
        self.txtSum.EndTextColour()
        self.txtSum.Newline()
        
        self.txtSum.Thaw()
    
    def getVariablesSummary(self, obj):
        self.txtSum.Freeze()
        
        self.txtSum.BeginBold()
        self.txtSum.BeginUnderline()
        self.txtSum.WriteText("Variable")
        self.txtSum.EndBold()
        self.txtSum.EndUnderline()
        self.txtSum.Newline()
       
        self.txtSum.WriteText("Code: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.WriteText(str(obj.VariableCode))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()

        self.txtSum.WriteText("Name: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.VariableNameCV:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.VariableNameCV))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Type: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        if not obj.VariableTypeCV:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.VariableTypeCV))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Definition: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.VariableDefinition:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.VariableDefinition))
        self.txtSum.EndItalic()
        self.txtSum.EndTextColour()
        self.txtSum.Newline()
        
        self.txtSum.Thaw()
        
    def getUnitsSummary(self, obj):
        self.txtSum.Freeze()
        
        self.txtSum.BeginBold()
        self.txtSum.BeginUnderline()
        self.txtSum.WriteText("Unit")
        self.txtSum.EndBold()
        self.txtSum.EndUnderline()
        self.txtSum.Newline()
       
        self.txtSum.WriteText("Abbreviation: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.WriteText(str(obj.UnitsAbbreviation))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()

        self.txtSum.WriteText("Name: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.UnitsName:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.UnitsName))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Type: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        if not obj.UnitsTypeCV:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.UnitsTypeCV))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Link: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.UnitsLink:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.BeginURL(obj.UnitsLink)
            self.txtSum.WriteText(str(obj.UnitsLink))
            self.txtSum.EndURL()
        self.txtSum.EndItalic()
        self.txtSum.EndTextColour()
        self.txtSum.Newline()
        
        self.txtSum.Thaw()
    
    def getProcessingLevelSummary(self, obj):
        self.txtSum.Freeze()
        
        self.txtSum.BeginBold()
        self.txtSum.BeginUnderline()
        self.txtSum.WriteText("Processing Level")
        self.txtSum.EndBold()
        self.txtSum.EndUnderline()
        self.txtSum.Newline()
       
        self.txtSum.WriteText("Code: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.WriteText(str(obj.ProcessingLevelCode))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()

        self.txtSum.WriteText("Definition: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.Definition:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.Definition))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Explanation: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        if not obj.Explanation:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.Explanation))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.Thaw()
    
    def getActionsSummary(self, obj):
        self.txtSum.Freeze()
        
        self.txtSum.BeginBold()
        self.txtSum.BeginUnderline()
        self.txtSum.WriteText("Action")
        self.txtSum.EndBold()
        self.txtSum.EndUnderline()
        self.txtSum.Newline()
       
        self.txtSum.WriteText("ID: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.WriteText(str(obj.ActionID))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()

        self.txtSum.WriteText("Type: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.ActionTypeCV:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.ActionTypeCV))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Description: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        if not obj.ActionDescription:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.ActionDescription))
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Method ID: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.MethodID:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.MethodID))
        self.txtSum.EndItalic()
        self.txtSum.EndTextColour()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("Begin Time: ")
        self.txtSum.BeginTextColour(self.fontColor)
        self.txtSum.BeginItalic()
        if not obj.BeginDateTime:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.BeginDateTime) + " (UTC Offset " + str(obj.BeginDateTimeUTCOffset) + ")")
        self.txtSum.EndTextColour()
        self.txtSum.EndItalic()
        self.txtSum.Newline()
        
        self.txtSum.WriteText("End Time: ")
        self.txtSum.BeginItalic()
        self.txtSum.BeginTextColour(self.fontColor)
        if not obj.EndDateTime:
            self.txtSum.WriteText("--")
        else:
            self.txtSum.WriteText(str(obj.EndDateTime) + " (UTC Offset " + str(obj.EndDateTimeUTCOffset) + ")")
        self.txtSum.EndItalic()
        self.txtSum.EndTextColour()
        self.txtSum.Newline()
        
        self.txtSum.Thaw()
