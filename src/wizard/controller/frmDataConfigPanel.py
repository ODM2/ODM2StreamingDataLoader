
import wx
from copy import deepcopy
from collections import namedtuple 

from src.wizard.view.clsDataConfigPanel \
    import DataConfigPanelView, MyColLabelRenderer
from src.handlers.csvHandler import CSVReader
from src.common.functions import searchDict
from src.controllers.Database import Database

from src.wizard.controller.frmSeriesWizard import SeriesWizardController
from src.wizard.controller.frmVirtualGrid import GridBase

from src.wizard.controller.frmSeriesDialog import SeriesSelectDialog

from src.wizard.models.ResultMapping import ResultMapping

from api.ODM2.services.readService import ReadODM2

class DataConfigPanelController(DataConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(DataConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        
        self.prev_data = {}
        self.inputDict = {}
        #self.m_button8.Enable(False)
        self.m_listCtrl3.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.rightClick)


    def rightClick(self, event):
        if len(event.GetEventObject().GetSelectedObjects()) < 1:
            return

        menu = wx.Menu()
        menu.Append(11, "Edit Mapping")
        menu.Append(12, "Delete Mapping")
        
        wx.EVT_MENU(menu, 11, self.editMapping)
        wx.EVT_MENU(menu, 12, self.deleteMapping)
        
        if len(event.GetEventObject().GetSelectedObjects()) > 1:
            menu.Enable(11, False)
            menu.SetLabel(12, "Delete Mappings")

        self.PopupMenu(menu)
        menu.Destroy()
        event.Skip()

    def editMapping(self, event):
        self.selectedColumn = \
            self.m_listCtrl3.GetSelectedObject().variableName
        self.runSeriesSelectDialog()
        event.Skip()
    
    def deleteMapping(self, event):
        names = [obj.variableName for obj in \
            self.m_listCtrl3.GetSelectedObjects()]
        for i in range(0, self.m_listCtrl1.GetNumberCols()):
            if str(self.m_listCtrl1.GetColLabelValue(i)) in names:
                self.m_listCtrl1.SetColLabelRenderer(\
                    i,
                    MyColLabelRenderer(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND)))
                self.m_listCtrl1.Refresh()
        
        for name in self.m_listCtrl3.GetSelectedObjects():
            self.inputDict['Mappings'].pop(name.variableName)

        self.m_listCtrl3.RemoveObjects(\
            self.m_listCtrl3.GetSelectedObjects())
        self.m_listCtrl3.RepopulateList()
        event.Skip()

    def getInput(self):
        '''
        A method which returns a dict of data.
        Used to share data between panels.
        '''
        try:
            lastUpdate = str(self.inputDict['Schedule']['LastUpdate'])
        except KeyError: 
            self.inputDict['Schedule']['LastUpdate'] = "--"
        i = self.choiceTimeCol.GetSelection()
        self.inputDict['Settings']['DateTimeColumnName'] = \
            str(self.choiceTimeCol.GetString(i))
        self.inputDict['Settings']['FillGaps'] = 'false'
        for k,v in self.inputDict['Mappings'].iteritems():
            #print v
            v['IntendedTimeSpacing'] = self.spinTimeSpacing.GetValue()
            i = self.choiceUnitID.GetSelection()
            v['IntendedTimeSpacingUnitID'] = int(\
                filter(\
                str.isdigit,
                str(self.choiceUnitID.GetString(i))))
        self.inputDict['Settings']['UTCOffset'] = \
            self.spinUTCOffset.GetValue()
        return self.inputDict

    def setInput(self, data):
        '''
        A method to populate the controls/widgets with the contents
        of the given data parameter.
        '''
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
            
            self.m_listCtrl3.DeleteAllItems()
            self.m_listCtrl3.RepopulateList()


            csv = CSVReader()

            try:
                read = self.parent.db.getReadSession()
                timeUnits = read.getUnitsByTypeCV('time')
                for unit in timeUnits:
                    #self.choiceUnitID.Append(unit.UnitsName+" (id "+str(unit.UnitsID)+")")
                    self.choiceUnitID.Append(unit.UnitsName+" (id "+str(unit.UnitsID)+")")
                self.choiceUnitID.SetSelection(0)
               
                try:
                    self.spinTimeSpacing.SetValue(\
                        searchDict(self.inputDict['Mappings'],
                            'IntendedTimeSpacing'))
                except KeyError:
                    pass
                try:
                    unitID = searchDict(self.inputDict['Mappings'],
                        'IntendedTimeSpacingUnitID')
                    unit = read.getUnitById(int(unitID))
                    self.choiceUnitID.Append(unit.UnitsName+" (id "+str(unit.UnitsID)+")")
                    i = self.choiceUnitID.FindString(unit.UnitsName+" (id "+str(unit.UnitsID)+")")
                    self.choiceUnitID.SetSelection(i)
                except KeyError:
                    pass
                
                try:
                    offset = self.inputDict['Settings']['UTCOffset']
                    self.spinUTCOffset.SetValue(int(offset))
                except KeyError:
                    pass
                
                self.choiceTimeCol.Clear()
                try:
                    dateCol = self.inputDict['Settings']['DateTimeColumnName']
                    i = self.choiceTimeCol.FindString(str(dateCol))
                    self.choiceTimeCol.SetSelection(i)
                except KeyError:
                    pass
                
                
                df = csv.dataFrameReader(searchDict(data, 'FileLocation'),
                    header=searchDict(data, 'HeaderRowPosition'), sep=searchDict(data, 'Delimiter'),
                    dataBegin=searchDict(data, 'DataRowPosition'))
                
                columns = csv.getColumnNames(df)
                print columns
                # Create the underlying table of data for
                # the grid control. Having a virtual table
                # enables the control to display millions of
                # cells of data efficiently.
                base = GridBase(csv.getData(df[:50]), columns)
                # Assign the table to the grid control.
                self.m_listCtrl1.setTable(base)
              
                [self.choiceTimeCol.Append(column) \
                    for column in columns]
                self.choiceTimeCol.SetSelection(0)

                for column in range(self.m_listCtrl1.GetNumberCols()):
                    self.m_listCtrl1.AutoSizeColLabelSize(column)
                
                index = self.choiceTimeCol.GetSelection()
                self.selectedDateColumn = \
                    self.choiceTimeCol.GetString(index)
                

                read = self.parent.db.getReadSession()
                 
                try:
                    for k,v in self.inputDict['Mappings'].iteritems():
                        variable = k
                        for i in range(0, self.m_listCtrl1.GetNumberCols()):
                            if variable == str(self.m_listCtrl1.GetColLabelValue(i)):
                                mapping = read.getDetailedResultInfo(\
                                    "Time series coverage",
                                    v['ResultID'])
                                mapped = mapping[0]
                                self.m_listCtrl3.AddObject(
                                    ResultMapping(mapped.resultID,
                                        mapped.samplingFeatureCode,
                                        mapped.samplingFeatureName,
                                        mapped.methodCode,
                                        mapped.methodName,
                                        mapped.variableCode,
                                        mapped.variableNameCV,
                                        mapped.processingLevelCode,
                                        mapped.processingLevelDef,
                                        mapped.unitsName,
                                        variable))
                            #else:
                            #    self.inputDict['Mappings'].pop(variable)
                                
                except KeyError:
                    pass
                try:
                    for i in range(0, self.m_listCtrl1.GetNumberCols()):
                        if str(self.m_listCtrl1.GetColLabelValue(i))\
                        in self.inputDict['Mappings'].keys():
                            self.m_listCtrl1.SetColLabelRenderer(\
                                i,
                                MyColLabelRenderer('#50c061'))
                        else:
                            self.m_listCtrl1.SetColLabelRenderer(\
                                i,
                                MyColLabelRenderer(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND)))
                    self.m_listCtrl1.Refresh()
                except KeyError:
                    pass
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
        event.Skip
    
    def onColDoubleClick(self, event):
        if event.GetCol() > -1:
            self.selectedColumn = \
                self.m_listCtrl1.GetColLabelValue(event.GetCol())
            print self.selectedColumn 
            if self.selectedColumn == self.selectedDateColumn:
                msg = wx.MessageBox('This column is not mappable because you have chosen it as your date time column.', 'Configuration Error')
            else:
                if self.runSeriesSelectDialog():
                    self.m_listCtrl1.SetColLabelRenderer(\
                        int(event.GetCol()),
                        MyColLabelRenderer('#50c061'))
                    self.m_listCtrl1.Refresh()
        event.Skip()
    
    def onTimeSelect(self, event):
        index = self.choiceTimeCol.GetSelection()
        self.selectedDateColumn = self.choiceTimeCol.GetString(index)

        event.Skip()
   
    def onTimeChoice(self, event):
        self.selectedDateColumn = event.GetEventObject().GetString(event.GetEventObject().GetSelection())
        print self.selectedDateColumn 
        event.Skip()


    def runSeriesSelectDialog(self):
        dlg = SeriesSelectDialog(self,
                variable=self.selectedColumn,
                database=self.parent.db)
        dlg.CenterOnParent()
        if dlg.ShowModal() == wx.ID_OK:
            dlg.selectedResult.variableName = self.selectedColumn
            #print dlg.selectedResult.variableNameCV
            #import pprint
            
            if "Mappings" not in self.inputDict.keys():
                self.inputDict.update({'Mappings':{}})
            if self.selectedColumn not in \
                self.inputDict["Mappings"].keys():
                self.inputDict['Mappings'].update(\
                    {str(self.selectedColumn):{\
                        'ResultID':int(dlg.selectedResult.resultID),
                        'LastByteRead':0,
                        'CalculateAggInterval':'false'}})
            
            #pprint.pprint(self.inputDict)
            for m in self.m_listCtrl3.GetObjects():
                if m.variableName == dlg.selectedResult.variableName:
                    self.m_listCtrl3.RemoveObjects([m])
                    break

            self.m_listCtrl3.AddObject(dlg.selectedResult)
            dlg.Destroy()
            return True
        dlg.Destroy()
        return False


