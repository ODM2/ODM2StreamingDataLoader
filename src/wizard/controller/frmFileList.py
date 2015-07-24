
import wx

from view.clsFileList import FileListView
from models.YamlConfiguration import YamlConfiguration


class FileListController(FileListView):
    def __init__(self, daddy, **kwargs):
        super(FileListController, self).__init__(daddy, **kwargs)
        
        self.populateRows()

    def populateRows(self):
        yamlConfig = YamlConfiguration('/home/denver/test2.yaml')
        '''
        for file_block in yamlConfig.getAttributeDict():
            id = file_block
            database = yamlConfig.getAttributeDict('Database')
        '''
        data = []

        for file_block in yamlConfig.get():
            database_name = u'%s' % (file_block['Database']['DatabaseName'])
            database_server = u'%s' % (file_block['Database']['Address']) 
            print database_server
            print database_name
            
            id = 1

            file_path = u'%s' % (file_block['Settings']['FileLocation'])
            print file_path

            last_update = u'%s' % (file_block['Schedule']['LastUpdate'])
            print last_update

            begin_date = u'%s' % (file_block['Schedule']['Beginning'])
            print begin_date

            period = u'%s' % (file_block['Schedule']['Frequency'])
            print period

            data = [u'0', database_server, database_name, file_path,
                period, begin_date, last_update]
            
            print data
            self.fileListCtrl.Append(data)

if __name__ == '__main__':
    app = wx.App()
    frame = FileListController(None)
    frame.Show()
    app.MainLoop()

