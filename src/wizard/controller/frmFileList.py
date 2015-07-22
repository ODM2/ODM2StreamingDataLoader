
import wx

from view.clsFileList import FileListView

class FileListController(FileListView):
    def __init__(self, daddy, **kwargs):
        super(FileListController, self).__init__(daddy, **kwargs)


if __name__ == '__main__':
    app = wx.App()
    frame = FileListController(None)
    frame.Show()
    app.MainLoop()

