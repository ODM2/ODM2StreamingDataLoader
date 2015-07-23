
import wx
import os

from view.clsMain import MainView

from controller.frmToolbar import ToolbarController
from controller.frmFileList import FileListController

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
        self.file_menu.Append(101, '&New Configuration File...')
        self.file_menu.Append(102, '&Load Configuration File...')
        self.file_menu.AppendSeparator()
        self.file_menu.Append(103, '&Exit')

        self.menu_bar.Append(self.file_menu, '&File')
        
        self.help_menu = wx.Menu()
        self.help_menu.Append(201, '&About')

        self.menu_bar.Append(self.help_menu, '&Help')

        self.SetMenuBar(self.menu_bar)

        self.Bind(wx.EVT_MENU, self.onFileOpenClick, id=102)
        self.Bind(wx.EVT_MENU, self.onFileNewClick, id=101)
        self.Bind(wx.EVT_MENU, self.onFileExitClick, id=103)
        self.Bind(wx.EVT_MENU, self.onHelpAboutClick, id=201)

    def onFileOpenClick(self, event):
        dlg = wx.FileDialog(self, message='Load Configuration File',
                defaultDir=os.getcwd(), defaultFile='',
                wildcard=WILDCARD,
                style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print paths
        
        dlg.Destroy()
        
        event.Skip()

    def onFileNewClick(self, event):
        event.Skip()
        
    def onFileExitClick(self, event):
        event.Skip()

    def onHelpAboutClick(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame = MainController(None)
    frame.Show()
    app.MainLoop()

