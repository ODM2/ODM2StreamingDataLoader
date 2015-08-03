
import wx
import os

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
        value = self.m_spinCtrl4.GetValue()
        if value <= 1:
            return 0
        return value - 2

    def getInput(self):
        dataFilePath = self._getDataFilePath()
        dataBegin = self._getDataBeginLine()

        if dataFilePath:
            self.inputDict['dataFilePath'] = dataFilePath
            self.inputDict['dataBegin'] = dataBegin

        return self.inputDict


    def populate(self, data={}):
        pass

        
