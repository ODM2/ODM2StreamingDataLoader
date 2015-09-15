
import wx

from src.wizard.controller.frmFileConfigPanel import FileConfigPanelController
from src.wizard.controller.frmDataConfigPanel import DataConfigPanelController
from src.wizard.controller.frmDBConfig import pnlDBConfig

class ChainedDialog(wx.Dialog):
    def __init__(self, data={}, *args, **kwargs):
        super(ChainedDialog, self).__init__(*args, **kwargs)
        
        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.panelSizer = wx.BoxSizer(wx.VERTICAL)
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.panelList = []
        self.currentPanel = 0
        self.data = data

        self.setPanels()
        
        # Add the buttons, which will appear on each page.
        self.cancelButton = wx.Button(self, label="Cancel")
        self.cancelButton.Bind(wx.EVT_BUTTON, self.onClose)
        buttonSizer.Add(self.cancelButton, 0,
            wx.ALL| wx.EXPAND | wx.ALIGN_RIGHT, 5)
        
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
        self.prevButton.Enable(False)
        self.panelList[self.currentPanel].Show()
        self.mainSizer.Fit(self)

        self.currentPanel = 0

        self.panelList[self.currentPanel].populate(data=self.data)

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

    def run(self):
        if (self.ShowModal()):
            return self.data
        return None

    def buttonCheck(self):
        if self.currentPanel == len(self.panelList)-1:
            self.nextButton.SetLabel("Finish")
            #self.nextButton.Bind(wx.EVT_BUTTON, self.onClose)
        else:
            self.panelList[self.currentPanel+1]
            self.nextButton.SetLabel("Next >")

        if self.currentPanel == 0:
            self.prevButton.Enable(False)
        else: 
            self.prevButton.Enable(True)
            
    def onClose(self, event):
        self.EndModal(-1)

    def onPrev(self, event):
        if self.currentPanel-1 >= 0:
            self.panelList[self.currentPanel].Hide()
            self.panelList[self.currentPanel-1].Show()
            self.currentPanel -= 1
            self.mainSizer.Fit(self)
            self.buttonCheck()
        event.Skip()

    def onNext(self, event):
        # OK to move to the next panel.
        if self.currentPanel+1 <= len(self.panelList)-1:
            if not self.panelList[self.currentPanel].Validate():
                event.Skip()
                return
            try:
                self.panelList[self.currentPanel+1].populate(data=self.panelList[self.currentPanel].getInput())
            except TypeError:
                error_dlg = wx.MessageBox('This data does not look valid. Check to see if the configuration options match the data file.\n\nDo you want to continue anyway?', 'Data Load Error', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                if error_dlg == wx.ID_NO:
                    event.Skip()
                    return

            self.panelList[self.currentPanel].Hide()
            self.panelList[self.currentPanel+1].Show()
            self.currentPanel += 1
            self.mainSizer.Fit(self)
            self.buttonCheck()
        else: 
            for panel in self.panelList:
                self.data.update(panel.getInput())
            self.EndModal(1)
            print "end"

        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    myWizard = ChainedDialog(parent=None, title="Wizard",
                             size=wx.DefaultSize,
                             style=wx.DEFAULT_DIALOG_STYLE)
    myWizard.Show()
    app.MainLoop()
