
import wx
import os

class ToolbarView(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(ToolbarView, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(0, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #self.tool_bar = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition,
        #                    wx.DefaultSize)

        tsize = (30, 30)
        path = os.path.dirname(\
            os.path.dirname(os.path.realpath(__file__)))
        new_bmp = scaleBitmap(wx.Bitmap(\
            path + '/media/blue_add.png',\
            wx.BITMAP_TYPE_PNG), tsize)
        del_bmp = scaleBitmap(wx.Bitmap(\
            path + '/media/blue_remove.png',\
            wx.BITMAP_TYPE_PNG), tsize)
        edit_bmp = scaleBitmap(wx.Bitmap(\
            path + '/media/blue_edit.png',\
            wx.BITMAP_TYPE_PNG), tsize)
        #ref_bmp = scaleBitmap(wx.Bitmap(\
        #    path + '//media/ic_autorenew_black_24dp.png',\
        #    wx.BITMAP_TYPE_PNG), tsize)
        run_bmp = scaleBitmap(wx.Bitmap(\
            path + '//media/blue_run.png',\
            wx.BITMAP_TYPE_PNG), tsize)

        #self.tool_bar.SetToolBitmapSize(tsize) 
        
        #self.new_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
        #                    new_bmp, wx.DefaultPosition,
        #                    wx.DefaultSize, wx.BU_AUTODRAW)
        #self.new_btn.SetToolTipString('New Data File Configuration')
        
        #self.del_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
        #                    del_bmp, wx.DefaultPosition,
        #                    wx.DefaultSize, wx.BU_AUTODRAW)
        #self.del_btn.SetToolTipString('Delete Data File Configuration')
        
        #self.edit_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
        #                    edit_bmp, wx.DefaultPosition,
        #                    wx.DefaultSize, wx.BU_AUTODRAW)
        #self.edit_btn.SetToolTipString('Edit Data File Configuration')
        
        #self.ref_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
        #                    ref_bmp, wx.DefaultPosition,
        #                    wx.DefaultSize, wx.BU_AUTODRAW)
        #self.ref_btn.SetToolTipString('Restart Data File Configuration')
        
        #self.run_btn = wx.BitmapButton(self.tool_bar, wx.ID_ANY,
        #                    run_bmp, wx.DefaultPosition,
        #                    wx.DefaultSize, wx.BU_AUTODRAW)
        #self.run_btn.SetToolTipString('Run Data File Configuration')
        
        parent.tb.AddLabelTool(10, 'New Data File Configuration', new_bmp)       
        parent.tb.AddLabelTool(20, 'Delete Data File Configuration', del_bmp)       
        parent.tb.AddLabelTool(30, 'Edit Data File Configuration', edit_bmp)       
        parent.tb.AddLabelTool(40, 'Run Data File Configuration', run_bmp)       
        #self.tool_bar.AddControl(self.new_btn)
        #self.tool_bar.AddControl(self.del_btn)
        #self.tool_bar.AddControl(self.edit_btn)
        #self.tool_bar.AddControl(self.ref_btn)
        #self.tool_bar.AddControl(self.run_btn)
       
        parent.tb.Bind(wx.EVT_TOOL, self.onNewButtonClick, id=10)
        parent.tb.Bind(wx.EVT_TOOL, self.onDelButtonClick, id=20)
        parent.tb.Bind(wx.EVT_TOOL, self.onEditButtonClick, id=30)
        parent.tb.Bind(wx.EVT_TOOL, self.onRunButtonClick, id=40)
        parent.tb.EnableTool(10, not parent.tb.GetToolEnabled(10)) 
        #self.Bind(wx.EVT_ENTER_WINDOW, self.onNewButtonOver,
        #    self.new_btn)
        #self.Bind(wx.EVT_ENTER_WINDOW, self.onDelButtonOver,
        #    self.del_btn)
        #self.Bind(wx.EVT_ENTER_WINDOW, self.onEditButtonOver,
        #    self.edit_btn)
        parent.tb.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENUBAR)) 
        parent.tb.Realize()

        #supa_sizer.Add(self.tool_bar, 0, wx.EXPAND, 5)

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

