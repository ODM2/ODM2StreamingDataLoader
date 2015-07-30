
import wx
import os

from view.clsFileConfigPanel import FileConfigPanelView

class FileConfigPanelController(FileConfigPanelView):
    def __init__(self, daddy, **kwargs):
        super(FileConfigPanelController, self).__init__(daddy, **kwargs)
        self.parent = daddy
        self.path = None

    def onFileSelect(self, event):
        for radio, text, button in self.file_group:
            if radio is event.GetEventObject():
                text.Enable(True)
                button.Enable(True)
            else:
                text.Enable(False)
                button.Enable(False)

        event.Skip()

    def onFileSelectPath(self, event):
        dlg = wx.FileDialog(self, message='Choose a Data File',
                defaultDir=os.getcwd(), defaultFile='',
                style=wx.OPEN | wx.CHANGE_DIR) 
        
        if dlg.ShowModal() == wx.ID_OK:
            self.path = dlg.GetPath()
           
            # Check which text control to update by getting
            # the ID of the button.
            if event.GetId() == 49:
                self.local_file_txt.SetValue(self.path)
            else:
                self.remote_file_txt.SetValue(self.path)

        dlg.Destroy()
        event.Skip()

    def getDataFilePath(self):
        return self.local_file_txt.GetValue()

    def getInput(self):
        print "path: ", type(self.path)
        return {'data': self.path}

    def populate(self, data={}):
        pass
