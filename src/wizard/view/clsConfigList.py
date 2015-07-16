
import wx

class ConfigListView(wx.Frame):
    def __init__(self, parent, **kwargs):
        super(ConfigListView, self).__init__(parent,
                                         id=wx.ID_ANY,
                                         pos=wx.DefaultPosition,
                                         size=(1000,700),
                                         style=wx.DEFAULT_FRAME_STYLE,
                                         **kwargs)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
    
