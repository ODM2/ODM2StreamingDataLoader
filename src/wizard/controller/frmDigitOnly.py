import string
import wx

class DigitValidator(wx.PyValidator):
    '''
    This validator class is used to ensure that a file path
    entered into a text control actually exists.

    '''
    def __init__(self):
        super(DigitValidator, self).__init__()
        self.Bind(wx.EVT_CHAR, self.onChar)
        self.Bind(wx.EVT_SET_FOCUS, self.onClick)

    def Clone(self):
        '''
        Every validator must implement a Clone method.
        '''
        return DigitValidator()
    
    def Validate(self, win):
        textControl = self.GetWindow()
        value = textControl.GetValue()
        print "Validating!", value
        print value.count('.')
        if not len(value):
            #textControl.SetBackgroundColour('#C5EFFF')
            textControl.SetBackgroundColour('#FFFAC5')
            return False
        if value.count('.') > 1:
            #textControl.SetBackgroundColour('#C5EFFF')
            textControl.SetBackgroundColour('#FFFAC5')
            return False
        
        if value.count('-') > 1:
            #textControl.SetBackgroundColour('#C5EFFF')
            textControl.SetBackgroundColour('#FFFAC5')
            return False
            
        for x in value:
            # If one of the characters is not a number
            # and not a "." or empty.
            if x not in string.digits and x != '.' and x != '-':
                #textControl.SetBackgroundColour('#C5EFFF')
                textControl.SetBackgroundColour('#FFFAC5')
                return False

        if True not in [False if value.find(i) < 0 else True for i in string.digits]:
            textControl.SetBackgroundColour('#FFFAC5')
            return False
            
        return True
    
    def onChar(self, event):    
        key = event.GetKeyCode()

        text = self.GetWindow().GetValue()

        print text

        if text.count('.') == 1 and chr(key) == '.':
            return
        
        if key == 45 and len(text) > 0 and self.GetWindow().GetInsertionPoint() != 0:
            return

        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return

        if chr(key) in string.digits or key == 46 or key == 45:
            event.Skip()
            return
         
        if not wx.Validator_IsSilent():
            wx.Bell()

        return
    
    def onClick(self, event):
        print self.GetWindow().GetInsertionPoint()
        control = self.GetWindow()
        control.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
        control.Refresh()
        event.Skip()
        return

    def TransferToWindow(self):
        return True
    def TransferFromWindow(self):
        return True

