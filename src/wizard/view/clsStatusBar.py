import wx

class StatusBarView(wx.StatusBar):
    def __init__(self, parent):
        super(StatusBarView, self).__init__(parent)

        self.SetFieldsCount(2)
        self.SetStatusWidths([-1, -1])

        self.SetStatusText('', 0)
        self.SetStatusText('Configuration File: [NEW FILE]', 1)

    def __del__(self):
        pass
