
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
    
    def populateRows(self, yamlObject):
        '''
            The populateRows method takes in a list
            of tuples containing data from a yaml
            file, and sends each one off to be formatted
            for the list control.
            
            For example: [('id',{...}),]
            
            Generally, you should pass the result
            of a call to YamlConfiguration.get() into
            this method.
        '''
        # For each tuple in the list...
        for tup in yamlObject:
            try:
                # Get only the neccessary parts of the data.
                dataForListCtrl = self._getRowData(tup)
                # Append the data to the list control.
                self.fileListCtrl.Append(dataForListCtrl)
            except Exception:
                continue
        # Adjust the column widths.
        for column in range(self.fileListCtrl.GetColumnCount()):
            self.fileListCtrl.SetColumnWidth(column, wx.LIST_AUTOSIZE)


    def _getRowData(self, tup):
        '''
            The getRowData method takes in a tuple
            in this format: ('id', {...}) and gathers
            data from the dictionary to be shown in
            the list control. Returns a list of the
            gathered data, or throws a KeyError
            exception.
        '''
        try:
            id = tup[0]
            dbName = u'%s' % (self.searchDict(tup[1], 'DatabaseName'))
            dbServer = u'%s' % (self.searchDict(tup[1], 'Address'))
            path = u'%s' % (self.searchDict(tup[1], 'FileLocation'))
            lastUpdate = u'%s' % (self.searchDict(tup[1], 'LastUpdate'))
            begin = u'%s' % (self.searchDict(tup[1], 'Beginning'))
            period = u'%s %s' % (self.searchDict(tup[1], 'Time'),
                self.searchDict(tup[1], 'Frequency'))
            data = [id, dbServer, dbName,
                    path, period, begin, lastUpdate]
            return data
        except KeyError as e:
            wx.MessageBox('The configuration file appears to be missing the "%s" attribute. This mapping has not been loaded.' % e, 'Error reading id "%s"' % tup[0])

    def searchDict(self, obj, key, lvl=0):
        # Base case: key is in the first level of dictionary.
        if key in obj:
            return obj[key]
        # Key is not in the first level of the dictionary.
        # Loop through keys to find nested dictionaries.
        for k,v in obj.items():
            # Recurse if a dictionary is found.
            if isinstance(v, dict):
                item = self.searchDict(v, key, lvl+1)
                if item is not None:
                    return item
        # If we're done looking and key still has not
        # been found, then raise a KeyError
        if lvl == 0:
            raise KeyError(key)

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

