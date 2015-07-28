
import wx
import wx.wizard as wiz
import sys

from view.clsToolbar import ToolbarView
from controller.frmWizard import WizardController
from controller.frmWizardPage1 import WizardPage1Controller

class ToolbarController(ToolbarView):
    def __init__(self, daddy, **kwargs):
        super(ToolbarController, self).__init__(daddy, **kwargs)
        self.parent = daddy
    
    def onNewButtonClick(self, event):
        wizard = WizardController(self, title='New Data Configuration Wizard')

        page1 = WizardPage1Controller(wizard)
        #page2 = WizardPage2Controller(wizard)

        wizard.FitToPage(page1)
        
        #wiz.WizardPageSimple.Chain(page1, page2)

        if wizard.RunWizard(page1):
            wx.MessageBox('Completed Successfully', 'Info')
        else:
            wx.MessageBox('Cancelled', 'Info')
            

        event.Skip()
    
    def onDelButtonClick(self, event):
        print 'delete'
        event.Skip()
    
    def onEditButtonClick(self, event):
        print 'edit'
        event.Skip()
    
    def onRefButtonClick(self, event):
        print 'refresh'
        event.Skip()

    def onRunButtonClick(self, event):
        print 'run'
        event.Skip()

    def onNewButtonOver(self, event):
        self.parent.SetStatusText('Add a new configuration to the file.', 1)
        event.Skip()

    def onDelButtonOver(self, event):
        self.parent.SetStatusText('Delete selected configuration from the file.', 1)
        event.Skip()
    
    def onEditButtonOver(self, event):
        self.parent.SetStatusText('Edit selected configuration.', 1)
        event.Skip()



if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarController(None)
    frame.Show()
    app.MainLoop()

