
import wx

from view.clsWizardPage1 import WizardPage1View
from controller.frmWizardPanel1 import WizardPanel1Controller

class WizardPage1Controller(WizardPage1View):
    def __init__(self, daddy, **kwargs):
        super(WizardPage1Controller, self).__init__(daddy, **kwargs)


        supa_sizer = wx.FlexGridSizer(0, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        panel = WizardPanel1Controller(self)

        supa_sizer.Add(panel, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(supa_sizer)
        self.Layout() 

if __name__ == '__main__':
    app = wx.App()
    frame = WizardPage1Controller(None)
    frame.Show()
    app.MainLoop()

