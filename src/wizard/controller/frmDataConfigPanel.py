
import wx
from copy import deepcopy
from collections import namedtuple 

from src.wizard.view.clsDataConfigPanel import DataConfigPanelView
from src.handlers.csvHandler import CSVReader
from src.common.functions import searchDict
from src.controllers.Database import Database

from src.wizard.controller.frmSeriesWizard import SeriesWizardController
from src.wizard.controller.frmVirtualGrid import GridBase

from src.wizard.controller.frmSeriesDialog import SeriesSelectDialog

class DataConfigPanelController(DataConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(DataConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        
        self.prev_data = {}
        self.inputDict = {}

        #self.m_button8.Enable(False)

    def getInput(self):
        '''
        A method which returns a dict of data.
        Used to share data between panels.
        '''
        #self.inputDict['LastUpdate'] = '-'
        return self.inputDict

    def setInput(self, data):
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
                df = csv.dataFrameReader(searchDict(data, 'FileLocation'),
                    header=searchDict(data, 'HeaderRowPosition'), sep=searchDict(data, 'Delimiter'),
                    dataBegin=searchDict(data, 'DataRowPosition'))
                #df = csv.dataFrameReader(data['FileLocation'],
                #    header=data['HeaderRowPosition'], sep=data['Delimiter'],
                #    dataBegin=data['DataRowPosition'])
                
                columns = csv.getColumnNames(df)

                # Create the underlying table of data for
                # the grid control. Having a virtual table
                # enables the control to display millions of
                # cells of data efficiently.
                base = GridBase(csv.getData(df), columns)
                # Assign the table to the grid control.
                self.m_listCtrl1.setTable(base)
              
                # Refresh the values
                #self.m_choice4.Clear()
                #self.m_choice3.Clear()
                # Set the values of the time choice controls.
                [self.choiceTimeCol.Append(column) \
                    for column in columns]
                self.choiceTimeCol.SetSelection(0)
                #[self..Append(column) \
                #    for column in columns]
                #self.choiceTimeCol.SetSelection(0)

                for column in range(self.m_listCtrl1.GetNumberCols()):
                    self.m_listCtrl1.AutoSizeColLabelSize(column)
                
                index = self.choiceTimeCol.GetSelection()
                self.selectedDateColumn = \
                    self.choiceTimeCol.GetString(index)
            except:
                raise
        # Important to make a deep copy, or else
        # data gets changed.
        self.prev_data = deepcopy(data)

    def onAddNew(self, event):
        self.runSeriesSelectDialog()
        event.Skip()
   
    def onCellClick(self, event):
        #self.m_button8.Enable(False)
        event.Skip()
    
    def onColClick(self, event): 
        if event.GetCol() > -1:
            # Get the column header.
            self.selectedColumn = \
                self.m_listCtrl1.GetColLabelValue(event.GetCol())
            # Enable the 'add' button.
            #self.m_button8.Enable(True)
        #else:
            #self.m_button8.Enable(False)
        event.Skip#()
    
    def onColDoubleClick(self, event):
        if event.GetCol() > -1:
            self.selectedColumn = \
                self.m_listCtrl1.GetColLabelValue(event.GetCol())
            print self.selectedColumn 
            if self.selectedColumn == self.selectedDateColumn:
                msg = wx.MessageBox('This column is not mappable because you have chosen it as your date time column.', 'Configuration Error')
            else:
                self.runSeriesSelectDialog()
        event.Skip()
    
    def onTimeSelect(self, event):
        #if event.GetEventObject() == self.m_radioBtn3:
        #    #self.m_choice3.Enable(True)
        #    #self.m_choice4.Enable(False)
        
        index = self.choiceTimeCol.GetSelection()
        self.selectedDateColumn = self.choiceTimeCol.GetString(index)
        #if event.GetEventObject() == self.m_radioBtn4:
        #    self.m_choice3.Enable(False)
        #    self.m_choice4.Enable(True)
            
        #    index = self.m_choice4.GetSelection()
        #    self.selectedDateColumn = self.m_choice4.GetString(index)

        event.Skip()
   
    def onTimeChoice(self, event):
        self.selectedDateColumn = event.GetEventObject().GetString(event.GetEventObject().GetSelection())
        print self.selectedDateColumn 
        event.Skip()


    def runSeriesSelectDialog(self):
        db = Database()
        Credentials = namedtuple('Credentials', 'engine, host, db_name, uid, pwd')
        db.createConnection(Credentials(\
            self.inputDict['Database']['Engine'],
            self.inputDict['Database']['Address'],
            self.inputDict['Database']['DatabaseName'],
            self.inputDict['Database']['UserName'],
            self.inputDict['Database']['Password']))
        dlg = SeriesSelectDialog(self,
                variable=self.selectedColumn,
                database=db)
        if dlg.ShowModal() == wx.ID_OK:
            print "Result...", dlg.selectedResult
            dlg.selectedResult.variableName = self.selectedColumn
            self.m_listCtrl3.AddObject(dlg.selectedResult)
        dlg.Destroy()


