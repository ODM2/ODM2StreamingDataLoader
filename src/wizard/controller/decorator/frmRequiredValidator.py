import string
import wx

class RequiredValidator(wx.PyValidator):
    '''
    This validator will ensure that whatever it's added to gets
    filled out.
    '''
    def __init__(self):
        super(RequiredValidator, self).__init__()
        self.Bind(wx.EVT_SET_FOCUS, self.onClick)

    def Clone(self):
        '''
        Every validator must implement a Clone method.
        '''
        return RequiredValidator()
    
    def Validate(self, win):
        textControl = self.GetWindow()
        value = textControl.GetValue()
        
        if not len(value):
            textControl.SetBackgroundColour('#FFFAC5')
            return False
            
        return True
    
    def onClick(self, event):
        control = self.GetWindow()
        control.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
        control.Refresh()
        event.Skip()
        return

    def TransferToWindow(self):
        return True
    def TransferFromWindow(self):
        return True

