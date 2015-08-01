
import wx
import os

from view.clsFileConfigPanel import FileConfigPanelView

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
        for radio, text, button in self.file_group:
            if radio is event.GetEventObject():
                text.Enable(True)
                button.Enable(True)
                self.dataFileRadioSelected = radio
            else:
                text.Enable(False)
                button.Enable(False)

        print self.dataFileRadioSelected
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
           
            # Check which text control to update by getting
            # the ID of the button.
            if event.GetId() == 49:
                self.local_file_txt.SetValue(path)
            else:
                self.remote_file_txt.SetValue(path)

        dlg.Destroy()
        event.Skip()

    def _getDataFilePath(self):
        # Decide which radio box is checked.
        if self.dataFileRadioSelected in self.file_group[0]:
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

        
