
import wx
import wx.wizard as wiz
import sys

from view.clsWizardPage import WizardPageView

class WizardPageController(WizardPageView):
    def __init__(self, daddy, **kwargs):
        super(WizardPageController, self).__init__(daddy, **kwargs)


if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarController(None)
    frame.Show()
    app.MainLoop()

