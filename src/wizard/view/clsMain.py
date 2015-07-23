
import wx

class MainView(wx.Frame):
    def __init__(self, parent, **kwargs):
        super(MainView, self).__init__(parent,
                                         id=wx.ID_ANY,
                                         pos=wx.DefaultPosition,
                                         size=(1080,700),
                                         style=wx.DEFAULT_FRAME_STYLE,
                                         **kwargs)

        self.SetSizeHintsSz(wx.Size(1080, 700), wx.DefaultSize)
        self.Centre(wx.BOTH)

    def __del__(self):
        pass
    
    def onFileOpenClick(self, event):    
        event.Skip()
    def onFileNewClick(self, event):    
        event.Skip()
    def onFileExitClick(self, event):    
        event.Skip()
    def onHelpAboutClick(self, event):    
        event.Skip()
