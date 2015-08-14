import wx

class AddNewResultsPanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 455,725 ), style = wx.TAB_TRAVERSAL )
                
        self.SetMinSize( wx.Size( 455,725 ) )
        
        bSizer174 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer29 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields:" ), wx.VERTICAL )
        
        bSizer274 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText244 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Result UUID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText244.Wrap( -1 )
        bSizer274.Add( self.m_staticText244, 0, wx.ALL, 5 )
        
        
        bSizer274.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl234 = wx.TextCtrl( sbSizer29.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl234.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer274.Add( self.m_textCtrl234, 0, wx.ALL, 5 )
        
        
        sbSizer29.Add( bSizer274, 1, wx.EXPAND, 5 )
        
        bSizer2741 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2441 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Value Count", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2441.Wrap( -1 )
        bSizer2741.Add( self.m_staticText2441, 0, wx.ALL, 5 )
        
        
        bSizer2741.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl2341 = wx.TextCtrl( sbSizer29.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl2341.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer2741.Add( self.m_textCtrl2341, 0, wx.ALL, 5 )
        
        
        sbSizer29.Add( bSizer2741, 1, wx.EXPAND, 5 )
        
        bSizer5321 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4221 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Feature Action ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4221.Wrap( -1 )
        bSizer5321.Add( self.m_staticText4221, 0, wx.ALL, 5 )
        
        
        bSizer5321.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox821Choices = []
        self.m_comboBox821 = wx.ComboBox( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Select Feature Action ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox821Choices, 0 )
        self.m_comboBox821.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer5321.Add( self.m_comboBox821, 0, wx.ALL, 5 )
        
        
        sbSizer29.Add( bSizer5321, 1, wx.EXPAND, 5 )
        
        bSizer53211 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42211 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Result Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42211.Wrap( -1 )
        bSizer53211.Add( self.m_staticText42211, 0, wx.ALL, 5 )
        
        
        bSizer53211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox8211Choices = []
        self.m_comboBox8211 = wx.ComboBox( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Select Result Type", wx.DefaultPosition, wx.DefaultSize, m_comboBox8211Choices, 0 )
        self.m_comboBox8211.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer53211.Add( self.m_comboBox8211, 0, wx.ALL, 5 )
        
        
        sbSizer29.Add( bSizer53211, 1, wx.EXPAND, 5 )
        
        bSizer53212 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42212 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Variable ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42212.Wrap( -1 )
        bSizer53212.Add( self.m_staticText42212, 0, wx.ALL, 5 )
        
        
        bSizer53212.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox8212Choices = []
        self.m_comboBox8212 = wx.ComboBox( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Select Variable ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox8212Choices, 0 )
        self.m_comboBox8212.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer53212.Add( self.m_comboBox8212, 0, wx.ALL, 5 )
        
        
        sbSizer29.Add( bSizer53212, 1, wx.EXPAND, 5 )
        
        bSizer53213 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42213 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Units ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42213.Wrap( -1 )
        bSizer53213.Add( self.m_staticText42213, 0, wx.ALL, 5 )
        
        
        bSizer53213.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox8213Choices = []
        self.m_comboBox8213 = wx.ComboBox( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Select Units ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox8213Choices, 0 )
        self.m_comboBox8213.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer53213.Add( self.m_comboBox8213, 0, wx.ALL, 5 )
        
        
        sbSizer29.Add( bSizer53213, 1, wx.EXPAND, 5 )
        
        bSizer53214 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42214 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Processing Level ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42214.Wrap( -1 )
        bSizer53214.Add( self.m_staticText42214, 0, wx.ALL, 5 )
        
        
        bSizer53214.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox8214Choices = []
        self.m_comboBox8214 = wx.ComboBox( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Select Processing Level ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox8214Choices, 0 )
        self.m_comboBox8214.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer53214.Add( self.m_comboBox8214, 0, wx.ALL, 5 )
        
        
        sbSizer29.Add( bSizer53214, 1, wx.EXPAND, 5 )
        
        bSizer53215 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42215 = wx.StaticText( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Sampled Medium", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42215.Wrap( -1 )
        bSizer53215.Add( self.m_staticText42215, 0, wx.ALL, 5 )
        
        
        bSizer53215.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox8215Choices = []
        self.m_comboBox8215 = wx.ComboBox( sbSizer29.GetStaticBox(), wx.ID_ANY, u"Select Sampled Medium", wx.DefaultPosition, wx.DefaultSize, m_comboBox8215Choices, 0 )
        self.m_comboBox8215.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer53215.Add( self.m_comboBox8215, 0, wx.ALL, 5 )
        
        
        sbSizer29.Add( bSizer53215, 1, wx.EXPAND, 5 )
        
        
        bSizer174.Add( sbSizer29, 1, wx.EXPAND, 5 )
        
        sbSizer30 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizer2742 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2442 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Result Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2442.Wrap( -1 )
        bSizer2742.Add( self.m_staticText2442, 0, wx.ALL, 5 )
        
        
        bSizer2742.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_datePicker5 = wx.DatePickerCtrl( sbSizer30.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
        self.m_datePicker5.SetMinSize( wx.Size( 149,-1 ) )
        
        bSizer2742.Add( self.m_datePicker5, 0, wx.ALL, 5 )
        
        self.m_staticText126 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText126.Wrap( -1 )
        bSizer2742.Add( self.m_staticText126, 0, wx.ALL, 5 )
        
        self.m_textCtrl83 = wx.TextCtrl( sbSizer30.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl83.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizer2742.Add( self.m_textCtrl83, 0, wx.ALL, 5 )
        
        
        sbSizer30.Add( bSizer2742, 1, wx.EXPAND, 5 )
        
        bSizer27421 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText24421 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Valid Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24421.Wrap( -1 )
        bSizer27421.Add( self.m_staticText24421, 0, wx.ALL, 5 )
        
        
        bSizer27421.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_datePicker51 = wx.DatePickerCtrl( sbSizer30.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
        self.m_datePicker51.SetMinSize( wx.Size( 149,-1 ) )
        
        bSizer27421.Add( self.m_datePicker51, 0, wx.ALL, 5 )
        
        self.m_staticText1261 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1261.Wrap( -1 )
        bSizer27421.Add( self.m_staticText1261, 0, wx.ALL, 5 )
        
        self.m_textCtrl831 = wx.TextCtrl( sbSizer30.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl831.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizer27421.Add( self.m_textCtrl831, 0, wx.ALL, 5 )
        
        
        sbSizer30.Add( bSizer27421, 1, wx.EXPAND, 5 )
        
        bSizer53216 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42216 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Taxonomical Classifier ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42216.Wrap( -1 )
        bSizer53216.Add( self.m_staticText42216, 0, wx.ALL, 5 )
        
        
        bSizer53216.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox8216Choices = []
        self.m_comboBox8216 = wx.ComboBox( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Select Taxonomical Classifier ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox8216Choices, 0 )
        self.m_comboBox8216.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer53216.Add( self.m_comboBox8216, 0, wx.ALL, 5 )
        
        
        sbSizer30.Add( bSizer53216, 1, wx.EXPAND, 5 )
        
        bSizer53217 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42217 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42217.Wrap( -1 )
        bSizer53217.Add( self.m_staticText42217, 0, wx.ALL, 5 )
        
        
        bSizer53217.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox8217Choices = []
        self.m_comboBox8217 = wx.ComboBox( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Select Status", wx.DefaultPosition, wx.DefaultSize, m_comboBox8217Choices, 0 )
        self.m_comboBox8217.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer53217.Add( self.m_comboBox8217, 0, wx.ALL, 5 )
        
        
        sbSizer30.Add( bSizer53217, 1, wx.EXPAND, 5 )
        
        bSizer27411 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText24411 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"X Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24411.Wrap( -1 )
        bSizer27411.Add( self.m_staticText24411, 0, wx.ALL, 5 )
        
        
        bSizer27411.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl23411 = wx.TextCtrl( sbSizer30.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl23411.SetMinSize( wx.Size( 99,-1 ) )
        
        bSizer27411.Add( self.m_textCtrl23411, 0, wx.ALL, 5 )
        
        self.m_staticText42218 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Units ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42218.Wrap( -1 )
        bSizer27411.Add( self.m_staticText42218, 0, wx.ALL, 5 )
        
        m_comboBox8218Choices = []
        self.m_comboBox8218 = wx.ComboBox( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Select Units ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox8218Choices, 0 )
        self.m_comboBox8218.SetMinSize( wx.Size( 115,-1 ) )
        
        bSizer27411.Add( self.m_comboBox8218, 0, wx.ALL, 5 )
        
        
        sbSizer30.Add( bSizer27411, 1, wx.EXPAND, 5 )
        
        bSizer27412 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText24412 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Y Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24412.Wrap( -1 )
        bSizer27412.Add( self.m_staticText24412, 0, wx.ALL, 5 )
        
        
        bSizer27412.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl23412 = wx.TextCtrl( sbSizer30.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl23412.SetMinSize( wx.Size( 99,-1 ) )
        
        bSizer27412.Add( self.m_textCtrl23412, 0, wx.ALL, 5 )
        
        self.m_staticText42219 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Units ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42219.Wrap( -1 )
        bSizer27412.Add( self.m_staticText42219, 0, wx.ALL, 5 )
        
        m_comboBox8219Choices = []
        self.m_comboBox8219 = wx.ComboBox( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Select Units ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox8219Choices, 0 )
        self.m_comboBox8219.SetMinSize( wx.Size( 115,-1 ) )
        
        bSizer27412.Add( self.m_comboBox8219, 0, wx.ALL, 5 )
        
        
        sbSizer30.Add( bSizer27412, 1, wx.EXPAND, 5 )
        
        bSizer27413 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText24413 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Z Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24413.Wrap( -1 )
        bSizer27413.Add( self.m_staticText24413, 0, wx.ALL, 5 )
        
        
        bSizer27413.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl23413 = wx.TextCtrl( sbSizer30.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl23413.SetMinSize( wx.Size( 99,-1 ) )
        
        bSizer27413.Add( self.m_textCtrl23413, 0, wx.ALL, 5 )
        
        self.m_staticText422110 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Units ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText422110.Wrap( -1 )
        bSizer27413.Add( self.m_staticText422110, 0, wx.ALL, 5 )
        
        m_comboBox82110Choices = []
        self.m_comboBox82110 = wx.ComboBox( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Select Units ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox82110Choices, 0 )
        self.m_comboBox82110.SetMinSize( wx.Size( 115,-1 ) )
        
        bSizer27413.Add( self.m_comboBox82110, 0, wx.ALL, 5 )
        
        
        sbSizer30.Add( bSizer27413, 1, wx.EXPAND, 5 )
        
        bSizer274131 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText244131 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Intended Time Spacing", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText244131.Wrap( -1 )
        bSizer274131.Add( self.m_staticText244131, 0, wx.ALL, 5 )
        
        
        bSizer274131.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl234131 = wx.TextCtrl( sbSizer30.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl234131.SetMinSize( wx.Size( 99,-1 ) )
        
        bSizer274131.Add( self.m_textCtrl234131, 0, wx.ALL, 5 )
        
        self.m_staticText4221101 = wx.StaticText( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Units ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4221101.Wrap( -1 )
        bSizer274131.Add( self.m_staticText4221101, 0, wx.ALL, 5 )
        
        m_comboBox821101Choices = []
        self.m_comboBox821101 = wx.ComboBox( sbSizer30.GetStaticBox(), wx.ID_ANY, u"Select Units ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox821101Choices, 0 )
        self.m_comboBox821101.SetMinSize( wx.Size( 115,-1 ) )
        
        bSizer274131.Add( self.m_comboBox821101, 0, wx.ALL, 5 )
        
        
        sbSizer30.Add( bSizer274131, 1, wx.EXPAND, 5 )
        
        
        bSizer174.Add( sbSizer30, 1, wx.EXPAND, 5 )
        
        m_sdbSizer13 = wx.StdDialogButtonSizer()
        self.m_sdbSizer13OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer13.AddButton( self.m_sdbSizer13OK )
        self.m_sdbSizer13Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer13.AddButton( self.m_sdbSizer13Cancel )
        m_sdbSizer13.Realize();
        
        bSizer174.Add( m_sdbSizer13, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer174 )
        self.Layout()

    def __del__( self ):
        pass
