import wx

from src.wizard.view.clsSeriesSelectPanel \
    import SeriesSelectPanelView
from src.wizard.view.clsCustomDialog \
    import CustomDialog
from src.wizard.controller.frmSeriesWizard \
    import SeriesWizardController

from src.wizard.controller.WizardDialog \
    import WizardDialog

from src.wizard.controller.frmSampFeatSelectPanel \
    import SampFeatSelectPanel
from src.wizard.controller.frmVariableSelectPanel \
    import VariableSelectPanel
from src.wizard.controller.frmUnitSelectPanel \
    import UnitSelectPanel
from src.wizard.controller.frmProcLevelSelectPanel \
    import ProcLevelSelectPanel
from src.wizard.controller.frmActionsSelectPanel \
    import ActionsSelectPanel
from src.wizard.controller.frmResultSummaryPanel \
    import ResultSummaryPanel

from api.ODM2.services.readService \
    import DetailedResult

class ResultMapping(DetailedResult):
    def __init__(self, result, samplingFeature,
        method, variable, processingLevel,
        unit, variableName=""):

        self.resultID=result
        self.samplingFeatureCode=samplingFeature
        self.methodCode=method
        self.variableCode=variable
        self.processingLevelCode=processingLevel
        self.unitsName=unit
        self.variableName = variableName



class SeriesSelectDialog(CustomDialog):
    def __init__(self, parent, variable, database):
        super(SeriesSelectDialog, self).__init__(\
            parent=parent,
            title="Select Result for %s" % variable)
        self.database = database

        read = database.getReadSession()
        #read.getDetailedResultInfo("Time series coverage")
        self.seriesSelectPanel = SeriesSelectPanelView(self)
        self.addPanel(self.seriesSelectPanel)

        self.seriesSelectPanel.newBtn.Bind(wx.EVT_BUTTON, self.onNew)
        self.seriesSelectPanel.okBtn.Bind(wx.EVT_BUTTON, self.onOK)

        self.seriesSelectPanel.listCtrl.SetObjects(read.getDetailedResultInfo("Time series coverage"))

    # ================== #
    # > Event Handlers < #
    # ================== #

    def onNew(self, event):
        wiz = WizardDialog(self,
            database=self.database,
            title="New Result Wizard")
        
        wiz.addPage(SampFeatSelectPanel) 
        wiz.addPage(VariableSelectPanel) 
        wiz.addPage(UnitSelectPanel) 
        wiz.addPage(ProcLevelSelectPanel) 
        wiz.addPage(ActionsSelectPanel) 
        #wiz.addPage(ResultPageView)
        wiz.addPage(ResultSummaryPanel)
        
        wiz.CenterOnScreen()
        wiz.ShowModal()
        
        event.Skip()

    def onOK(self, event):
        obj = self.seriesSelectPanel.listCtrl.GetSelectedObject()
        
        mapping = ResultMapping(obj.resultID,
            obj.samplingFeatureCode,
            obj.methodCode,
            obj.variableCode,
            obj.processingLevelCode,
            obj.unitsName)

        self.selectedResult = mapping

        event.Skip()



