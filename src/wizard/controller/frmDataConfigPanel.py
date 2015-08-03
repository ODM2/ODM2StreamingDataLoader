
import wx

from view.clsDataConfigPanel import DataConfigPanelView
from handlers.csvHandler import CSVReader
from copy import deepcopy

class DataConfigPanelController(DataConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(DataConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        
        self.prev_data_x = {}

    def getInput(self):
        '''
        A method which returns a dict of data.
        Used to share data between panels.
        '''
        return {}

    def populate(self, data):
        '''
        A method to populate the controls/widgets with the contents
        of the given data parameter.
        '''
        # Update the list control only if the new data is different.
        if cmp(self.prev_data_x, data) != 0:
            # Here is what happens in here:
            # Create a CSV reader object.
            # Clear the list control of previous data.
            # Read the file to get the csv data.
            # Get column headers and InsertColumn for each of them.
            # Set the number of items because this is
            # a virtual list ctrl.
            # Give the virtual list ctrl a data source.
            # Adjust column width.
            csv = CSVReader()

            self.m_listCtrl1.RefreshAllItems()

            df = csv.dataFrameReader(data['dataFilePath'],
                skip=data['dataBegin'])
            
            columns = csv.getColumnNames(df)
            
            for column in columns:
                self.m_listCtrl1.InsertColumn(columns.index(column),\
                    column)
            
            self.m_listCtrl1.SetItemCount(len(df))
            self.m_listCtrl1.setData(csv.getData(df))
            
            for column_index in range(\
                    self.m_listCtrl1.GetColumnCount()):
                self.m_listCtrl1.SetColumnWidth(column_index,
                    wx.LIST_AUTOSIZE)

        self.prev_data_x = deepcopy(data)
        
