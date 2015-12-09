import wx

from src.wizard.controller.frmRequiredValidator \
    import RequiredValidator
from src.wizard.controller.frmRequiredComboValidator \
    import RequiredComboValidator

class PersonPanelView(wx.Panel):
    def __init__( self, parent):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 542,300 ), style = wx.TAB_TRAVERSAL )
        
        self.SetMinSize( wx.Size( 450,300 ) )
        
        bSizer80 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Person:" ), wx.VERTICAL )
        
        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText31 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Existing person", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        bSizer35.Add( self.m_staticText31, 0, wx.ALL, 5 )
        
        
        bSizer35.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox13Choices = []
        self.m_comboBox13 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, m_comboBox13Choices, 0 )
        self.m_comboBox13.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer35.Add( self.m_comboBox13, 0, wx.ALL, 5 )
        
        
        sbSizer22.Add( bSizer35, 0, wx.EXPAND, 10 ) # Denver

        newPersonSizer = wx.BoxSizer( wx.VERTICAL )
        firstMiddleSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        lblFirst = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"First Name:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        firstMiddleSizer.Add(lblFirst, 0, wx.ALL, 5)
        
        firstMiddleSizer.AddSpacer((0,0), 1, wx.EXPAND, 5)

        self.textFirst = wx.TextCtrl(sbSizer22.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(100,-1), validator=RequiredValidator())
        firstMiddleSizer.Add(self.textFirst, 0, wx.ALL, 5)
        
        lblMiddle = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Middle:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        firstMiddleSizer.Add(lblMiddle, 0, wx.ALL, 5)
        
        self.textMiddle = wx.TextCtrl(sbSizer22.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(100,-1), 0)
        firstMiddleSizer.Add(self.textMiddle, 0, wx.ALL, 5)
        
        newPersonSizer.Add(firstMiddleSizer, 0, wx.EXPAND, 5) #denver

        lastSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        lblLast = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Last Name:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        lastSizer.Add(lblLast, 0, wx.ALL, 5)
        
        lastSizer.AddSpacer((0,0), 1, wx.EXPAND, 5)

        self.textLast = wx.TextCtrl(sbSizer22.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), validator=RequiredValidator())
        lastSizer.Add(self.textLast, 0, wx.ALL, 5)
        
        newPersonSizer.Add(lastSizer, 0, wx.EXPAND, 5) # Denver

        sbSizer22.Add(newPersonSizer, 0, wx.EXPAND, 5) # Denver
        
        bSizer80.Add( sbSizer22, 0, wx.EXPAND, 5 ) # Denver
        
        self.SetSizer( bSizer80 )
        self.Layout()
        




