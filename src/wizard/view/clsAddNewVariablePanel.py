import wx
from src.wizard.controller.frmRequiredComboValidator \
    import RequiredComboValidator
from src.wizard.controller.frmRequiredValidator \
    import RequiredValidator
from src.wizard.controller.frmDigitOnly \
    import DigitValidator

class AddNewVariablePanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 407,336 ), style = wx.TAB_TRAVERSAL )
                
        self.SetMinSize( wx.Size( 415,356 ) )
        
        bSizer13 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields:" ), wx.VERTICAL )
        
        bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText24 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Variable Code", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )
        bSizer27.Add( self.m_staticText24, 0, wx.ALL, 5 )
        
        
        bSizer27.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl23 = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,validator=RequiredValidator())
        self.m_textCtrl23.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer27.Add( self.m_textCtrl23, 0, wx.ALL, 5 )
        
        
        sbSizer9.Add( bSizer27, 0, wx.EXPAND, 5 )
        
        bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText25 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Variable Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )
        bSizer28.Add( self.m_staticText25, 0, wx.ALL, 5 )
        
        
        bSizer28.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox4Choices = []
        self.m_comboBox4 = wx.ComboBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Select Variable Name", wx.DefaultPosition, wx.DefaultSize, m_comboBox4Choices, wx.CB_READONLY, validator=RequiredComboValidator() )
        self.m_comboBox4.SetMinSize( wx.Size( 280,-1 ) )
        bSizer28.Add( self.m_comboBox4, 0, wx.ALL, 5 )
        
        sbSizer9.Add( bSizer28, 0, wx.EXPAND, 5 )
        
        bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText29 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Variable Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )
        bSizer32.Add( self.m_staticText29, 0, wx.ALL, 5 )
        
        
        bSizer32.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox12Choices = []
        self.m_comboBox12 = wx.ComboBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Select Variable Type", wx.DefaultPosition, wx.DefaultSize, m_comboBox12Choices, wx.CB_READONLY , validator=RequiredComboValidator())
        self.m_comboBox12.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer32.Add( self.m_comboBox12, 0, wx.ALL, 5 )
        
        
        sbSizer9.Add( bSizer32, 0, wx.EXPAND, 5 )
        
        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText21 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"No Data Value", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        bSizer20.Add( self.m_staticText21, 0, wx.ALL, 5 )
        
        
        bSizer20.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl15 = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, u"-9999", wx.DefaultPosition, wx.DefaultSize, validator=DigitValidator())
        self.m_textCtrl15.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer20.Add( self.m_textCtrl15, 0, wx.ALL, 5 )
        
        
        sbSizer9.Add( bSizer20, 0, wx.EXPAND, 5 )
        
        
        bSizer13.Add( sbSizer9, 0, wx.EXPAND, 5 )
        
        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText26 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Speciation", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )
        bSizer29.Add( self.m_staticText26, 0, wx.ALL, 5 )
        
        
        bSizer29.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox2Choices = []
        self.m_comboBox2 = wx.ComboBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Select Speciation", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, wx.CB_READONLY )
        self.m_comboBox2.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer29.Add( self.m_comboBox2, 0, wx.ALL, 5 )
        
        #self.m_button42 = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 40,27 ), 0 )
        #self.m_button42.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
        
        #bSizer29.Add( self.m_button42, 0, wx.ALL, 5 )
        
        
        sbSizer6.Add( bSizer29, 0, wx.EXPAND, 5 )
        
        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText28 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Definition", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )
        bSizer31.Add( self.m_staticText28, 0, wx.ALL, 5 )
        
        
        bSizer31.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl24 = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(280, 70), wx.TE_MULTILINE )
        #self.m_textCtrl24.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer31.Add( self.m_textCtrl24, 0, wx.ALL, 5 )
        
        
        sbSizer6.Add( bSizer31, 0, wx.EXPAND, 5 )
        
        
        bSizer13.Add( sbSizer6, 0, wx.EXPAND, 5 )
        
        m_sdbSizer2 = wx.StdDialogButtonSizer()
        self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
        self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
        m_sdbSizer2.Realize();
        
        bSizer13.Add( m_sdbSizer2, 1, wx.EXPAND, 5 )
        self.m_sdbSizer2OK.Bind(wx.EVT_BUTTON, self.onOK)        
        
        self.SetSizer( bSizer13 )
        self.Layout() 
    
    def __del__( self ):
        pass
