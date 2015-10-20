import string
import wx

class CustomValidator(wx.PyValidator):
    '''
    This is a basic validator that inherits from
    PyValidator.
    '''
    def __init__(self):
        super(CustomValidator, self).__init__()
    
    def Clone(self):
        # Every validator must implement a Clone method.
        return CustomValidator()
    
    def Validate(self, win):
        return True

    def TransferToWindow(self):
        return True
    def TransferFromWindow(self):
        return True

