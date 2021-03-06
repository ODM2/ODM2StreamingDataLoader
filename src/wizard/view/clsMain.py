import os
import wx
from ..media.images import blue_add, blue_remove, blue_edit, blue_run

class MainView(wx.Frame):
    def __init__(self, parent, **kwargs):
        super(MainView, self).__init__(parent,
                                         id=wx.ID_ANY,
                                         pos=wx.DefaultPosition,
                                         size=(1080,700),
                                         style=wx.DEFAULT_FRAME_STYLE,
                                         **kwargs)

        self.tb = self.CreateToolBar()


        #tsize = (30, 30)
        # path = os.path.dirname(\
        #     os.path.dirname(os.path.realpath(__file__)))
        # new_bmp = scaleBitmap(wx.Bitmap(\
        #     path + '/media/blue_add.png',\
        #     wx.BITMAP_TYPE_PNG), tsize)
        # del_bmp = scaleBitmap(wx.Bitmap(\
        #     path + '/media/blue_remove.png',\
        #     wx.BITMAP_TYPE_PNG), tsize)
        # edit_bmp = scaleBitmap(wx.Bitmap(\
        #     path + '/media/blue_edit.png',\
        #     wx.BITMAP_TYPE_PNG), tsize)
        # #ref_bmp = scaleBitmap(wx.Bitmap(\
        # #    path + '//media/ic_autorenew_black_24dp.png',\
        # #    wx.BITMAP_TYPE_PNG), tsize)
        # run_bmp = scaleBitmap(wx.Bitmap(\
        #     path + '//media/blue_run.png',\
        #     wx.BITMAP_TYPE_PNG), tsize)
        new_bmp= blue_add.GetImage().Rescale(30, 30).ConvertToBitmap()#.getBitmap()
        del_bmp=blue_remove.GetImage().Rescale(30, 30).ConvertToBitmap()#.getBitmap()
        edit_bmp= blue_edit.GetImage().Rescale(30, 30).ConvertToBitmap()#.getBitmap()
        run_bmp= blue_run.GetImage().Rescale(30, 30).ConvertToBitmap()#.getBitmap()


        self.tb.AddLabelTool(id=10, label="New",
            bitmap=new_bmp, longHelp='Create a new mapping.')      
        self.tb.AddLabelTool(id=20, label='Delete',
            bitmap=del_bmp, longHelp='Delete selected mapping.')
        self.tb.AddLabelTool(id=30, label='Edit',
            bitmap=edit_bmp, longHelp='Edit selected mapping.')
        self.tb.AddLabelTool(id=40, label='Run',
            bitmap=run_bmp, longHelp='Run Data File Configuration.')

        self.tb.Bind(wx.EVT_TOOL, self.onNewButtonClick, id=10)
        self.tb.Bind(wx.EVT_TOOL, self.onDelButtonClick, id=20)
        self.tb.Bind(wx.EVT_TOOL, self.onEditButtonClick, id=30)
        self.tb.Bind(wx.EVT_TOOL, self.onRunButtonClick, id=40)

        self.tb.EnableTool(20, False)
        self.tb.EnableTool(30, False)
        self.tb.EnableTool(40, False)

        self.tb.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENUBAR))
        self.tb.Realize()

        self.SetSizeHintsSz(wx.Size(1080, 700), wx.DefaultSize)
        self.Centre(wx.BOTH)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENUBAR))
    def __del__(self):
        pass
    
    def onFileOpenClick(self, event):    
        event.Skip()

    def onFileNewClick(self, event):    
        event.Skip()

    def onFileSaveAsClick(self, event):    
        event.Skip()

    def onFileExitClick(self, event):    
        event.Skip()

    def onHelpAboutClick(self, event):    
        event.Skip()

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
