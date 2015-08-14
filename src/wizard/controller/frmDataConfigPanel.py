
import wx
from copy import deepcopy

from view.clsDataConfigPanel import DataConfigPanelView
from handlers.csvHandler import CSVReader

from controller.frmSeriesWizard import SeriesWizardController
from controller.frmVirtualGrid import GridBase

class DataConfigPanelController(DataConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(DataConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        
        self.prev_data = {}
        self.inputDict = {}

    def getInput(self):
        '''
        A method which returns a dict of data.
        Used to share data between panels.
        '''
        return self.inputDict

    def populate(self, data):
        '''
        A method to populate the controls/widgets with the contents
        of the given data parameter.
        '''
        print data
        self.inputDict = data
        # Update the list control only if the new data is different.
        if cmp(self.prev_data, data) != 0:
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

            #self.m_listCtrl1.RefreshAllItems()
            
            df = csv.dataFrameReader(data['dataFilePath'],
                header=data['columnBegin'], sep=data['delimiter'],
                dataBegin=data['dataBegin'])
            
            columns = csv.getColumnNames(df)
            
            base = GridBase(csv.getData(df), columns)

            self.m_listCtrl1.setTable(base)
            #self.m_listCtrl1.InsertColumns(columns)
            #self.m_listCtrl1.SetItemCount(len(df))
            #self.m_listCtrl1.setData(csv.getData(df))
            
            #for column_index in range(\
            #        self.m_listCtrl1.GetColumnCount()):
            #    self.m_listCtrl1.SetColumnWidth(column_index,
            #        wx.LIST_AUTOSIZE)

        self.prev_data = deepcopy(data)

    def onAddNew(self, event):
        seriesWizard = SeriesWizardController(self,
            title=u'Create New Mapping For %s' % self.selectedColumn)
        seriesWizard.run()
        event.Skip()
    
    def onColClick(self, event):
        # Get Number of items (rows) in the table.
        count = self.m_listCtrl1.GetItemCount()
        # Set the selected column to whichever was clicked.
        self.selectedColumn = self.m_listCtrl1.getColumnText(\
            event.GetColumn())

        for row in range(count):
            item = self.m_listCtrl1.GetItem(itemId=row,
                col=event.GetColumn())
            self.m_listCtrl1.Select(row)
        event.Skip()


