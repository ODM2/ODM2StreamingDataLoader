
import wx

from src.wizard.view.clsFileList import FileListView
from src.models.YamlConfiguration import YamlConfiguration
from src.common.functions import searchDict

class FileListController(FileListView):
    def __init__(self, daddy, **kwargs):
        super(FileListController, self).__init__(daddy, **kwargs)
        self.parent = daddy

        # The list to store a list of dictionaries.
        # Each dictionary is an entry in a YAML
        # configuration file.
        self.yamlDataList = []
    
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
            dbName = u'%s' % (searchDict(tup[1], 'DatabaseName'))
            dbServer = u'%s' % (searchDict(tup[1], 'Address'))
            path = u'%s' % (searchDict(tup[1], 'FileLocation'))
            lastUpdate = u'%s' % (searchDict(tup[1], 'LastUpdate'))
            begin = u'%s' % (searchDict(tup[1], 'Beginning'))
            period = u'%s %s' % (searchDict(tup[1], 'Time'),
                searchDict(tup[1], 'Frequency'))
            data = [id, dbServer, dbName,
                    path, period, begin, lastUpdate]
            return data
        except KeyError as e:
            wx.MessageBox('The configuration file appears to be missing the "%s" attribute. This mapping has not been loaded.' % e, 'Error reading id "%s"' % tup[0])
    
    def editRow(self, row, dataDict):
        '''
            editRow modifies an existing list entry.
        '''
        

    def appendRow(self, dataDict):
        '''
        appendRow adds a list of data to the list control.
        '''
        dataForListCtrl = self._getRowData(dataDict) 

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

