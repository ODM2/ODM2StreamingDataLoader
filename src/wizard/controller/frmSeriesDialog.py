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

class SeriesSelectDialog(CustomDialog):
    def __init__(self, parent, variable, database):
        super(SeriesSelectDialog, self).__init__(\
            parent=parent,
            title="Select Result for %s" % variable)
        self.database = database

        read = database.getReadSession()
        #read.getDetailedResultInfo("Time series coverage")
        seriesSelectPanel = SeriesSelectPanelView(self)
        self.addPanel(seriesSelectPanel)

        seriesSelectPanel.newBtn.Bind(wx.EVT_BUTTON, self.onNew)

        seriesSelectPanel.listCtrl.SetObjects(read.getDetailedResultInfo("Time series coverage"))

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

