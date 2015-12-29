import wx
import wx.wizard as wiz

from controller.frmDBConfig import pnlDBConfig
from controller.frmWizardPage import WizardPage
from controller.frmFileConfigPanel import FileConfigPanelController
from controller.frmDataConfigPanel import DataConfigPanelController

class WizardController(wiz.Wizard):
    def __init__(self, parent, data={}, **kwargs):
        super(WizardController, self).__init__(parent,
            id=wx.ID_ANY, bitmap=wx.NullBitmap,
            pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE,
            **kwargs)
        # In order for validation to work on widgets within
        # a panel, you must set this extra style.
        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
        
        self.page1 = self.createPages()
        self.metadata = data

    def createPages(self):
        
        page1 = WizardPage(self)
        page2 = WizardPage(self)
        page3 = WizardPage(self)
        
        databasePanel = pnlDBConfig(page1, None)        
        filePanel = FileConfigPanelController(page2)
        dataPanel = DataConfigPanelController(page3)

        page1.addPanel(databasePanel)
        page2.addPanel(filePanel)
        page3.addPanel(dataPanel)

        page2.SetPrev(page1)
        page1.SetNext(page2)
        
        page2.SetNext(page3)
        page3.SetPrev(page2)

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
        panels = page.getPanels()

        # If moving forward in the wizard...
        if event.GetDirection():
            try:
                prev_panels = page.GetPrev().getPanels()
                for pp in prev_panels:
                    for p in panels:
                        p.populate(data=pp.getInput())
            except AttributeError as e:
                for p in panels:
                    p.populate(data=self.metadata)
                    
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
        #self.metadata = event.GetPage().getPanel().getInput()
        panels = event.GetPage().getPanels()
        for p in panels:
            self.metadata.update(p.getInput())
        event.Skip()
        
    def run(self):
        self.FitToPage(self.page1)
        if self.RunWizard(self.page1):
            return self.metadata
        return None

