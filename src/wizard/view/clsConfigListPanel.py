
import wx

class ConfigListPanelView(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(ConfigListPanelView, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(0, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.tool_bar = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition,
                            wx.DefaultSize, wx.TB_HORIZONTAL)

        tsize = (34, 34)
        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW,
                        wx.ART_TOOLBAR, tsize)
        del_bmp = wx.ArtProvider.GetBitmap(wx.ART_DELETE,
                        wx.ART_TOOLBAR, tsize)
        edit_bmp = wx.ArtProvider.GetBitmap(wx.ART_REPORT_VIEW,
                        wx.ART_TOOLBAR, tsize)
        
        self.tool_bar.SetToolBitmapSize(tsize) 
        
        self.new_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
                            new_bmp, wx.DefaultPosition,
                            wx.DefaultSize, wx.BU_AUTODRAW)
        
        self.del_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
                            del_bmp, wx.DefaultPosition,
                            wx.DefaultSize, wx.BU_AUTODRAW)
        
        self.edit_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
                            edit_bmp, wx.DefaultPosition,
                            wx.DefaultSize, wx.BU_AUTODRAW)
        
        
        self.tool_bar.AddControl(self.new_btn)
        self.tool_bar.AddControl(self.del_btn)
        self.tool_bar.AddControl(self.edit_btn)
        
        self.tool_bar.Realize()

        supa_sizer.Add(self.tool_bar, 0, wx.EXPAND, 5)

        self.SetSizer(supa_sizer)
        self.Layout()

    def __del__(self):
        pass
