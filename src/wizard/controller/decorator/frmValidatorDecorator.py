import string
import wx

class ValidatorDecorator(wx.PyValidator):
    '''
        Abstract decorator class
    '''
    def __init__(self, toBeDecorated):
        self.toBeDecorated = toBeDecorated
        super(ValidatorDecorator, self).__init__()

    def Clone(self):
        # Every validator must implement a Clone method.
        return self.toBeDecorated.Clone()
    
    def Validate(self, win):
        # Delegate this.
        return self.toBeDecorated.Validate(win)

    def TransferToWindow(self):
        # Delegate this.
        return self.toBeDecorated.TransferToWindow()

    def TransferFromWindow(self):
        # Delegate this.
        return self.toBeDecorated.TransferFromWindow()


class RequiredValidator(ValidatorDecorator):
    
    def __init__(self, toBeDecorated):
        super(RequiredValidator, self).__init__(toBeDecorated)
        # Now add customization to the validator.
        self.Bind(wx.EVT_SET_FOCUS, self.onClick)

    def Clone(self):
        # Every validator must implement a Clone method.
        return self.__class__(self.toBeDecorated)
    
    def Validate(self, win):
        print "self",self
        print "win",win
        print "win",win.GetTopLevelParent()
        #print "win",dir(win)
        textControl = self.GetWindow()
        value = textControl.GetValue()
            
        if not len(value):
            textControl.SetBackgroundColour('#FFFAC5')
            return False
        return super(RequiredValidator, self).Validate(win)       
        
    def onClick(self, event):
        control = self.GetWindow()
        control.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
        control.Refresh()
        event.Skip()
        return

class DigitValidator(ValidatorDecorator):
    def __init__(self, toBeDecorated):
        print "init digit"
        super(DigitValidator, self).__init__(toBeDecorated)
        # Digit-only validation specific behaviors:
        print "binding key event"
        self.Bind(wx.EVT_CHAR, self.onChar)
        self.Bind(wx.EVT_SET_FOCUS, self.onClick)

    def Clone(self):
        # Every validator must implement a Clone method.
        print "Clone"
        return DigitValidator(self.toBeDecorated)
    

    def Validate(self, win):
        print "Validating digit only!"
        try:
            textControl = self.GetWindow()
            value = textControl.GetValue()
        except AttributeError:
            return super(DigitValidator, self).Validate(win)
        if value.count('.') > 1:
            textControl.SetBackgroundColour('#FFFAC5')
            return False
        if value.count('-') > 1:
            textControl.SetBackgroundColour('#FFFAC5')
            return False
        for x in value:
            # If one of the characters is not a number
            # and not a "." or empty.
            if x not in string.digits and x != '.' and x != '-':
                textControl.SetBackgroundColour('#FFFAC5')
                return False

        if len(value) > 0:
            if True not in [False if value.find(i) < 0 else True for i in string.digits]:
                textControl.SetBackgroundColour('#FFFAC5')
                return False
        print "...digit OK"
        #return True
        return super(DigitValidator, self).Validate(win)      

    def onChar(self, event):
        print "char event"
        key = event.GetKeyCode()
        text = self.GetWindow().GetValue()

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
 
