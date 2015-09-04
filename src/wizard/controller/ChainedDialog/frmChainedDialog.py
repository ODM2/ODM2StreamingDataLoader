
import wx

from controller.frmFileConfigPanel import FileConfigPanelController
from controller.frmDataConfigPanel import DataConfigPanelController
from controller.frmDBConfig import pnlDBConfig

class ChainedDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(ChainedDialog, self).__init__(*args, **kwargs)
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.panelSizer = wx.BoxSizer(wx.VERTICAL)
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.panelList = []
        self.currentPanel = 0
        self.setPanels()
        
        # Add the buttons, which will appear on each page.
        self.prevButton = wx.Button(self, label="< Back")
        self.prevButton.Bind(wx.EVT_BUTTON, self.onPrev)
        buttonSizer.Add(self.prevButton, 0,
            wx.ALL| wx.EXPAND | wx.ALIGN_RIGHT, 5)
        
        self.nextButton = wx.Button(self, label="Next >")
        self.nextButton.Bind(wx.EVT_BUTTON, self.onNext)
        buttonSizer.Add(self.nextButton, 0,
            wx.ALL| wx.EXPAND | wx.ALIGN_RIGHT, 5)

        # Add the buttons and sizers to the main sizer.
        self.mainSizer.Add(self.panelSizer, 1, wx.EXPAND)
        self.mainSizer.Add(buttonSizer, 0, wx.ALIGN_RIGHT)
        self.SetSizer(self.mainSizer)
        
        # Show/start the dialog.
        self.showDialog()

    def setPanels(self):
        filePanel = FileConfigPanelController(self)
        dataPanel = DataConfigPanelController(self)
        dbPanel = pnlDBConfig(self, None)

        self.panelSizer.Add(filePanel)
        self.panelSizer.Add(dataPanel)
        self.panelSizer.Add(dbPanel)
        
        filePanel.Hide()
        dataPanel.Hide()
        dbPanel.Hide()

        self.panelList.append(dbPanel)
        self.panelList.append(filePanel)
        self.panelList.append(dataPanel)
        

    def showDialog(self):
        
        self.prevButton.Enable(False)
        self.panelList[self.currentPanel].Show()
        self.mainSizer.Fit(self)
        self.Show(True)
        self.currentPanel = 0

    def buttonCheck(self):
        try:
            self.panelList[self.currentPanel+1]
            self.nextButton.SetLabel("Next >")
        except IndexError:
            self.nextButton.SetLabel("Finish")
        try:
            self.panelList[self.currentPanel-2]
            self.prevButton.Enable(True)
        except IndexError:
            self.prevButton.Enable(False)
            


    def onPrev(self, event):
        print self.currentPanel
        if self.currentPanel-1 >= 0:
            self.panelList[self.currentPanel].Hide()
            self.panelList[self.currentPanel-1].Show()
            self.currentPanel -= 1
            self.mainSizer.Fit(self)
            self.buttonCheck()
        else: 
            print "beginning"
            event.Skip()

    def onNext(self, event):
        print self.currentPanel
        if self.currentPanel+1 < len(self.panelList):
            self.panelList[self.currentPanel].Hide()
            self.panelList[self.currentPanel+1].Show()
            self.currentPanel += 1
            self.mainSizer.Fit(self)
            self.buttonCheck()
        else: 
            print "end"
            event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    myWizard = ChainedDialog(parent=None, title="Wizard",
                             size=wx.DefaultSize,
                             style=wx.DEFAULT_DIALOG_STYLE)
    myWizard.Show()
    app.MainLoop()
