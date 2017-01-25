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

from odm2api.ODM2.services.readService \
    import DetailedResult

from src.wizard.models.ResultMapping import ResultMapping

class SeriesSelectDialog(CustomDialog):
    def __init__(self, parent, variable, database):
        super(SeriesSelectDialog, self).__init__(parent=parent, title="Select Result for %s" % variable, size=wx.Size(700, 500))
        self.database = database

        read = database.getReadSession()
        self.existingResult = None
        #read.getDetailedResultInfo("Time series coverage")
        self.seriesSelectPanel = SeriesSelectPanelView(self)
        self.addPanel(self.seriesSelectPanel)
        self.seriesSelectPanel.okBtn.Disable()

        self.seriesSelectPanel.newBtn.Bind(wx.EVT_BUTTON, self.onNew)
        self.seriesSelectPanel.editBtn.Bind(wx.EVT_BUTTON, self.onEdit)
        self.seriesSelectPanel.okBtn.Bind(wx.EVT_BUTTON, self.onOK)

        #self.seriesSelectPanel.listCtrl.SetObjects(read.getDetailedResultInfo("Time series coverage"))
        detailedResults = read.getDetailedResultInfo("Time series coverage")
        self.seriesSelectPanel.listCtrl.SetObjects(detailedResults)

        self.seriesSelectPanel.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.enable)
        self.seriesSelectPanel.listCtrl.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.on_deselect_item)

    # ================== #
    # > Event Handlers < #
    # ================== #

    def on_deselect_item(self, event):
        self.seriesSelectPanel.okBtn.Disable()

    def onNew(self, event):
        wiz = WizardDialog(self, database=self.database, title="New Result Wizard", result=None)
        
        wiz.addPage(SampFeatSelectPanel) 
        wiz.addPage(VariableSelectPanel) 
        wiz.addPage(UnitSelectPanel) 
        wiz.addPage(ProcLevelSelectPanel) 
        wiz.addPage(ActionsSelectPanel) 
        #wiz.addPage(ResultPageView)
        wiz.addPage(ResultSummaryPanel)

        wiz.CenterOnParent()
        if wiz.ShowModal() == wx.ID_OK:
            wiz.Center()
            read = self.database.getReadSession()
            r = read.getDetailedResultInfo("Time series coverage", 
                                            wiz.result.ResultID)
            r_id = r[0].resultID
            detailedResults = read.getDetailedResultInfo("Time series coverage")
            self.seriesSelectPanel.listCtrl.SetObjects(detailedResults)

            for i in detailedResults:
                if i.resultID == r_id:
                    self.seriesSelectPanel.listCtrl.SelectObject(\
                        i, deselectOthers=True,
                        ensureVisible=True)
        else:
            pass
            #wx.MessageBox('An error occurred while creating a new result', 'Error')
        
        event.Skip()

    def enable(self, event):
        self.seriesSelectPanel.editBtn.Enable()
        self.seriesSelectPanel.okBtn.Enable()
        self.existingResult = self.seriesSelectPanel.listCtrl.GetSelectedObject()

    def Warning(parent, message, caption ='Warning!'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy()

    def onEdit(self, event):
        message = 'Warning, you may clobber the integrity of your data when using this feature'
        dlg = wx.MessageDialog(self, message=message, caption='Warning')
        dlg.SetOKCancelLabels(ok="Continue", cancel="Cancel")

        if dlg.ShowModal() == wx.ID_OK:
            wiz = WizardDialog(self, database=self.database, title="Edit Result Wizard", result=self.existingResult)
            wiz.centerSelf()
            wiz.addPage(SampFeatSelectPanel)
            wiz.addPage(VariableSelectPanel)
            wiz.addPage(UnitSelectPanel)
            wiz.addPage(ProcLevelSelectPanel)
            wiz.addPage(ActionsSelectPanel)
            wiz.addPage(ResultSummaryPanel)
            wiz.CenterOnParent()
            wiz.ShowModal()

        dlg.Destroy()

    def onOK(self, event):
        obj = self.seriesSelectPanel.listCtrl.GetSelectedObject()
        print obj.variableNameCV

        mapping = ResultMapping(obj.resultID,
            obj.samplingFeatureCode,
            obj.samplingFeatureName,
            obj.methodCode,
            obj.methodName,
            obj.variableCode,
            obj.variableNameCV,
            obj.processingLevelCode,
            obj.processingLevelDef,
            obj.unitsName)

        self.selectedResult = mapping

        event.Skip()
