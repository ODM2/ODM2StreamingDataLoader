import wx

class AddNewMethodPanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 409,452 ), style = wx.TAB_TRAVERSAL )
                
        self.SetMinSize(wx.Size(409, 452))
        bSizer44 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fileds:" ), wx.VERTICAL )
        
        bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText38 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Method Code", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText38.Wrap( -1 )
        bSizer45.Add( self.m_staticText38, 0, wx.ALL, 5 )
        
        
        bSizer45.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl33 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl33.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer45.Add( self.m_textCtrl33, 0, wx.ALL, 5 )
        
        
        sbSizer12.Add( bSizer45, 1, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText39 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Method Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText39.Wrap( -1 )
        bSizer46.Add( self.m_staticText39, 0, wx.ALL, 5 )
        
        
        bSizer46.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl331 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl331.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer46.Add( self.m_textCtrl331, 0, wx.ALL, 5 )
        
        
        sbSizer12.Add( bSizer46, 1, wx.EXPAND, 5 )
        
        bSizer47 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText40 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Method Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText40.Wrap( -1 )
        bSizer47.Add( self.m_staticText40, 0, wx.ALL, 5 )
        
        
        bSizer47.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox14Choices = []
        self.m_comboBox14 = wx.ComboBox( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Select Method Type", wx.DefaultPosition, wx.DefaultSize, m_comboBox14Choices, 0 )
        self.m_comboBox14.SetMinSize( wx.Size( 230,-1 ) )
        
        bSizer47.Add( self.m_comboBox14, 0, wx.ALL, 5 )
        
        self.m_button41 = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 40,27 ), 0 )
        self.m_button41.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer47.Add( self.m_button41, 0, wx.ALL, 5 )
        
        
        sbSizer12.Add( bSizer47, 1, wx.EXPAND, 5 )
        
        
        bSizer44.Add( sbSizer12, 1, wx.EXPAND, 5 )
        
        sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizer48 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText41 = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Organization ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText41.Wrap( -1 )
        bSizer48.Add( self.m_staticText41, 0, wx.ALL, 5 )
        
        
        bSizer48.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox141Choices = []
        self.m_comboBox141 = wx.ComboBox( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Select Organization ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox141Choices, 0 )
        self.m_comboBox141.SetMinSize( wx.Size( 230,-1 ) )
        
        bSizer48.Add( self.m_comboBox141, 0, wx.ALL, 5 )
        
        self.m_button411 = wx.Button( sbSizer13.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 40,27 ), 0 )
        self.m_button411.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer48.Add( self.m_button411, 0, wx.ALL, 5 )
        
        
        sbSizer13.Add( bSizer48, 1, wx.EXPAND, 5 )
        
        bSizer49 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42 = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Method Link", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42.Wrap( -1 )
        bSizer49.Add( self.m_staticText42, 0, wx.ALL, 5 )
        
        
        bSizer49.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl37 = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl37.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer49.Add( self.m_textCtrl37, 0, wx.ALL, 5 )
        
        
        sbSizer13.Add( bSizer49, 1, wx.EXPAND, 5 )
        
        bSizer50 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText43 = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText43.Wrap( -1 )
        bSizer50.Add( self.m_staticText43, 0, wx.ALL, 5 )
        
        
        bSizer50.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl38 = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_textCtrl38.SetMinSize( wx.Size( 280,70 ) )
        
        bSizer50.Add( self.m_textCtrl38, 0, wx.ALL, 5 )
        
        
        sbSizer13.Add( bSizer50, 1, wx.EXPAND, 5 )
        
        
        bSizer44.Add( sbSizer13, 1, wx.EXPAND, 5 )
        
        m_sdbSizer5 = wx.StdDialogButtonSizer()
        self.m_sdbSizer5OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer5.AddButton( self.m_sdbSizer5OK )
        self.m_sdbSizer5Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer5.AddButton( self.m_sdbSizer5Cancel )
        m_sdbSizer5.Realize();
        
        bSizer44.Add( m_sdbSizer5, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer44 )
        self.Layout() 

    
    def __del__( self ):
        pass
