
import wx

from view.clsFileList import FileListView
from models.YamlConfiguration import YamlConfiguration


class FileListController(FileListView):
    def __init__(self, daddy, **kwargs):
        super(FileListController, self).__init__(daddy, **kwargs)

    def populateRows(self, paths):
        # Clear the previous data from the list.
        self.fileListCtrl.DeleteAllItems()
        
        for path in paths:
            yamlConfig = YamlConfiguration(path)

            # Append the list control each configuration block in the 
            # YAML file.
            for file_block in reversed(yamlConfig.get()):
                database_name = u'%s' % (file_block[1]\
                    ['Database']['DatabaseName'])
                database_server = u'%s' % (file_block[1]\
                    ['Database']['Address']) 
                id = file_block[0]
                file_path = u'%s' % (file_block[1]\
                    ['Settings']['FileLocation'])
                last_update = u'%s' % (file_block[1]\
                    ['Schedule']['LastUpdate'])
                begin_date = u'%s' % (file_block[1]\
                    ['Schedule']['Beginning'])
                period = u'%s' % (file_block[1]\
                    ['Schedule']['Frequency'])

                data = [id, database_server, database_name, file_path,
                    period, begin_date, last_update]
                
                print data
                self.fileListCtrl.Append(data)

        # Adjust the width of the list columns. 
        for column_index in range(self.fileListCtrl.GetColumnCount()):
            self.fileListCtrl.SetColumnWidth(column_index,
                wx.LIST_AUTOSIZE)
    
    def save(self, path):
        # Check if path already exists:
        yamlConfig = YamlConfiguration()
        yamlConfig.save(path)
        

if __name__ == '__main__':
    app = wx.App()
    frame = FileListController(None)
    frame.Show()
    app.MainLoop()

