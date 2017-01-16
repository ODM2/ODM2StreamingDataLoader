import wx
from src.wizard.controller.frmRequiredValidator \
    import RequiredValidator
from src.wizard.controller.frmRequiredComboValidator \
    import RequiredComboValidator

class AddNewUnitPanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 409,257 ), style = wx.TAB_TRAVERSAL )
                
        self.SetMinSize(wx.Size(420, 257))

        bSizer33 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields:" ), wx.VERTICAL )
        
        bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText30 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Units Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )
        bSizer34.Add( self.m_staticText30, 0, wx.ALL, 5 )
        
        
        bSizer34.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl26 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ), validator=RequiredValidator())
        bSizer34.Add( self.m_textCtrl26, 0, wx.ALL, 5 )
        
        
        sbSizer7.Add( bSizer34, 1, wx.EXPAND, 5 )
        
        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText31 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Units Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        bSizer35.Add( self.m_staticText31, 0, wx.ALL, 5 )
        
        
        bSizer35.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_comboBox13 = wx.ComboBox(sbSizer7.GetStaticBox(), wx.ID_ANY, u"Select Units Type", style=wx.CB_READONLY, validator=RequiredComboValidator())
        self.m_comboBox13.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer35.Add( self.m_comboBox13, 0, wx.ALL, 5 )
        
        
        sbSizer7.Add( bSizer35, 1, wx.EXPAND, 5 )
        
        bSizer341 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText301 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Units Abbreviation", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText301.Wrap( -1 )
        bSizer341.Add( self.m_staticText301, 0, wx.ALL, 5 )
        
        
        bSizer341.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl261 = wx.TextCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 280,-1 ),validator=RequiredValidator() )
        bSizer341.Add( self.m_textCtrl261, 0, wx.ALL, 5 )
        
        
        sbSizer7.Add( bSizer341, 1, wx.EXPAND, 5 )
        
        
        bSizer33.Add( sbSizer7, 1, wx.EXPAND, 5 )
        
        sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizer39 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText34 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Units Link", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )
        bSizer39.Add( self.m_staticText34, 0, wx.ALL, 5 )
        
        
        bSizer39.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl29 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl29.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer39.Add( self.m_textCtrl29, 0, wx.ALL, 5 )
        
        
        sbSizer8.Add( bSizer39, 1, wx.EXPAND, 5 )
        
        
        bSizer33.Add( sbSizer8, 1, wx.EXPAND, 5 )
        
        m_sdbSizer3 = wx.StdDialogButtonSizer()
        self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
        self.m_sdbSizer3Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
        m_sdbSizer3.Realize();
        
        bSizer33.Add( m_sdbSizer3, 1, wx.EXPAND, 5 )
        self.m_sdbSizer3OK.Bind(wx.EVT_BUTTON, self.onOK)        
        
        self.SetSizer( bSizer33 )
        self.Layout() 
    
    def __del__( self ):
        pass
