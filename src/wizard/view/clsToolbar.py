
import wx

class ToolbarView(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(ToolbarView, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(0, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.tool_bar = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition,
                            wx.DefaultSize, wx.TB_HORIZONTAL)

        tsize = (24, 24)
       
        new_bmp = scaleBitmap(wx.Bitmap('../media/ic_add_box_black_24dp.png',
                    wx.BITMAP_TYPE_PNG), tsize)
        del_bmp = scaleBitmap(wx.Bitmap('../media/ic_delete_black_24dp.png',
                                wx.BITMAP_TYPE_PNG), tsize)
        edit_bmp = scaleBitmap(wx.Bitmap('../media/ic_mode_edit_black_24dp.png',
                                wx.BITMAP_TYPE_PNG), tsize)
        ref_bmp = scaleBitmap(wx.Bitmap('../media/ic_autorenew_black_24dp.png',
                                wx.BITMAP_TYPE_PNG), tsize)
        run_bmp = scaleBitmap(wx.Bitmap('../media/ic_desktop_mac_black_24dp.png',
                                wx.BITMAP_TYPE_PNG), tsize)

        self.tool_bar.SetToolBitmapSize(tsize) 
        
        self.new_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
                            new_bmp, wx.DefaultPosition,
                            wx.DefaultSize, wx.BU_AUTODRAW)
        self.new_btn.SetToolTipString('New Data File Configuration')
        
        self.del_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
                            del_bmp, wx.DefaultPosition,
                            wx.DefaultSize, wx.BU_AUTODRAW)
        self.del_btn.SetToolTipString('Delete Data File Configuration')
        
        self.edit_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
                            edit_bmp, wx.DefaultPosition,
                            wx.DefaultSize, wx.BU_AUTODRAW)
        self.edit_btn.SetToolTipString('Edit Data File Configuration')
        
        self.ref_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
                            ref_bmp, wx.DefaultPosition,
                            wx.DefaultSize, wx.BU_AUTODRAW)
        self.ref_btn.SetToolTipString('Restart Data File Configuration')
        
        self.run_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
                            run_bmp, wx.DefaultPosition,
                            wx.DefaultSize, wx.BU_AUTODRAW)
        self.run_btn.SetToolTipString('Run Data File Configuration')
        
                
        self.tool_bar.AddControl(self.new_btn)
        self.tool_bar.AddControl(self.del_btn)
        self.tool_bar.AddControl(self.edit_btn)
        self.tool_bar.AddControl(self.ref_btn)
        self.tool_bar.AddControl(self.run_btn)
       
        self.Bind(wx.EVT_BUTTON, self.onNewButtonClick, self.new_btn)
        self.Bind(wx.EVT_BUTTON, self.onDelButtonClick, self.del_btn)
        self.Bind(wx.EVT_BUTTON, self.onEditButtonClick, self.edit_btn)
        self.Bind(wx.EVT_BUTTON, self.onRefButtonClick, self.ref_btn)
        self.Bind(wx.EVT_BUTTON, self.onRunButtonClick, self.run_btn)
        
        self.Bind(wx.EVT_ENTER_WINDOW, self.onNewButtonOver,
            self.new_btn)
        self.Bind(wx.EVT_ENTER_WINDOW, self.onDelButtonOver,
            self.del_btn)
        self.Bind(wx.EVT_ENTER_WINDOW, self.onEditButtonOver,
            self.edit_btn)
        
        self.tool_bar.Realize()

        supa_sizer.Add(self.tool_bar, 0, wx.EXPAND, 5)

        self.SetSizer(supa_sizer)
        self.Layout()

    def __del__(self):
        pass

    def onNewButtonClick(self, event):
        event.Skip()

    def onDelButtonClick(self, event):
        event.Skip()
    
    def onEditButtonClick(self, event):
        event.Skip()
    
    def onRefButtonClick(self, event):
        event.Skip()

    def onRunButtonClick(self, event):
        event.Skip()
    
    def onNewButtonOver(self, event):
        event.Skip()

    def onDelButtonOver(self, event):
        event.Skip()
    
    def onEditButtonOver(self, event):
        event.Skip()


def scaleBitmap(bitmap, size):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(size[0], size[1], wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

