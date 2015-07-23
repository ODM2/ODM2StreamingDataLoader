
import wx

from view.clsWizardPanel1 import WizardPanel1View

class WizardPage1View(wx.wizard.WizardPageSimple):
    def __init__(self, parent, **kwargs):
        super(WizardPage1View, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(0, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        panel = WizardPanel1View(self)

        supa_sizer.Add(panel, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(supa_sizer)
        self.Layout()

    def __del__(self):
        pass

