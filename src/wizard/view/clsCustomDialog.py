import wx

class CustomDialog(wx.Dialog):
    def __init__(self, parent, title,
                 size=wx.DefaultSize,
                 pos=wx.DefaultPosition,
                 style=wx.DEFAULT_DIALOG_STYLE):
        
        pre = wx.PreDialog()
        pre.Create(parent, wx.ID_ANY, title, pos, size, style)
        self.PostCreate(pre)
        # Outermost sizer.
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        self.Layout()
        self.sizer.Fit(self)

    def addPanel(self, pnl):
        self.sizer.Add(pnl, 1, wx.ALL|wx.EXPAND, 5)
        self.sizer.Layout()
        self.sizer.Fit(self)

