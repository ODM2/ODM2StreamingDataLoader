import wx
import wx.wizard as wiz

from controller.frmDBConfig import pnlDBConfig
from controller.frmWizardPage import WizardPage
from controller.frmFileConfigPanel import FileConfigPanelController
from controller.frmDataConfigPanel import DataConfigPanelController

class WizardController(wiz.Wizard):
    def __init__(self, parent, **kwargs):
        super(WizardController, self).__init__(parent,
            id=wx.ID_ANY, bitmap=wx.NullBitmap,
            pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE,
            **kwargs)
        
        # In order for validation to work on widgets within
        # a panel, you must set this extra style.
        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
        
        self.page1 = self.createPages()

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

        return page1

    def onPageChange(self, event):
        '''
        Event which takes place as the user clicks the 'next'
        or 'previous' button.
        '''

        page = event.GetPage()
        panel = page.getPanel()
        
        if event.GetDirection():
            # Validate all of the children widgets.
            page.Validate()
            
            next_page = page.GetNext()
            
            try:
                print 'tick...\n'
                next_panel = next_page.getPanel()
                next_panel.populate(data=panel.getInput())
            
            except AttributeError as e:
                pass
       
        event.Skip()
        
    def run(self):
        self.FitToPage(self.page1)
        return self.RunWizard(self.page1)

