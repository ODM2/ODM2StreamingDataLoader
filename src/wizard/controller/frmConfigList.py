
import wx

from view.clsConfigList import ConfigListView
from view.clsConfigListPanel import ConfigListPanelView

class ConfigListController(ConfigListView):
    def __init__(self, daddy, **kwargs):
        super(ConfigListController, self).__init__(daddy,
                        title='Streaming Data Loader',
                        **kwargs)
        
        supa_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        #self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
        #                wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panel = ConfigListPanelView(self)
        supa_sizer.Add(self.panel, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(supa_sizer)
        self.Layout()
        self.Centre(wx.BOTH)

if __name__ == '__main__':
    app = wx.App()
    frame = ConfigListController(None)
    frame.Show()
    app.MainLoop()

