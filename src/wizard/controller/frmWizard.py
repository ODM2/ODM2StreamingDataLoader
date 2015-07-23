
import wx
import sys

from view.clsWizard import WizardView

class WizardController(WizardView):
    def __init__(self, daddy, title='', **kwargs):
        super(WizardController, self).__init__(daddy, 
                title=title, **kwargs)


if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarController(None)
    frame.Show()
    app.MainLoop()

