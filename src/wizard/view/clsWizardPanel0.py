
import wx
import wx.lib.masked as masked
import operator

from controller.frmDBConfig import pnlDBConfig

class WizardPanel0View(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(WizardPanel0View, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(1, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        
        self.database_panel = pnlDBConfig(self, None)
        
        database_flex_sizer = wx.FlexGridSizer(1, 1, 0, 0)
        database_flex_sizer.SetFlexibleDirection(wx.BOTH)
        database_flex_sizer.SetNonFlexibleGrowMode(\
            wx.FLEX_GROWMODE_SPECIFIED)

        database_flex_sizer.Add(self.database_panel, 0,
            wx.ALL, 5)

        supa_sizer.Add(database_flex_sizer, 1, wx.EXPAND, 5)
        
        
        self.SetSizer(supa_sizer)
        self.Layout()

    def __del__(self):
        pass

