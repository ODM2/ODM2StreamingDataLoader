
import wx

from view.clsWizardPage0 import WizardPage0View
from controller.frmWizardPanel0 import WizardPanel0Controller

class WizardPage0Controller(WizardPage0View):
    def __init__(self, daddy, **kwargs):
        super(WizardPage0Controller, self).__init__(daddy, **kwargs)


        supa_sizer = wx.FlexGridSizer(0, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        panel = WizardPanel0Controller(self)

        supa_sizer.Add(panel, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(supa_sizer)
        self.Layout() 

if __name__ == '__main__':
    app = wx.App()
    frame = WizardPage0Controller(None)
    frame.Show()
    app.MainLoop()

