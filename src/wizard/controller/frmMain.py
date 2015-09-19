
import wx
import os

import sys
sys.path.append("/Users/Stephanie/DEV/StreamingDataLoader/src")
sys.path.append("/Users/Stephanie/DEV/StreamingDataLoader/src/wizard")

from src.wizard.view.clsMain import MainView

from src.wizard.controller.frmToolbar import ToolbarController
#from src.wizard.controller.frmFileList import FileListController
from src.wizard.controller.frmMappingListPanel import MappingListPanel
from src.wizard.controller.frmStatusBar import StatusBarController

from src.models.YamlConfiguration import YamlConfiguration

WILDCARD = "YAML file (*.yaml)|*.yaml"

class MainController(MainView):
    def __init__(self, daddy, **kwargs):
        super(MainController, self).__init__(daddy,
                        title='Streaming Data Loader Wizard',
                        **kwargs)

        self.setupMenu()

        supa_sizer = wx.FlexGridSizer(2, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # Status bar.
        self.status_bar = StatusBarController(self)
        self.SetStatusBar(self.status_bar)
        
        # Panel for the tool bar.
        self.toolbar = ToolbarController(self)
        
        #self.fileList = FileListController(self)
        self.fileList = MappingListPanel(self)
        supa_sizer.Add(self.toolbar, 0, wx.EXPAND | wx.ALL, 5)
        supa_sizer.Add(self.fileList, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(supa_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

        self.mappings = None

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
            self.fileList.fileListCtrl.DeleteAllItems()
            # Get the file path(s).
            path = dlg.GetPaths()
            # Create a new YAML model object.
            # This will represent the file that
            # the user just opened.
            yamlConfiguration = YamlConfiguration(path[0],
                ignoreBytes=False)
            self.mappings = yamlConfiguration.get()
            # Now try to get a list of the mappings
            # that are inside of the file.
            self.fileList.populateRows(self.mappings)
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
            self.mappings.save(path)
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
        self.fileList.fileListCtrl.DeleteAllItems()
        
        self.file_menu.Enable(103, False)
        self.file_menu.Enable(108, False)
        self.file_menu.Enable(101, False)
        
        event.Skip()
        
    def onFileExitClick(self, event):
        self.Close()
        event.Skip()

    def onHelpAboutClick(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame = MainController(None)
    frame.Show()
    app.MainLoop()

