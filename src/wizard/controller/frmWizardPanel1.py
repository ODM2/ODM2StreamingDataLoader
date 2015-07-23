
import wx

from view.clsWizardPanel1 import WizardPanel1View

class WizardPanel1Controller(WizardPanel1View):
    def __init__(self, daddy, **kwargs):
        super(WizardPanel1Controller, self).__init__(daddy, **kwargs)


if __name__ == '__main__':
    app = wx.App()
    frame = WizardPanel1Controller(None)
    frame.Show()
    app.MainLoop()

