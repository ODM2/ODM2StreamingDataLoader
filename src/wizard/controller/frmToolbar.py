
import wx
import wx.wizard as wiz
import sys

from view.clsToolbar import ToolbarView
from controller.frmWizard import WizardController

class ToolbarController(ToolbarView):
    def __init__(self, daddy, **kwargs):
        super(ToolbarController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        self.del_btn.Enable(False)
        self.ref_btn.Enable(False)
        self.run_btn.Enable(False)
        self.edit_btn.Enable(False)
    
    def onNewButtonClick(self, event):
        
        wizard = WizardController(self, title='Harry Potter Wizard')
        newMapping = wizard.run()
        if newMapping:
            print 'data from wizard: ', newMapping
            self.parent.fileList.appendRow(newMapping)

            self.parent.mappings.update(newMapping)

        event.Skip()
    
    def onDelButtonClick(self, event):
        msg_txt = self.parent.fileList.getSelectionTextByColumn(3)
        msg = wx.MessageDialog(self,
            "Are you sure you want to delete the mapping for '%s' from this configuration file?" % (msg_txt),
            'Delete Mapping',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        if msg.ShowModal() == wx.ID_YES:
            row = self.parent.fileList.getSelection()
            self.parent.fileList.deleteRow(row)
            self.parent.toolbar.del_btn.Enable(False)

        msg.Destroy()

        event.Skip()
    
    def onEditButtonClick(self, event):
        wizard = WizardController(self, title='Edit Mapping', data=self.parent.mappings)
        newMapping = wizard.run()
        if newMapping:
            print 'data from wizard: ', newMapping
            self.parent.mappings.update(newMapping)
            self.parent.fileList.updateRow(\
                self.parent.fileList.fileListCtrl.GetFirstSelected(), newMapping)

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

