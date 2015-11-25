import wx
from src.wizard.controller.frmSampFeatSelectPanel \
    import SampFeatSelectPanel
from src.wizard.controller.frmVariableSelectPanel \
    import VariableSelectPanel
from src.wizard.controller.frmUnitSelectPanel \
    import UnitSelectPanel
from src.wizard.controller.frmProcLevelSelectPanel \
    import ProcLevelSelectPanel
from src.wizard.controller.frmActionsSelectPanel \
    import ActionsSelectPanel
from src.wizard.view.clsResultPage import ResultPageView

class WizardDialog(wx.Dialog):
    def __init__(self, parent, database=None, title="Wizard Dialog",
                 size=wx.DefaultSize,
                 pos=wx.DefaultPosition,
                 style=wx.DEFAULT_DIALOG_STYLE):

        pre = wx.PreDialog()
        pre.Create(parent, wx.ID_ANY, title, pos, size, style)
        self.PostCreate(pre)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.pnlSizer = wx.BoxSizer(wx.VERTICAL)
        self.btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.pnlList = []
        self.currentPnl = None;
        self.database = database

        self.addButtons()

        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)

    def addButtons(self):
        self.btnCancel = wx.Button(self, wx.ID_CANCEL, "Cancel")
        self.btnNext = wx.Button(self, wx.ID_ANY, "Finish")
        self.btnPrev = wx.Button(self, wx.ID_ANY, "< Back")

        self.btnSizer.Add(self.btnCancel, 0, 
                          wx.ALL|wx.ALIGN_RIGHT, 5)
        self.btnSizer.Add(self.btnPrev, 0, 
                          wx.ALL|wx.ALIGN_RIGHT, 5)
        self.btnSizer.Add(self.btnNext, 0, 
                          wx.ALL|wx.ALIGN_RIGHT, 5)

        self.mainSizer.Add(self.pnlSizer, 1, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(self.btnSizer, 0, wx.ALL|wx.ALIGN_RIGHT, 5)

        self.btnPrev.Enable(False)
        self.btnNext.Bind(wx.EVT_BUTTON, self.onFinish)
        self.btnPrev.Bind(wx.EVT_BUTTON, self.onPrev)
    
    def addPage(self, pnl):
        newPnl = pnl(self)
        newPnl.Hide()
        self.pnlList.append(newPnl)
        self.pnlSizer.Add(newPnl, 1, wx.ALL|wx.EXPAND, 5)

        if len(self.pnlList) == 1:
            self.btnNext.Unbind(wx.EVT_BUTTON)
            self.btnNext.SetLabel("Next >")
            self.btnNext.Bind(wx.EVT_BUTTON, self.onNext)
    
    def getSelections(self):
        data = []
        for pnl in self.pnlList:
            try:
                data.append(pnl.list_ctrl.GetSelectedObject())
            except AttributeError:
                continue
        return data

    def ShowModal(self):
        if self.pnlList:
            self.currentPnl = self.pnlList[0]
            self.currentPnl.Show()
        self.mainSizer.Fit(self)
        super(WizardDialog, self).ShowModal()

    # ********************** #
    # *** Event Handlers *** #
    # ********************** #

    def onFinish(self, event):
        self.Close()
        event.Skip()

    def onPrev(self, event):
        self.currentPnl.Hide()
        self.currentPnl = self.pnlList[self.pnlList.index( \
            self.currentPnl)-1]
        self.currentPnl.Show()
        self.Layout()
        self.mainSizer.Fit(self)
        
        if self.currentPnl == self.pnlList[0]:
            self.btnPrev.Enable(False)
        else:
            self.btnPrev.Enable(True)
        if self.currentPnl == self.pnlList[-1]:
            self.btnNext.SetLabel("Finish")
            self.btnNext.Unbind(wx.EVT_BUTTON)
            self.btnNext.Bind(wx.EVT_BUTTON, self.onFinish)
        else:
            self.btnNext.SetLabel("Next >")
            self.btnNext.Unbind(wx.EVT_BUTTON)
            self.btnNext.Bind(wx.EVT_BUTTON, self.onNext)
        
        
        event.Skip()

    def onNext(self, event):
        self.currentPnl.Hide()
        self.currentPnl = self.pnlList[self.pnlList.index( \
            self.currentPnl)+1]
        self.currentPnl.Show()
        self.Layout()
        self.mainSizer.Fit(self)
        
        if self.currentPnl == self.pnlList[0]:
            self.btnPrev.Enable(False)
        else:
            self.btnPrev.Enable(True)
        if self.currentPnl == self.pnlList[-1]:
            self.btnNext.SetLabel("Finish")
            self.btnNext.Unbind(wx.EVT_BUTTON)
            self.btnNext.Bind(wx.EVT_BUTTON, self.onFinish)
        else:
            self.btnNext.SetLabel("Next >")
            self.btnNext.Unbind(wx.EVT_BUTTON)
            self.btnNext.Bind(wx.EVT_BUTTON, self.onNext)
            
        
        event.Skip() 


if __name__ == '__main__': 
    app = wx.App(False) 
    wiz = WizardDialog(None) 
    wiz.addPage(SampFeatSelectPanel) 
    wiz.addPage(VariableSelectPanel) 
    wiz.addPage(UnitSelectPanel) 
    wiz.addPage(ProcLevelSelectPanel) 
    wiz.addPage(ActionsSelectPanel) 
    wiz.addPage(ResultPageView)   
    wiz.ShowModal() 
    app.MainLoop() 

