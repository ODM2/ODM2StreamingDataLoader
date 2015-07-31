import wx
import os

class FilePathValidator(wx.PyValidator):
    '''
    This validator class is used to ensure that a file path
    entered into a text control actually exists.

    '''
    def __init__(self):
        super(FilePathValidator, self).__init__()

    def Clone(self):
        '''
        Every validator must implement a Clone method.
        '''
        return FilePathValidator()
    
    def Validate(self, win):
        text_ctrl = self.GetWindow()
        text = text_ctrl.GetValue()
        if not os.path.exists(text):
            text_ctrl.SetBackgroundColour('pink')
            wx.MessageBox('Not a valid file path.', 'You lie to me?')
            text_ctrl.SetFocus()
            text_ctrl.Refresh()
            return False
        else:
            text_ctrl.SetBackgroundColour(\
                wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            text_ctrl.Refresh()
            return True

    def TransferToWindow(self):
        return True
    
    def TransferFromWindow(self):
        return True

