
import wx
import sys

from view.clsToolbar import ToolbarView

class ToolbarController(ToolbarView):
    def __init__(self, daddy, **kwargs):
        super(ToolbarController, self).__init__(daddy, **kwargs)

    def OnNewButtonClick(self, event):
        print sys.path
        event.Skip()
    
    def OnDelButtonClick(self, event):
        print 'delete'
        event.Skip()
    
    def OnEditButtonClick(self, event):
        print 'edit'
        event.Skip()
    
    def OnRefButtonClick(self, event):
        print 'refresh'
        event.Skip()

    def OnRunButtonClick(self, event):
        print 'run'
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = ToolbarController(None)
    frame.Show()
    app.MainLoop()

