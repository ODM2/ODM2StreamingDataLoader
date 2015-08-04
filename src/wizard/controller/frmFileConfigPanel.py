
import wx
import os
from datetime import datetime

from view.clsFileConfigPanel import FileConfigPanelView
from controller.frmFilePathValidator import FilePathValidator

class FileConfigPanelController(FileConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(FileConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        self.inputDict = {}
        self.dataFileRadioSelected = self.local_file_radio


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
            self.remote_file_txt.SetValidator(FilePathValidator())
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
            path = self.local_file_txt.GetValue()
            return path or None
        
        path = self.remote_file_txt.GetValue()
        return path or None

    def _getDataBeginLine(self):
        dataStart = self.m_spinCtrl4.GetValue()
        return dataStart

    def _getColumnBeginLine(self):
        value = self.m_spinCtrl2.GetValue()
        return value

    def _getDelimiter(self):
        value = {u'Comma': ',', u'Tab': '\t', u'Custom': None}
        index = self.m_choice1.GetSelection()
        return value[self.m_choice1.GetString(index)]
    
    def _getTime(self):
        value = self.m_spinCtrl1.GetValue()
        return value

    def _getFrequency(self):
        value = {u'Hours': 'Hour', u'Minutes': 'Minute'}
        index = self.m_choice2.GetSelection()
        return value[self.m_choice2.GetString(index)]

    def _getBegin(self):
        date = self.m_datePicker3.GetValue()
        time = self.m_timePicker1.GetValue()

        v1 = datetime.strptime(str(date), '%c').strftime('%m/%d/%Y')
        value = v1 + ' ' + str(time)
        return value

    def getInput(self):
        dataFilePath = self._getDataFilePath()
        dataBegin = self._getDataBeginLine()
        columnBegin = self._getColumnBeginLine()
        delimiter = self._getDelimiter()
        time = self._getTime()
        frequency = self._getFrequency()
        begin = self._getBegin()

        if dataFilePath:
            self.inputDict['dataFilePath'] = dataFilePath
            self.inputDict['dataBegin'] = dataBegin
            self.inputDict['columnBegin'] = columnBegin
            self.inputDict['delimiter'] = delimiter
            self.inputDict['time'] = time
            self.inputDict['frequency'] = frequency
            self.inputDict['begin'] = begin

        return self.inputDict


    def populate(self, data={}):
        return self.inputDict

        
