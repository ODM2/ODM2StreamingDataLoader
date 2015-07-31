import wx

class VirtualList(wx.ListCtrl):
    def __init__(self, parent, **kwargs):
        super(VirtualList, self).__init__(parent,
            wx.ID_ANY, style=wx.LC_VIRTUAL | wx.LC_REPORT |\
            wx.LC_VRULES | wx.LC_HRULES, **kwargs)
    
        self.data = None

    def setData(self, data):
        self.data = data

    def OnGetItemText(self, item, col):
        return self.data[item]    

