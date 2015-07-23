
import wx
import wx.wizard as wiz
import sys

from view.clsToolbar import ToolbarView
from controller.frmWizard import WizardController
from controller.frmWizardPage import WizardPageController

class ToolbarController(ToolbarView):
    def __init__(self, daddy, **kwargs):
        super(ToolbarController, self).__init__(daddy, **kwargs)

    def OnNewButtonClick(self, event):
        wizard = WizardController(self, 'New Data Configuration Wizard')
        page1 = WizardPageController(wizard)
        page2 = WizardPageController(wizard)

        wizard.FitToPage(page1)
        
        wiz.WizardPageSimple.Chain(page1, page2)

        if wizard.RunWizard(page1):
            wx.MessageBox('Completed Successfully', 'Info')
        else:
            wx.MessageBox('Cancelled', 'Info')
            

        event.Skip()
    
    def OnDelButtonClick(self, event):
        print 'delete'
        event.Skip()
    
    def OnEditButtonClick(self, event):
        print 'edit'
        event.Skip()
    
    def OnRefButtonClick(self, event):
        print 'refresh'
        event.Skip()

    def OnRunButtonClick(self, event):
        print 'run'
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarController(None)
    frame.Show()
    app.MainLoop()

