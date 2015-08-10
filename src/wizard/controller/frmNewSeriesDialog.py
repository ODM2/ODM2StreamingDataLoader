import wx


class NewSeriesDialog(wx.Dialog):
    def __init__(self, parent, title, **kwargs):
        super(NewSeriesDialog, self).__init__(parent, id=-1,
            title=title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE, **kwargs)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        self.Layout()

    
    def addPanel(self, panel):
        self.sizer.Add(panel, 0, wx.ALL, 5)
        self.sizer.Layout()
        self.sizer.Fit(self)
