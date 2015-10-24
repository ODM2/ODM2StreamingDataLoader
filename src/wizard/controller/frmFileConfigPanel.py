
import wx
import os
from datetime import datetime

from src.wizard.view.clsFileConfigPanel import FileConfigPanelView
from src.wizard.controller.frmFilePathValidator import FilePathValidator
from src.wizard.controller.frmURLValidator import URLValidator
from src.common.functions import searchDict, pydate2wxdate, wxdate2pydate

class FileConfigPanelController(FileConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(FileConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        self.inputDict = {}
        self.dataFileRadioSelected = self.local_file_radio
        self.remote_file_txt.SetValidator(wx.DefaultValidator)

        self.timeValue = {0: 'Hour', 1: 'Minute'}
        self.delimValue = {'Comma': ',', 'Tab': '\t', 'Custom': None}
    
    
    def onFileSelect(self, event):
        '''
        Event that happens when user clicks the local/remote
        file radio button.
        '''
        if event.GetEventObject() == self.local_file_radio:
            self.local_file_txt.Enable(True)
            self.remote_file_txt.Enable(False)
            self.local_file_btn.Enable(True)
            self.local_file_txt.SetValidator(FilePathValidator())
            self.remote_file_txt.SetValidator(wx.DefaultValidator)
            self.dataFileRadioSelected = self.local_file_radio

        if event.GetEventObject() == self.remote_file_radio:
            self.remote_file_txt.Enable(True)
            self.local_file_txt.Enable(False)
            self.local_file_btn.Enable(False)
            self.remote_file_txt.SetValidator(URLValidator())
            self.local_file_txt.SetValidator(wx.DefaultValidator)
            self.dataFileRadioSelected = self.remote_file_radio

        event.Skip()

    def onFileSelectPath(self, event):
        '''
        Event that happens when user clicks the file select button.
        '''
        dlg = wx.FileDialog(self, message='Choose a Data File',
                defaultDir=os.getcwd(), defaultFile='',
                style=wx.OPEN | wx.CHANGE_DIR) 
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.local_file_txt.SetValue(path)

        dlg.Destroy()
        event.Skip()

    def _getDataFilePath(self):
        # Decide which radio box is checked.
        if self.local_file_radio.GetValue():
            path = str(self.local_file_txt.GetValue())
            return path or None
        path = str(self.remote_file_txt.GetValue())
        if path.startswith('http://') == False:
            path = 'http://' + path
        return path or None

    def _getDataBeginLine(self):
        dataStart = self.m_spinCtrl4.GetValue()
        return dataStart

    def _getColumnBeginLine(self):
        value = self.m_spinCtrl2.GetValue()
        return value

    def _getDelimiter(self):
        #value = {u'Comma': ',', u'Tab': '\t', u'Custom': None}
        index = self.m_choice1.GetSelection()
        return self.delimValue[self.m_choice1.GetString(index)]
    
    def _getTime(self):
        value = self.m_spinCtrl1.GetValue()
        return value

    def _getFrequency(self):
        #value = {u'Hours': 'Hour', u'Minutes': 'Minute'}
        index = self.m_choice2.GetSelection()
        #return value[self.m_choice2.GetString(index)]
        return self.m_choice2.GetString(index)

    def _getBegin(self):
        date = self.m_datePicker3.GetValue()
        time = self.m_timePicker1.GetValue()
        begin = ''
        try:
            begin = datetime.strptime(str(date), '%c').strftime('%m/%d/%Y')
            begin = begin + ' ' + str(time)
        except ValueError:
            date = str(date)
            print date
            date = date.replace("'PMt'", '')
            date = date.replace("'AMt'", '')
            begin = datetime.strptime(date, '%A, %B %d, %Y %X %p').strftime('%m/%d/%Y')
            begin = begin + ' ' + str(time)
        return begin

    def getInput(self):
        dataFilePath = self._getDataFilePath()
        dataBegin = self._getDataBeginLine()
        columnBegin = self._getColumnBeginLine()
        delimiter = self._getDelimiter()
        time = self._getTime()
        frequency = self._getFrequency()
        begin = self._getBegin()

        if dataFilePath:
            if not self.inputDict.has_key('Schedule'):
                self.inputDict['Schedule'] = {}
            self.inputDict['Schedule']['Time'] = time
            self.inputDict['Schedule']['Frequency'] = str(frequency)
            self.inputDict['Schedule']['Beginning'] = begin
            
            if not self.inputDict.has_key('Settings'):
                self.inputDict['Settings'] = {}
            self.inputDict['Settings']['FileLocation'] = dataFilePath
            self.inputDict['Settings']['DataRowPosition'] = dataBegin
            self.inputDict['Settings']['HeaderRowPosition'] = columnBegin
            self.inputDict['Settings']['Delimiter'] = delimiter
        
        return self.inputDict


    def setInput(self, data={}):
        #print "data!! ", data
        # Populate the local or remote file text controls.
        print "!!!", data
        self.inputDict.update(data)
        try:
            if searchDict(data, 'FileLocation').startswith('http'):
                self.remote_file_txt.SetValue(searchDict(data, 'FileLocation'))
                self.remote_file_txt.Enable(True)
                self.local_file_txt.Enable(False)
                self.local_file_btn.Enable(False)
                self.remote_file_radio.SetValue(True)
                self.local_file_radio.SetValue(False)
                self.dataFileRadioSelected = self.remote_file_radio
            else:
                self.local_file_txt.SetValue(searchDict(data, 'FileLocation'))
            
            self.m_spinCtrl4.SetValue(searchDict(data, 'DataRowPosition'))
            self.m_spinCtrl2.SetValue(searchDict(data, 'HeaderRowPosition'))
            for key, value in self.delimValue.iteritems():
                if value == searchDict(data, 'Delimiter'):
                    index = self.m_choice1.FindString(key)
                    self.m_choice1.SetSelection(index)
            self.m_spinCtrl1.SetValue(searchDict(data, 'Time'))
            index = self.m_choice2.FindString(searchDict(data, 'Frequency'))
            self.m_choice2.SetSelection(index)

            date = datetime.strptime(searchDict(data, 'Beginning'),
                '%m/%d/%Y %I:%M:%S %p')
            print "date: ", date
            self.m_datePicker3.SetValue(pydate2wxdate(date))
            self.m_timePicker1.SetValue(str(date.time()))

            self.inputDict['Database'] = searchDict(data, 'Database')
            print self.inputDict
        except KeyError:
            print "no data..."

