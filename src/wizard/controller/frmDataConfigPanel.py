
import wx

from view.clsDataConfigPanel import DataConfigPanelView
from handlers.csvHandler import CSVReader

class DataConfigPanelController(DataConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(DataConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        
    def getInput(self):
        '''
        A method which returns a dict of data.
        Used to share data between panels.
        '''
        return {}

    def populate(self, data={}):
        '''
        A method to populate the controls/widgets with the contents
        of the given data parameter.
        '''
        print type(data['dataBegin'])
        # Read the file.
        csv = CSVReader()
        data = csv.dataFrameReader(data['dataFilePath'],
            skip=data['dataBegin'] - 2)
        
        # TODO: Delete data if file path was changed.
        
        # Get column headers and InsertColumn for each of them.
        columns = csv.getColumnNames(data)
        for column in columns:
            self.m_listCtrl1.InsertColumn(columns.index(column), column)

        # Read data into appropriate columns.
        self.m_listCtrl1.SetItemCount(len(data)-1)
        self.m_listCtrl1.setData(csv.getData(data))
        #i=0
        #for row in csv.getData(data):
        #    self.m_listCtrl1.OnGetItemText(i, row)
        #    i = i + 1

