
import wx
import wx.wizard as wiz
import sys

from view.clsToolbar import ToolbarView
from controller.frmWizard import WizardController

class ToolbarController(ToolbarView):
    def __init__(self, daddy, **kwargs):
        super(ToolbarController, self).__init__(daddy, **kwargs)
        self.parent = daddy
    
    def onNewButtonClick(self, event):
        
        wizard = WizardController(self, title='New Data Wizard')
        wizard.run() 
        
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

