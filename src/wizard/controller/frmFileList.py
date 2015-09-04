
import wx

from view.clsFileList import FileListView
from models.YamlConfiguration import YamlConfiguration


class FileListController(FileListView):
    def __init__(self, daddy, **kwargs):
        super(FileListController, self).__init__(daddy, **kwargs)
        self.parent = daddy

        # The list to store a list of dictionaries.
        # Each dictionary is an entry in a YAML
        # configuration file.
        self.yamlDataList = []
    
    def update(self, newData):
        
        print "updating! ", newData
        data = self.getRowData2(newData)
        for d in data:
            self.fileListCtrl.Append(d)
        # Add the object to our list.
        # TODO This will need to append a
        # dictionary that is compatable with
        # the YamlConfiguration class.
        self.yamlDataList.append([newData])
    
    def populateRows(self, paths):
        # Clear the previous data from the list.
        self.fileListCtrl.DeleteAllItems()
        
        # Loop through each income file path;
        # there may be one to many.
        for path in paths:
            # Create a YAML representation.
            yamlConfig = YamlConfiguration(path)
            print yamlConfig.get()
            # Add the object to our list.
            self.yamlDataList.append(yamlConfig)
            # Now extract only the parts from the file
            # that will be displayed iside the list control.
            data_list = self.getRowData(yamlConfig.get())
            # Finally, append the list control with the
            # appropriate data.
            for data in data_list:
                self.fileListCtrl.Append(data)

        # Adjust the width of the list columns. 
        for column_index in range(self.fileListCtrl.GetColumnCount()):
            self.fileListCtrl.SetColumnWidth(column_index,
                wx.LIST_AUTOSIZE)
        return True

    def getRowData(self, dictionary):
        data_list = []
        for file_block in reversed(dictionary):
            print "file block", file_block
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

            # This is what's going into the list control:
            data = [id, database_server, database_name, file_path,
                period, begin_date, last_update]
            data_list.append(data)
        return data_list
    
    def getRowData2(self, dictionary):
        data_list = []
        for file_block in reversed(dictionary):
            database_name = u'%s' % (self.searchDict(file_block[1], 'DatabaseName'))
            database_server = u'%s' % (self.searchDict(file_block[1], 'Address'))
            id = u'%s' % (file_block[0])
            file_path = u'%s' % (self.searchDict(file_block[1], 'FileLocation'))
            last_update = u'%s' % (self.searchDict(file_block[1], 'LastUpdate'))
            begin_date = u'%s' % (self.searchDict(file_block[1], 'Beginning'))
            period = u'%s' % (self.searchDict(file_block[1], 'Frequency'))
            # This is what's going into the list control:
            data = [id, database_server, database_name, file_path,
                period, begin_date, last_update]
            data_list.append(data)
        return data_list
    
    def searchDict(self, obj, key):
        if key in obj:
            return obj[key]
        for k,v in obj.items():
            if isinstance(v, dict):
                item = self.searchDict(v, key)
                if item is not None:
                    return item

    def appendRow(self, dataDict):
        '''
        appendRow adds a list of data to the list control.
        '''
        data = ['fake_id']
        data.append(dataDict['address'])
        data.append(dataDict['db'])
        data.append(dataDict['dataFilePath'])
        data.append(dataDict['frequency'])
        data.append(dataDict['begin'])
        data.append('--')
        self.fileListCtrl.Append(data)
        
        # Adjust the width of the list columns. 
        for column_index in range(self.fileListCtrl.GetColumnCount()):
            self.fileListCtrl.SetColumnWidth(column_index,
                wx.LIST_AUTOSIZE)
   
    def updateRow(self, row, dataDict):
        '''
        updateRow modifies an existing row in the list control.
        '''
        data = ['fake_id']
        data.append(dataDict['address'])
        data.append(dataDict['db'])
        data.append(dataDict['dataFilePath'])
        data.append(dataDict['frequency'])
        data.append(dataDict['begin'])
        data.append('--')
        for i, col in zip(data, range(len(data))):
            self.fileListCtrl.SetStringItem(row, col, i)
        
        # Adjust the width of the list columns. 
        for column_index in range(self.fileListCtrl.GetColumnCount()):
            self.fileListCtrl.SetColumnWidth(column_index,
                wx.LIST_AUTOSIZE)

    def getSelectionTextByColumn(self, col=0):
        return self.fileListCtrl.GetItemText(\
            self.fileListCtrl.GetFocusedItem(), col)

    def getSelection(self):
        return self.fileListCtrl.GetFocusedItem()

    def deleteRow(self, row):
        return self.fileListCtrl.DeleteItem(row)

    def save(self, path):
        # Check if path already exists:
        yamlConfig = YamlConfiguration()
        yamlConfig.save(path)
        
    def onSelection(self, event):
        #self.parent.setMapping(event....)
        self.parent.toolbar.del_btn.Enable(True)
        self.parent.toolbar.edit_btn.Enable(True)
        event.Skip()

    def onDeselection(self, event):
        self.parent.toolbar.del_btn.Enable(False)
        self.parent.toolbar.edit_btn.Enable(False)
        event.Skip()

    def onDoubleClick(self, event):
        self.parent.toolbar.onEditButtonClick(event)
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = FileListController(None)
    frame.Show()
    app.MainLoop()

