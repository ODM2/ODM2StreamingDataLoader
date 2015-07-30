
import wx

from view.clsWizardPage2 import WizardPage2View
from controller.frmWizardPanel2 import WizardPanel2Controller

class WizardPage2Controller(WizardPage2View):
    def __init__(self, daddy, **kwargs):
        super(WizardPage2Controller, self).__init__(daddy, **kwargs)


        supa_sizer = wx.FlexGridSizer(0, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        panel = WizardPanel2Controller(self)

        supa_sizer.Add(panel, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(supa_sizer)
        self.Layout() 

if __name__ == '__main__':
    app = wx.App()
    frame = WizardPage2Controller(None)
    frame.Show()
    app.MainLoop()

