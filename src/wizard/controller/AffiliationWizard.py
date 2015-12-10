import wx

class AffiliationWizard(wx.Dialog):
    def __init__(self, parent, database=None, title="Create new affiliation",
                 size=wx.DefaultSize,
                 pos=wx.DefaultPosition,
                 style=wx.DEFAULT_DIALOG_STYLE):
        
        pre = wx.PreDialog()
        pre.Create(parent, wx.ID_ANY, title, pos, size, style)
        self.PostCreate(pre)
        
        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.pnlSizer = wx.BoxSizer(wx.VERTICAL)
        self.btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.pnlList = []
        self.currentPnl = None;
        self.database = database

        self.addButtons()

        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)

        self.returnValue = wx.ID_ANY

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
        self.btnNext.Enable(False)
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
        data = {}
        for p in self.pnlList:
            data.update(p.getData())
        return data

    def ShowModal(self):
        if self.pnlList:
            self.currentPnl = self.pnlList[0]
            self.currentPnl.Show()
        self.mainSizer.Fit(self)
        super(AffiliationWizard, self).ShowModal()
        return self.returnValue

    # ********************** #
    # *** Event Handlers *** #
    # ********************** #

    def onFinish(self, event):
        if self.currentPnl.Validate():
            self.result = self.pnlList[-1].createAffiliation()
            if self.result:
                self.returnValue = wx.ID_OK
                self.Close()
        else:
            self.currentPnl.Refresh()
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
        if self.currentPnl.Validate():
            self.btnNext.Enable(False)
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
        else:
            self.currentPnl.Refresh()
        event.Skip() 

