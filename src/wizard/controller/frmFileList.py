
import wx

from view.clsFileList import FileListView
from models.YamlConfiguration import YamlConfiguration


class FileListController(FileListView):
    def __init__(self, daddy, **kwargs):
        super(FileListController, self).__init__(daddy, **kwargs)
        
        self.populateRows()

    def populateRows(self):
        yamlConfig = YamlConfiguration('/home/denver/test2.yaml')
        print yamlConfiguration.GetAttributeDict('DataRowPosition')

if __name__ == '__main__':
    app = wx.App()
    frame = FileListController(None)
    frame.Show()
    app.MainLoop()

