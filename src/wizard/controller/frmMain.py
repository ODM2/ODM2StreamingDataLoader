
import wx
import os

import sys
sys.path.append("/Users/Stephanie/DEV/StreamingDataLoader/src")
sys.path.append("/Users/Stephanie/DEV/StreamingDataLoader/src/wizard")

from view.clsMain import MainView

from controller.frmToolbar import ToolbarController
from controller.frmFileList import FileListController
from controller.frmStatusBar import StatusBarController

WILDCARD = "YAML file (*.yaml)|*.yaml"

class MainController(MainView):
    def __init__(self, daddy, **kwargs):
        super(MainController, self).__init__(daddy,
                        title='Streaming Data Loader',
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
        
        self.fileList = FileListController(self)
        supa_sizer.Add(self.toolbar, 0, wx.EXPAND | wx.ALL, 5)
        supa_sizer.Add(self.fileList, 0, wx.EXPAND | wx.ALL, 5)

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
        self.file_menu.Append(103, '&Save as...', 'Save as...')
        
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
        self.Bind(wx.EVT_MENU, self.onFileExitClick, id=104)
        self.Bind(wx.EVT_MENU, self.onHelpAboutClick, id=201)

    def onFileOpenClick(self, event):
        dlg = wx.FileDialog(self, message='Load Configuration File',
                defaultDir=os.getcwd(), defaultFile='',
                wildcard=WILDCARD,
                style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPaths()
            self.fileList.populateRows(path)
            self.SetStatusText('Configuration File: "' + path[0] + '"', 1)
            self.file_menu.Enable(101, True)
            self.file_menu.Enable(103, True)

        
        dlg.Destroy()
        
        event.Skip()

    def onFileSaveAsClick(self, event):
        dlg = wx.FileDialog(self, message='Save Configuration File',
                defaultDir=os.getcwd(), defaultFile='',
                wildcard=WILDCARD,
                style=wx.SAVE)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.fileList.save(path)
            self.SetStatusText('Configuration File: "' + path + '"', 1)

        dlg.Destroy()
        
        event.Skip()

    def onFileNewClick(self, event):
        self.SetStatusText('Configuration File: [NEW FILE]', 1)
        self.fileList.fileListCtrl.DeleteAllItems()
        
        self.file_menu.Enable(103, False)
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

