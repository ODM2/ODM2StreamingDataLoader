import wx
import wx.wizard as wiz

from controller.frmWizardPage import WizardPage
from controller.frmSeriesSelectPanel import SeriesSelectPanel

class SeriesWizardController(wiz.Wizard):
    def __init__(self, parent, **kwargs):
        super(SeriesWizardController, self).__init__(parent,
            id=wx.ID_ANY, bitmap=wx.NullBitmap,
            pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE,
            **kwargs)
        
        # In order for validation to work on widgets within
        # a panel, you must set this extra style.
        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
        
        self.page1 = self.createPages()
        self.metadata = {}

    def createPages(self):
        
        page1 = WizardPage(self)
        page2 = WizardPage(self)
        page3 = WizardPage(self)
        page4 = WizardPage(self)

        variableSelectPanel = SeriesSelectPanel(page1, u'Variable')
        unitSelectPanel = SeriesSelectPanel(page2, u'Unit')
        procLevelSelectPanel = SeriesSelectPanel(page3,
            u'Processing Level')
        methodSelectPanel = SeriesSelectPanel(page4, u'Method')

        page1.addPanel(variableSelectPanel)
        page2.addPanel(unitSelectPanel)
        page3.addPanel(procLevelSelectPanel)
        page4.addPanel(methodSelectPanel)

        page1.SetNext(page2)
        page2.SetPrev(page1)
        page2.SetNext(page3)
        page3.SetPrev(page2)
        page3.SetNext(page4)
        page4.SetPrev(page3)

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
