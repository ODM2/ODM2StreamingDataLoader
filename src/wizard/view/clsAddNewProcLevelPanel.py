import wx
from src.wizard.controller.frmRequiredValidator \
    import RequiredValidator

class AddNewProcLevelPanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 437,241 ), style = wx.TAB_TRAVERSAL )
                
        self.SetMinSize( wx.Size( 450,285 ) )
        
        bSizer40 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields:" ), wx.VERTICAL )
        
        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText35 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Processing Level Code", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText35.Wrap( -1 )
        bSizer41.Add( self.m_staticText35, 0, wx.ALL, 5 )
        
        
        bSizer41.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl30 = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, validator=RequiredValidator() )
        self.m_textCtrl30.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer41.Add( self.m_textCtrl30, 0, wx.ALL, 5 )
        
        
        sbSizer9.Add( bSizer41, 0, wx.EXPAND, 5 )
        
        
        bSizer40.Add( sbSizer9, 0, wx.EXPAND, 5 )
        
        sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText36 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Definition", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText36.Wrap( -1 )
        bSizer42.Add( self.m_staticText36, 0, wx.ALL, 5 )
        
        
        bSizer42.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl31 = wx.TextCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(280, 70), wx.TE_MULTILINE )
        #self.m_textCtrl31.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer42.Add( self.m_textCtrl31, 0, wx.ALL, 5 )
        
        
        sbSizer10.Add( bSizer42, 0, wx.EXPAND, 5 )
        
        bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText37 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Explanation", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText37.Wrap( -1 )
        bSizer43.Add( self.m_staticText37, 0, wx.ALL, 5 )
        
        
        bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl32 = wx.TextCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(280, 70), wx.TE_MULTILINE )
        #self.m_textCtrl32.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer43.Add( self.m_textCtrl32, 0, wx.ALL, 5 )
        
        
        sbSizer10.Add( bSizer43, 0, wx.EXPAND, 5 )
        
        
        bSizer40.Add( sbSizer10, 0, wx.EXPAND, 5 )
        
        m_sdbSizer4 = wx.StdDialogButtonSizer()
        self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
        self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
        m_sdbSizer4.Realize();
        
        bSizer40.Add( m_sdbSizer4, 1, wx.EXPAND, 5 )
        self.m_sdbSizer4OK.Bind(wx.EVT_BUTTON, self.onOK) 
        
        self.SetSizer( bSizer40 )
        self.Layout()
    
    def __del__( self ):
        pass
