import wx

class VirtualList(wx.ListCtrl):
    def __init__(self, parent, **kwargs):
        super(VirtualList, self).__init__(parent,
            wx.ID_ANY, style=wx.LC_VIRTUAL | wx.LC_REPORT |\
            wx.LC_VRULES | wx.LC_HRULES, **kwargs)
    
        self.data = None
        self.columns = []

    def setData(self, data):
        self.data = data
        print data

    def RefreshAllItems(self):
        if self.data:
            if self.DeleteAllItems():
                if self.DeleteAllColumns():
                    self.SetItemCount(len(self.data))
                    self.RefreshItems(0, len(self.data) - 1)
                    return True
        return False

    def OnGetItemText(self, item, col):
        return self.data[item][col]
    
    def InsertColumns(self, columnList):
        self.columns = columnList
        
        for column in columnList:
            super(VirtualList, self).InsertColumn(\
                columnList.index(column), column)

    def getColumnText(self, index):
        return self.columns[index]
