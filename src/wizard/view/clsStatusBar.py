import wx

class StatusBarView(wx.StatusBar):
    def __init__(self, parent):
        super(StatusBarView, self).__init__(parent)

        self.SetFieldsCount(1)
        self.SetStatusWidths([-1])

        self.SetStatusText('File: <NEW FILE>', 0)

    def __del__(self):
        pass
