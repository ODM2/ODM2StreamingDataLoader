import wx

class AddNewSourcePanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 402,528 ), style = wx.TAB_TRAVERSAL )
                
        self.SetMinSize( wx.Size( 402,528 ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields:" ), wx.VERTICAL )
        
        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText12 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Organization", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer18.Add( self.m_staticText12, 0, wx.ALL, 5 )
        
        
        bSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl3 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl3.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer18.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer18, 1, wx.EXPAND, 5 )
        
        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText14 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        bSizer19.Add( self.m_staticText14, 0, wx.ALL, 5 )
        
        
        bSizer19.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl31 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl31.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer19.Add( self.m_textCtrl31, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer19, 1, wx.EXPAND, 5 )
        
        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText15 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Citation", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        bSizer20.Add( self.m_staticText15, 0, wx.ALL, 5 )
        
        
        bSizer20.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl32 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl32.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer20.Add( self.m_textCtrl32, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )
        
        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText16 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Contact Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        bSizer21.Add( self.m_staticText16, 0, wx.ALL, 5 )
        
        
        bSizer21.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl33 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl33.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer21.Add( self.m_textCtrl33, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer21, 1, wx.EXPAND, 5 )
        
        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText17 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Contact Address", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        bSizer22.Add( self.m_staticText17, 0, wx.ALL, 5 )
        
        
        bSizer22.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl34 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl34.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer22.Add( self.m_textCtrl34, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer22, 1, wx.EXPAND, 5 )
        
        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText18 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Contact Phone", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        bSizer23.Add( self.m_staticText18, 0, wx.ALL, 5 )
        
        
        bSizer23.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl35 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl35.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer23.Add( self.m_textCtrl35, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer23, 1, wx.EXPAND, 5 )
        
        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText19 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Contact Email", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        bSizer24.Add( self.m_staticText19, 0, wx.ALL, 5 )
        
        
        bSizer24.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl36 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl36.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer24.Add( self.m_textCtrl36, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer24, 1, wx.EXPAND, 5 )
        
        bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText20 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"State", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        bSizer25.Add( self.m_staticText20, 0, wx.ALL, 5 )
        
        
        bSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl37 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl37.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer25.Add( self.m_textCtrl37, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer25, 1, wx.EXPAND, 5 )
        
        bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText21 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"City", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        bSizer28.Add( self.m_staticText21, 0, wx.ALL, 5 )
        
        
        bSizer28.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl20 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl20.SetMinSize( wx.Size( 142,-1 ) )
        
        bSizer28.Add( self.m_textCtrl20, 0, wx.ALL, 5 )
        
        self.m_staticText22 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Zip", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )
        bSizer28.Add( self.m_staticText22, 0, wx.ALL, 5 )
        
        self.m_textCtrl21 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl21.SetMinSize( wx.Size( 100,-1 ) )
        
        bSizer28.Add( self.m_textCtrl21, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer28, 1, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer8.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox1Choices = []
        self.m_comboBox1 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"ISO Metadata", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
        self.m_comboBox1.SetMinSize( wx.Size( 230,-1 ) )
        
        bSizer8.Add( self.m_comboBox1, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 40,27 ), 0 )
        self.m_button2.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer8.Add( self.m_button2, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( sbSizer1, 1, 0, 5 )
        
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText23 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Link", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )
        bSizer26.Add( self.m_staticText23, 0, wx.ALL, 5 )
        
        
        bSizer26.AddSpacer( ( 70, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl22 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl22.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer26.Add( self.m_textCtrl22, 0, wx.ALL, 5 )
        
        
        sbSizer2.Add( bSizer26, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( sbSizer2, 1, 0, 5 )
        
        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize();
        
        bSizer1.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()    
    
    def __del__( self ):
        pass
