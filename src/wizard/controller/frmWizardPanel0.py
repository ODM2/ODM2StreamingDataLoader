
import wx

from view.clsWizardPanel0 import WizardPanel0View

class WizardPanel0Controller(WizardPanel0View):
    def __init__(self, daddy, **kwargs):
        super(WizardPanel0Controller, self).__init__(daddy, **kwargs)
        self.parent = daddy


if __name__ == '__main__':
    app = wx.App()
    frame = WizardPanel0Controller(None)
    frame.Show()
    app.MainLoop()

