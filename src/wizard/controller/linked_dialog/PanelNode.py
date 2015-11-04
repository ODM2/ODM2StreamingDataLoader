
import wx
from src.wizard.view.clsResultPage import ResultPageView
from src.wizard.controller.frmSampFeatSelectPanel \
    import SampFeatSelectPanel
from src.wizard.controller.frmProcLevelSelectPanel \
    import ProcLevelSelectPanel
from src.wizard.controller.frmActionsSelectPanel \
    import ActionsSelectPanel
from src.wizard.controller.frmVariableSelectPanel \
    import VariableSelectPanel
from src.wizard.controller.frmUnitSelectPanel \
    import UnitSelectPanel
class CustomDialog(wx.Dialog):
    def __init__(self, parent, title="",
                 size=wx.DefaultSize,
                 pos=wx.DefaultPosition,
                 style=wx.DEFAULT_DIALOG_STYLE):
        
        pre = wx.PreDialog()
        pre.Create(parent, wx.ID_ANY, title, pos, size, style)
        self.PostCreate(pre)
        
        self.head = CustomDialogPage(parent=self)
        self.head._next = self.head
        self.head._prev = self.head

        self.currentPage = self.head
        
        self.createSizers()
        self.createNavButtons()
        self.addNavButtons()

        #self.topSizer.Add(self.head, 1, wx.ALL|wx.EXPAND, 5)
        self.finalizeLayout()
        
        self.Bind(wx.EVT_LEFT_DOWN, self.onClick)

    def ShowModal(self):
        #self.showPanel(self.currentPage.pnl)
        self.currentPage.pnl.Show()
        #self.sizer.Fit(self)
        super(CustomDialog, self).ShowModal()

    def onClick(self, event):
        event.Skip()

    def insertAfter(self, page, pnl):
        newPage = CustomDialogPage(parent=self,pnl=pnl(self, ''))
        newPage._prev = page
        newPage._next = page._next

        page._next = newPage
        self.topSizer.Add(newPage.pnl)#, 1, wx.ALL|wx.EXPAND, 5)
       
        newPage.pnl.Hide()
        self.sizer.Fit(self)
        #self.hidePanel(newPage.pnl)


    def createPage(self, pnl):
        if self.head.pnl is None:
            self.head.pnl = pnl(self,"")
            self.topSizer.Add(self.head.pnl)#, 1, wx.ALL|wx.EXPAND, 5)
            #self.hidePanel(self.head.pnl)
            self.head.pnl.Hide()
            self.sizer.Fit(self)
        else:    
            lastPage = self.head._prev
            self.insertAfter(lastPage, pnl)

            self.btnNext.SetLabel("Next >") 
            self.btnNext.Unbind(wx.EVT_BUTTON)
            self.btnNext.Bind(wx.EVT_BUTTON, self.onNext)

        #self.sizer.Add(self.head._next, 0, wx.ALL, 5)
    
    def finalizeLayout(self):
        #self.sizer.Add(self.head, 0, wx.ALL, 5)
        self.SetSizer(self.sizer)
        self.Layout()
        self.sizer.Fit(self)
    
    def createSizers(self):
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.topSizer = wx.BoxSizer(wx.VERTICAL)
        self.bottomSizer = wx.BoxSizer(wx.VERTICAL)
        self.btnSizer = wx.BoxSizer(wx.HORIZONTAL)
    
    def createNavButtons(self):
        self.btnCancel = wx.Button(self, wx.ID_CANCEL, "Cancel")
        self.btnNext = wx.Button(self, wx.ID_ANY, "Finish")
        self.btnBack = wx.Button(self, wx.ID_ANY, "< Back")
        self.btnBack.Enable(False)
        self.btnNext.Bind(wx.EVT_BUTTON, self.onFinish)
        self.btnBack.Bind(wx.EVT_BUTTON, self.onPrev)
    
    def addNavButtons(self):
        self.btnSizer.Add(self.btnCancel, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        self.btnSizer.Add(self.btnBack, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        self.btnSizer.Add(self.btnNext, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        self.bottomSizer.Add(self.btnSizer, 0, wx.ALL, 5)
        self.sizer.Add(self.topSizer, 0, wx.ALL, 5)
        self.sizer.Add(self.bottomSizer, 1, wx.ALL|wx.ALIGN_RIGHT, 5)
    
    def showPanel(self, pnl):
        if pnl is not None:
            pnl.Show()
            self.finalizeLayout()
    
    def hidePanel(self, pnl):
        if pnl is not None:
            pnl.Hide()
            self.finalizeLayout()
    
    def onNext(self, event):
        print self.currentPage
        self.hidePanel(self.currentPage.pnl)
        self.showPanel(self.currentPage._next.pnl)
        if self.currentPage._next._next is self.head:
            self.btnNext.SetLabel("Finish")
            self.btnNext.Unbind(wx.EVT_BUTTON)
            self.btnNext.Bind(wx.EVT_BUTTON, self.onFinish)
        if self.currentPage._prev is not None:
            self.btnBack.Enable(True)

        self.currentPage = self.currentPage._next
        event.Skip()
    
    def onPrev(self, event):
        print self.currentPage
        if self.currentPage._prev is not None:
            self.btnBack.Enable(True)

        self.currentPage = self.currentPage._prev
        event.Skip()
    
    def onFinish(self, event):
        self.Close()
        event.Skip()
        

class CustomDialogPage(wx.Panel):
    def __init__(self, parent, pnl=None, _prev=None, _next=None, **kwargs):    
        wx.Panel.__init__(self,parent,id=wx.ID_ANY)
       
        self._next = _next
        self._prev = _prev
        self.pnl = pnl
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        if self.pnl is not None:
            self.sizer.Add(self.pnl, 1, wx.GROW)
        self.SetSizer(self.sizer)
        
        #self.Layout()
        #self.sizer.Fit(self)


if __name__ == '__main__':
    app = wx.App(False)
    wiz = CustomDialog(None, title="Wizard")
    wiz.createPage(SampFeatSelectPanel)
    wiz.createPage(VariableSelectPanel)
    #wiz.createPage(UnitSelectPanel)
    #wiz.createPage(ProcLevelSelectPanel)
    #wiz.createPage(ActionsSelectPanel)
    #wiz.createPage(ResultPageView)
    
    wiz.ShowModal()
    app.MainLoop()
