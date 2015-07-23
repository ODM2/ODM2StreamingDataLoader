
import wx

from view.clsWizardPage1 import WizardPage1View

class WizardPage1Controller(WizardPage1View):
    def __init__(self, daddy, **kwargs):
        super(WizardPage1Controller, self).__init__(daddy, **kwargs)


if __name__ == '__main__':
    app = wx.App()
    frame = WizardPage1Controller(None)
    frame.Show()
    app.MainLoop()

