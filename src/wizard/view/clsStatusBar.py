import wx

class StatusBarView(wx.StatusBar):
    def __init__(self, parent):
        super(StatusBarView, self).__init__(parent)

        self.SetFieldsCount(2)
        self.SetStatusWidths([-1, -1])

        self.SetStatusText('', 1)
        self.SetStatusText('File: [NEW FILE]', 0)

    def __del__(self):
        pass
