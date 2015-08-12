import wx
import os

os.environ['http_proxy'] = ''
import urllib2

class URLValidator(wx.PyValidator):
    '''
    This validator class is used to ensure that a file path
    entered into a text control actually exists.

    '''
    def __init__(self):
        super(URLValidator, self).__init__()

    def Clone(self):
        '''
        Every validator must implement a Clone method.
        '''
        return URLValidator()
    
    def Validate(self, win):
        text_ctrl = self.GetWindow()
        url = str(text_ctrl.GetValue()).lstrip(' ')
        error_message = 'Enter a valid URL data file path.'

        # Check if text is empty.
        if len(url):
            # http://vocabulary.odm2.org/api/v1/actiontype/cruise/?format=csv
            # Add an http:// prefix if the user didn't already.
            if url.startswith('http://') == False:
                url = 'http://' + url
            try:
                urllib2.urlopen(url)
                text_ctrl.SetBackgroundColour(\
                    wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                text_ctrl.Refresh()
                return True
            except urllib2.URLError as e:
                print e
                error_message = 'Unable to connect to the provided URL!'
        
        text_ctrl.SetBackgroundColour('pink')
        wx.MessageBox(error_message, 'Form Error')
        text_ctrl.SetFocus()
        text_ctrl.Refresh()
        return False

    def TransferToWindow(self):
        return True
    
    def TransferFromWindow(self):
        return True

