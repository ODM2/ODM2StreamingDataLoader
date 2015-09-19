
import wx
import wx.wizard as wiz
import sys

from src.wizard.view.clsToolbar import ToolbarView
#from controller.frmWizard import WizardController
from src.wizard.controller.frmChainedDialog import ChainedDialog

class ToolbarController(ToolbarView):
    def __init__(self, daddy, **kwargs):
        super(ToolbarController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        self.del_btn.Enable(False)
        self.ref_btn.Enable(False)
        self.run_btn.Enable(False)
        self.edit_btn.Enable(False)
    
    def onNewButtonClick(self, event):
        '''
            This method happens when the plus button
            is clicked on the toolbar.
        '''
        print "onNewButtonClick"
        # Create a ChainedDialog.
        wizard = ChainedDialog(parent=self, title='New Mapping Wizard', data={})
        # Run the ChainedDialog
        newMapping = wizard.run()
        print 'data from wizard: ', newMapping
        # If the wizard was completed...
        if newMapping:
            # Update the list control that contains the mappings.
            self.parent.fileList.populateRows([('tester', newMapping)])
            # Also update the in-memory list of mappings.
            self.parent.mappings = [('test', newMapping)]
        # On Windows, calling event.Skip() makes this 
        # event be called twice for some reason, so I'm
        # commenting it out.
        #event.Skip()
    
    def onDelButtonClick(self, event):
        '''
            This method is called when the user clicks
            the delete button from the toolbar.
        '''
        # Get the path of the selected mapping.
        msg_txt = self.parent.fileList.getSelectionTextByColumn(3)
        # Display a message dialog to confirm the delete operation.
        msg = wx.MessageDialog(self,
            "Are you sure you want to delete the mapping for '%s' from this configuration file?" % (msg_txt),
            'Delete Mapping',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        # If user clicks "Yes,"...
        if msg.ShowModal() == wx.ID_YES:
            # Get the selected row from the list control. 
            row = self.parent.fileList.getSelection()
            # Delete that row from the list control.
            self.parent.fileList.deleteRow(row)
            # Disable the delete button on the toolbar.
            self.parent.toolbar.del_btn.Enable(False)
        # Destroy the message dialog handle.
        msg.Destroy()
        #event.Skip()
    
    def onEditButtonClick(self, event):
        # Get the currently selected mapping.
        mapping = self.parent.fileList.getSelectionTextByColumn(0)
        # Create a wizard to edit the selected mapping.
        wizard = ChainedDialog(parent=self, title='Edit Mapping',
            data=self.parent.mappings[mapping][1])
        # Run the wizard and store the data which is returned.
        newMapping = wizard.run()
        # If the wizard was completed successfully...
        if newMapping:
            print 'data from wizard: ', newMapping
            self.parent.mappings[mapping][1].update(newMapping)
            
            #self.parent.fileList.populateRows(self.parent.mappings)
            #self.parent.fileList.updateRow(\
            #    self.parent.fileList.fileListCtrl.GetFirstSelected(), newMapping)

        #event.Skip()
    
    def onRefButtonClick(self, event):
        print 'refresh'
        #event.Skip()

    def onRunButtonClick(self, event):
        print 'run'
        #event.Skip()

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

