import wx
import wx.wizard as wiz

from src.wizard.controller.frmWizardPage import WizardPage
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel
from src.wizard.controller.frmSampFeatSelectPanel import SampFeatSelectPanel
from src.wizard.controller.frmProcLevelSelectPanel import ProcLevelSelectPanel
from src.wizard.controller.frmActionsSelectPanel import ActionsSelectPanel
from src.wizard.controller.frmResultsSelectPanel import ResultsSelectPanel
from src.wizard.controller.frmVariableSelectPanel import VariableSelectPanel
from src.wizard.controller.frmUnitSelectPanel import UnitSelectPanel

class SeriesWizardController(wiz.Wizard):
    def __init__(self, parent, label, **kwargs):
        super(SeriesWizardController, self).__init__(parent,
            id=wx.ID_ANY, bitmap=wx.NullBitmap,
            pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE,
            **kwargs)
        
        # In order for validation to work on widgets within
        # a panel, you must set this extra style.
        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
        
        self.page1 = self.createPages()
        self.metadata = {0: label}

    def createPages(self):
        
        page1 = WizardPage(self)
        page2 = WizardPage(self)
        page3 = WizardPage(self)
        page4 = WizardPage(self)
        page5 = WizardPage(self)
        page6 = WizardPage(self)

        sampFeatSelectPanel = SampFeatSelectPanel(page1,
            u'Sampling Feature')
        variableSelectPanel = VariableSelectPanel(page2, u'Variable')
        unitsSelectPanel = UnitSelectPanel(page3, u'Units')
        procLevelSelectPanel = ProcLevelSelectPanel(page4,
            u'Processing Level')
        actionsSelectPanel = ActionsSelectPanel(page5, u'Actions')
        resultsSelectPanel = ResultsSelectPanel(page6, u'Results')

        page1.addPanel(sampFeatSelectPanel)
        page2.addPanel(variableSelectPanel)
        page3.addPanel(unitsSelectPanel)
        page4.addPanel(procLevelSelectPanel)
        page5.addPanel(actionsSelectPanel)
        page6.addPanel(resultsSelectPanel)

        page1.SetNext(page2)
        page2.SetPrev(page1)
        page2.SetNext(page3)
        page3.SetPrev(page2)
        page3.SetNext(page4)
        page4.SetPrev(page3)
        page4.SetNext(page5)
        page5.SetPrev(page4)
        page5.SetNext(page6)
        page6.SetPrev(page5)

        self.Bind(wiz.EVT_WIZARD_PAGE_CHANGING, self.onPageChange)
        self.Bind(wiz.EVT_WIZARD_PAGE_CHANGED, self.onPageChanged)
        self.Bind(wiz.EVT_WIZARD_FINISHED, self.onFinished)

        return page1

    def onPageChanged(self, event):
        '''
        Event which takes place after the user has clicked
        'next' or 'back' button.
        '''
        page = event.GetPage()
        panel = page.getPanel()

        # If moving forward in the wizard...
        if event.GetDirection():
            try:
                prev_panel = page.GetPrev().getPanel()
                panel.populate(data=prev_panel.getInput())
            except AttributeError as e:
                print e

        event.Skip()
    
    def onPageChange(self, event):
        '''
        Event which takes place after the user clicks the 'next'
        or 'previous' button, but before the next page is called.
        '''
        # If moving forward in the wizard...
        if event.GetDirection():
            page = event.GetPage()
            # Validate all of the children widgets.
            #page.Validate()
        
        event.Skip()

    def onFinished(self, event):
        self.metadata = event.GetPage().getPanel().getInput()
        event.Skip()
        
    def run(self):
        self.FitToPage(self.page1)
        if self.RunWizard(self.page1):
            return self.metadata
        return None

