
import wx
from copy import deepcopy
from collections import namedtuple 

from src.wizard.view.clsDataConfigPanel import DataConfigPanelView
from src.handlers.csvHandler import CSVReader
from src.common.functions import searchDict

from src.wizard.controller.frmSeriesWizard import SeriesWizardController
from src.wizard.controller.frmVirtualGrid import GridBase

class DataConfigPanelController(DataConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(DataConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        
        self.prev_data = {}
        self.inputDict = {}

        self.m_button8.Enable(False)

    def getInput(self):
        '''
        A method which returns a dict of data.
        Used to share data between panels.
        '''
        self.inputDict['LastUpdate'] = '-'
        return self.inputDict

    def populate(self, data):
        '''
        A method to populate the controls/widgets with the contents
        of the given data parameter.
        '''
        print "populate", data

        
        self.inputDict.update(data)
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
            
            try:
                df = csv.dataFrameReader(data['FileLocation'],
                    header=data['HeaderRowPosition'], sep=data['Delimiter'],
                    dataBegin=data['DataRowPosition'])
                
                columns = csv.getColumnNames(df)

                # Create the underlying table of data for
                # the grid control. Having a virtual table
                # enables the control to display millions of
                # cells of data efficiently.
                base = GridBase(csv.getData(df), columns)
                # Assign the table to the grid control.
                self.m_listCtrl1.setTable(base)
              
                # Refresh the values
                self.m_choice4.Clear()
                self.m_choice3.Clear()
                # Set the values of the time choice controls.
                [self.m_choice4.Append(column) \
                    for column in columns]
                self.m_choice4.SetSelection(0)
                [self.m_choice3.Append(column) \
                    for column in columns]
                self.m_choice3.SetSelection(0)

                for column in range(self.m_listCtrl1.GetNumberCols()):
                    self.m_listCtrl1.AutoSizeColLabelSize(column)
                
                #[self.m_choice4.SetString(n, unicode(string)) \
                #    for n, string in \
                #    zip(range(len(columns)), columns)]


                self.m_listCtrl3.ClearAll()
                self.m_listCtrl3.InsertColumn(0, 'Value Column')
                self.m_listCtrl3.InsertColumn(1, 'Variable')
                self.m_listCtrl3.InsertColumn(2, 'Units')
                self.m_listCtrl3.InsertColumn(3, 'Processing Level')
                self.m_listCtrl3.InsertColumn(4, 'Actions')
                self.m_listCtrl3.InsertColumn(5, 'Results')

                index = self.m_choice3.GetSelection()
                self.selectedDateColumn = \
                    self.m_choice3.GetString(index)
            except:
                raise
        # Important to make a deep copy, or else
        # data gets changed.
        self.prev_data = deepcopy(data)

    def onAddNew(self, event):
        self.doRunResultWizard()
        event.Skip()
   
    def onCellClick(self, event):
        self.m_button8.Enable(False)
        event.Skip()
    
    def onColClick(self, event): 
        if event.GetCol() > -1:
            # Get the column header.
            self.selectedColumn = \
                self.m_listCtrl1.GetColLabelValue(event.GetCol())
            # Enable the 'add' button.
            self.m_button8.Enable(True)
        else:
            self.m_button8.Enable(False)
        event.Skip()
    
    def onColDoubleClick(self, event):
        if event.GetCol() > -1:
            self.selectedColumn = \
                self.m_listCtrl1.GetColLabelValue(event.GetCol())
            print self.selectedColumn 
            if self.selectedColumn == self.selectedDateColumn:
                msg = wx.MessageBox('This column is not mappable because you have chosen it as your date time column.', 'Configuration Error')
            else:
                self.doRunResultWizard()
        event.Skip()
    
    def onTimeSelect(self, event):
        if event.GetEventObject() == self.m_radioBtn3:
            self.m_choice3.Enable(True)
            self.m_choice4.Enable(False)

            index = self.m_choice3.GetSelection()
            self.selectedDateColumn = self.m_choice3.GetString(index)
        if event.GetEventObject() == self.m_radioBtn4:
            self.m_choice3.Enable(False)
            self.m_choice4.Enable(True)
            
            index = self.m_choice4.GetSelection()
            self.selectedDateColumn = self.m_choice4.GetString(index)

        event.Skip()
   
    def onTimeChoice(self, event):
        self.selectedDateColumn = event.GetEventObject().GetString(event.GetEventObject().GetSelection())
        print self.selectedDateColumn 
        event.Skip()

    def doRunResultWizard(self):
        Credentials = namedtuple('Credentials',
            'dbType, host, db_name, uid, pwd')

        resultWizard = SeriesWizardController(self,
            title=u'Create New Mapping For %s' % self.selectedColumn,
            label=self.selectedColumn,
            creds=Credentials(searchDict(self.inputDict,'Engine'),
                searchDict(self.inputDict,'Address'),
                searchDict(self.inputDict,'DatabaseName'),
                searchDict(self.inputDict,'UserName'),
                searchDict(self.inputDict,'Password')))
        configData = resultWizard.run()
        self.m_listCtrl3.Append([configData[i] for i in configData])


