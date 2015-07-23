
import wx
import wx.wizard as wiz

class WizardView(wiz.Wizard):
    def __init__(self, parent, **kwargs):
        super(WizardView, self).__init__(parent,
            id=wx.ID_ANY, bitmap=wx.NullBitmap,
            pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE,
            **kwargs)

        self.Layout()

    def __del__(self):
        pass

