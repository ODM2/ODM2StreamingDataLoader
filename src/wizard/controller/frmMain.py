
import wx
import os

import sys

from src.wizard.view.clsMain import MainView

from src.wizard.controller.frmMappingListPanel import MappingListPanel
from src.wizard.controller.frmStatusBar import StatusBarController
from src.wizard.controller.frmChainedDialog import ChainedDialog

from src.models.YamlConfiguration import YamlConfiguration
from src.models.Mapping import Mapping

WILDCARD = "YAML file (*.yaml)|*.yaml"

class MainController(MainView):
    def __init__(self, daddy, **kwargs):
        super(MainController, self).__init__(daddy,
                        title='Streaming Data Loader Wizard',
                        **kwargs)

        self.setupMenu()

        supa_sizer = wx.BoxSizer(wx.VERTICAL)

        # Status bar.
        self.status_bar = StatusBarController(self)
        self.SetStatusBar(self.status_bar)
        
        
        self.fileList = MappingListPanel(self)
        supa_sizer.Add(self.fileList, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(supa_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def setupMenu(self):
        self.menu_bar = wx.MenuBar()
        self.file_menu = wx.Menu()
        self.file_menu.Append(101, '&New Configuration File...',
            'Create a new configuration file.')
        
        self.file_menu.Enable(101, False)

        self.file_menu.Append(102, '&Load Configuration File...',
            'Open an existing configuration file.')
        self.file_menu.AppendSeparator()
        self.file_menu.Append(108, '&Save', 'Save')
        self.file_menu.Append(103, '&Save as...', 'Save as...')
        self.file_menu.Enable(108, False)

        self.file_menu.Enable(103, False)

        self.file_menu.AppendSeparator()
        self.file_menu.Append(104, '&Exit', 'Exit')

        self.menu_bar.Append(self.file_menu, '&File')
        
        self.help_menu = wx.Menu()
        self.help_menu.Append(201, '&About')

        self.menu_bar.Append(self.help_menu, '&Help')

        self.SetMenuBar(self.menu_bar)

        self.Bind(wx.EVT_MENU, self.onFileOpenClick, id=102)
        self.Bind(wx.EVT_MENU, self.onFileNewClick, id=101)
        self.Bind(wx.EVT_MENU, self.onFileSaveAsClick, id=103)
        self.Bind(wx.EVT_MENU, self.onFileSaveClick, id=108)
        self.Bind(wx.EVT_MENU, self.onFileExitClick, id=104)
        self.Bind(wx.EVT_MENU, self.onHelpAboutClick, id=201)

    def onFileOpenClick(self, event):
        '''
            The method called when a user clicks
            File->Load Configuration from the
            menu.
        '''
        # Create a file picker dialog.
        dlg = wx.FileDialog(self, message='Load Configuration File',
                defaultDir=os.getcwd(), defaultFile='',
                wildcard=WILDCARD,
                style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        # If user chose a file and clicked the "OK" button...
        if dlg.ShowModal() == wx.ID_OK:
            # Delete everything in the mapping list control.
            self.fileList.listCtrl.DeleteAllItems()
            # Get the file path(s).
            path = dlg.GetPaths()
            # Create a new YAML model object.
            # This will represent the file that
            # the user just opened.
            self.yamlConfiguration = YamlConfiguration(path[0],
                ignoreBytes=False)
            # Store a list of mappings from the file.
            #self.mappings = yamlConfiguration.get()
            # Update the object list view control.
            self.fileList.setObjects(self.yamlConfiguration.get())
            # Change the status text at the bottom of
            # the screen to display the file name.
            self.SetStatusText('File: "' + path[0] + '"', 0)
            # Enable the "New Configuration File" menu option.
            self.file_menu.Enable(101, True)
            # Enable the "Save As" menu option.
            self.file_menu.Enable(103, True)
            # Enable the "Save" menu option.
            self.file_menu.Enable(108, True)
        # Destroy the file dialog handle.
        dlg.Destroy()
        event.Skip()

    def onFileSaveAsClick(self, event):
        '''
            This method is called when the user clicks
            File->Save As from the menu.
        '''
        # Get a handle to a save file dialog.
        dlg = wx.FileDialog(self, message='Save Configuration File',
                defaultDir=os.getcwd(), defaultFile='',
                wildcard=WILDCARD,
                style=wx.SAVE)
        # If the user clicks "Ok" to save the file...
        if dlg.ShowModal() == wx.ID_OK:
            # Get the file path.
            path = dlg.GetPath()
            # Call the YamlConfiguration object's save method.
            self.yamlConfiguration.save(path)
            print self.fileList.getObjects()
            #self.mappings.save(path)
            # Change the status text to reflect the new file name. 
            self.SetStatusText('File: "' + path + '"', 0)
        # Destroy the dialog handle.
        dlg.Destroy()
        event.Skip()

    def onFileSaveClick(self, event):
        '''
            This method is called when the user clicks
            File->Save from the menu.
        '''
        self.mappings.save()
        text = self.status_bar.GetStatusText(0)
        self.SetStatusText(text.replace('*', ''), 0)
    
    def onFileNewClick(self, event):
        self.SetStatusText('File: [NEW FILE]', 0)
        self.fileList.listCtrl.DeleteAllItems()
        
        self.file_menu.Enable(103, False)
        self.file_menu.Enable(108, False)
        self.file_menu.Enable(101, False)
        
        event.Skip()
        
    def onFileExitClick(self, event):
        self.Close()
        event.Skip()

    def onHelpAboutClick(self, event):
        event.Skip()

    def onNewButtonClick(self, event):
        '''
            This method happens when the plus button
            is clicked on the toolbar.
        '''
        # Create a ChainedDialog.
        wizard = ChainedDialog(parent=self, title='New Mapping Wizard', data={})
        # Run the ChainedDialog
        newMapping = wizard.run()
        print 'data from wizard: ', newMapping
        # If the wizard was completed...
        if newMapping:
            '''
            # Enable the "Save As" menu option.
            self.file_menu.Enable(103, True)
            # Enable the "Save" menu option.
            self.file_menu.Enable(108, True)
            # Update the list control that contains the mappings.
            # Also update the in-memory list of mappings.
            #self.parent.mappings.append(Mapping(('test', newMapping)))
            #self.fileList.listCtrl.AddObject(Mapping(('test', newMapping)))
            #self.parent.mappings = self.parent.fileList.listCtrl.GetObjects()
            '''
            # First add it to the object list view.
            new_mapping = Mapping(('new_id', newMapping))
            self.fileList.addObject(new_mapping)
            # Then add it to the yamlConfiguration model.
            self.yamlConfiguration = YamlConfiguration()
            self.yamlConfiguration.addMapping(new_mapping.asTuple())
            # Enable the "New Configuration File" menu option.
            self.file_menu.Enable(101, True)
            # Enable the "Save As" menu option.
            self.file_menu.Enable(103, True)
            # Enable the "Save" menu option.
            self.file_menu.Enable(108, True)
            
        # On Windows, calling event.Skip() makes this 
        # event be called twice for some reason, so I'm
        # commenting it out.
        #event.Skip()

    def onDelButtonClick(self, event):
        '''
            This method is called when the user clicks
            the delete button from the toolbar.
        '''
        selected = self.fileList.listCtrl.GetSelectedObject()
        # Get the id of the selected mapping.
        msg_txt = selected.id
        # Display a message dialog to confirm the delete operation.
        msg = wx.MessageDialog(self,
            "Are you sure you want to delete the mapping for '%s' from this configuration file?" % (msg_txt),
            'Delete Mapping',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        # If user clicks "Yes,"...
        if msg.ShowModal() == wx.ID_YES:
            # Delete that row from the list control.
            self.fileList.listCtrl.RemoveObject(selected)
            # Update the list of mappings.
            self.parent.mappings = self.fileList.listCtrl.GetObjects()
            # Disable the delete button on the toolbar.
            parent.tb.EnableTool(20, False)
        # Destroy the message dialog handle.
        msg.Destroy()
        #event.Skip()
    
    def onEditButtonClick(self, event):
        # Get the currently selected mapping.
        selected = self.fileList.listCtrl.GetSelectedObject()
        # Create a wizard to edit the selected mapping.
        wizard = ChainedDialog(parent=self, title='Edit Mapping',
            data=selected.asTuple()[1])
        # Run the wizard and store the data which is returned.
        newMapping = wizard.run()
        # If the wizard was completed successfully...
        if newMapping:
            print 'data from wizard: ', newMapping
            # TODO
            # Return as a tuple with an id
            selected.up((selected.id, newMapping))
            self.fileList.listCtrl.RepopulateList()

        #event.Skip()

    def onRunButtonClick(self, event):
        print 'run'
        #event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame = MainController(None)
    frame.Show()
    app.MainLoop()

