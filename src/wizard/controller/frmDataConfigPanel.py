
import wx

from view.clsDataConfigPanel import DataConfigPanelView
from handlers.csvHandler import CSVReader

class DataConfigPanelController(DataConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(DataConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        
    def getInput(self):
        return {}

    def populate(self, data={}):
        # Read the file.
        csv = CSVReader()
        data = csv.dataFrameReader(data['data'])
        # Delete data if file path was changed.
        # Get column headers and InsertColumn for each of them.
        columns = csv.getColumnNames(data)
        for column in columns:
            print columns.index(column)
            self.m_listCtrl1.InsertColumn(columns.index(column), column)

        # Read data into appropriate columns.
        
        for row in csv.getData(data):
            self.m_listCtrl1.Append(row)

