
import wx

class MainView(wx.Frame):
    def __init__(self, parent, **kwargs):
        super(MainView, self).__init__(parent,
                                         id=wx.ID_ANY,
                                         pos=wx.DefaultPosition,
                                         size=(1050,700),
                                         style=wx.DEFAULT_FRAME_STYLE,
                                         **kwargs)

        self.SetSizeHintsSz(wx.Size(1050, 700), wx.DefaultSize)
        self.Centre(wx.BOTH)

    def __del__(self):
        pass
    
