import string
import wx

class RequiredComboValidator(wx.PyValidator):
    '''
    This validator will ensure that whatever it's added to gets
    filled out.
    '''
    def __init__(self):
        super(RequiredComboValidator, self).__init__()
        self.Bind(wx.EVT_COMBOBOX, self.onCombo)

    def Clone(self):
        '''
        Every validator must implement a Clone method.
        '''
        return RequiredComboValidator()
    
    def Validate(self, win):
        comboControl = self.GetWindow()
        value = comboControl.GetSelection()
        
        if value == wx.NOT_FOUND:
            comboControl.SetBackgroundColour('#FFFAC5')
            return False
            
        return True
    
    def onCombo(self, event):
        control = self.GetWindow()
        control.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
        control.Refresh()
        event.Skip()
        return

    def TransferToWindow(self):
        return True
    def TransferFromWindow(self):
        return True

