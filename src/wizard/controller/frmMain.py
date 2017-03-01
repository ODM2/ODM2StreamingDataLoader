
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
        self.hasUnsavedChanges = False
        self.currentPath = None
        self.Bind(wx.EVT_CLOSE, self.onClosing)
        # Container for mappings.
        self.yamlConfiguration = YamlConfiguration()
        # Set up the window menu.
        self.setupMenu()
        # Create the main sizer.
        supa_sizer = wx.BoxSizer(wx.VERTICAL)
        # Status bar.
        self.status_bar = StatusBarController(self)
        self.SetStatusBar(self.status_bar)
        # Initialize the model list view table. TODO change the name.
        self.fileList = MappingListPanel(self)
        # Add it to the sizer.
        supa_sizer.Add(self.fileList, 1, wx.EXPAND | wx.ALL, 5)
        # Set the sizer to the window.
        self.SetSizer(supa_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

    def setupMenu(self):
        self.menu_bar = wx.MenuBar()
        self.file_menu = wx.Menu()
        self.file_menu.Append(101, '&New Configuration File...', 'Create a new configuration file.')
        
        self.file_menu.Enable(101, False)

        self.file_menu.Append(102, '&Load Configuration File...\tCtrl+O', 'Open an existing configuration file.')
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
            self.currentPath = path[0]
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
            self.currentPath = path
            # Enable the "Save" menu option.
            self.file_menu.Enable(108, True)
            #print self.fileList.getObjects()
            # Change the status text to reflect the new file name. 
            self.SetStatusText('File: "' + path + '"', 0)
            self.hasUnsavedChanges = False
        # Destroy the dialog handle.
        dlg.Destroy()

    def onFileSaveClick(self, event):
        '''
            This method is called when the user clicks
            File->Save from the menu.
        '''
        self.yamlConfiguration.save(self.currentPath)
        text = self.status_bar.GetStatusText(0)
        self.SetStatusText(text.replace('*', ''), 0)
        self.hasUnsavedChanges = False
    
    def onFileNewClick(self, event):
        self.checkForSavedChanges()
        self.SetStatusText('File: <NEW FILE>', 0)
        self.fileList.listCtrl.DeleteAllItems()
        self.yamlConfiguration.deleteMappings() 
        self.file_menu.Enable(103, False)
        self.file_menu.Enable(108, False)
        self.file_menu.Enable(101, False)
        
        self.currentPath = None

        event.Skip()
        
    def onFileExitClick(self, event):
        self.Close()
        event.Skip()

    def checkForSavedChanges(self):
        if self.hasUnsavedChanges:
            dlg = wx.MessageBox("This file has unsaved changes. Do you want to save the changes before closing?", "Unsaved Changes", style=wx.YES_NO|wx.YES_DEFAULT)
            self.hasUnsavedChanges = False
            if dlg == wx.YES:
                if self.currentPath:
                    self.onFileSaveClick(None)
                else:
                    self.onFileSaveAsClick(None)
                self.hasUnsavedChanges = False
                text = self.status_bar.GetStatusText(0)
                self.SetStatusText(text.replace('*', ''), 0)
        

    def onClosing(self, event):
        self.checkForSavedChanges()
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
        wizard.CenterOnScreen()
        newMapping = wizard.run()
        # If the wizard was completed...
        if newMapping:
            # Ask for an id
            idDialog = wx.TextEntryDialog(parent=self, message="Enter a unique ID for the new mapping.",
                                          caption="Mapping ID",
                                          pos=wx.DefaultPosition)
            # Inline function to make sure that
            # a valid id is entered.
            def fn():
                idDialog.ShowModal()
                if self.fileList.exists(idDialog.GetValue()):
                    wx.MessageBox('A mapping with ID "%s" already exists in this file.' % idDialog.GetValue(),\
                    'Unique ID Error')
                    fn()
                return idDialog.GetValue()
            # Store id for mapping as a str.
            mappingId = str(fn()) 
            # Create a Mapping object with the new info. 
            new_mapping = Mapping((mappingId, newMapping))
            # Then add it to the object list view table.
            self.fileList.addObject(new_mapping)
            # Then add it to the yamlConfiguration model.
            self.yamlConfiguration.addMapping(new_mapping.asTuple())
            # Enable the "New Configuration File" menu option.
            self.file_menu.Enable(101, True)
            # Enable the "Save As" menu option.
            self.file_menu.Enable(103, True)
            # Enable the "Save" menu option.
            #self.file_menu.Enable(108, True)
            text = self.status_bar.GetStatusText(0)
            if text[-1] != "*":
                self.SetStatusText(text + "*", 0)
            self.hasUnsavedChanges = True
            
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
            self.fileList.removeObject(selected)
            # Delete it from the yamlConfiguration model too.
            self.yamlConfiguration.deleteMapping(selected) 
            # Disable the delete button on the toolbar.
            self.tb.EnableTool(20, False)
            # Disable the edit button on the toolbar.
            self.tb.EnableTool(30, False)
            self.hasUnsavedChanges = True
            text = self.status_bar.GetStatusText(0)
            if text[-1] != "*":
                self.SetStatusText(text + "*", 0)
        # Destroy the message dialog handle.
        msg.Destroy()
    
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
            # Return as a tuple with an id
            selected.up((selected.id, newMapping))
            self.fileList.listCtrl.RepopulateList()
            self.hasUnsavedChanges = True
            text = self.status_bar.GetStatusText(0)
            if text[-1] != "*":
                self.SetStatusText(text + "*", 0)

    def onRunButtonClick(self, event):
        executable_path = sys.executable

        if hasattr(sys, 'frozen'):
            path = os.path.dirname(executable_path)

            streaming_data_loader_name = 'StreamingDataLoader.exe'
            if sys.platform == 'darwin':
                streaming_data_loader_name = 'StreamingDataLoader'

            path = os.path.join(path, streaming_data_loader_name)

            # if ' ' in self.currentPath:
            #     self.currentPath = "\"" + self.currentPath + "\""
            #
            # if ' ' in path:
            #     path = "\"" + path + "\""

            # command = path + ' -c ' + self.currentPath

            command = '""%s" -c "%s""' % (path, self.currentPath)

            # command = command.replace('\\', '/')
            print "vvvvvvvvvvvvvvvv"
            print command
            print "^^^^^^^^^^^^^^^^"
            os.system(command)
            # os.system(path + ' -c ' + self.currentPath)
        else:
            os.system(executable_path + " " + os.path.join(sys.path[1], 'StreamingDataLoader.py') + ' -c ' + self.currentPath)
