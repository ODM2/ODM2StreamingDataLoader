
import wx

from view.clsWizardPanel2 import WizardPanel2View

class WizardPanel2Controller(WizardPanel2View):
    def __init__(self, daddy, **kwargs):
        super(WizardPanel2Controller, self).__init__(daddy, **kwargs)
        self.parent = daddy


if __name__ == '__main__':
    app = wx.App()
    frame = WizardPanel2Controller(None)
    frame.Show()
    app.MainLoop()

