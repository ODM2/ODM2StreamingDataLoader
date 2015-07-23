
import wx

class WizardPageView(wx.wizard.WizardPageSimple):
    def __init__(self, parent, **kwargs):
        super(WizardPageView, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(0, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)


        self.SetSizer(supa_sizer)
        self.Layout()

    def __del__(self):
        pass

