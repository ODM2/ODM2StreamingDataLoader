import wx

from ObjectListView import ObjectListView, ColumnDefn

class Test():
    def __init__(self, name, org):
        self.name = name
        self.org = org

class AddNewActionsPanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 414,566 ), style = wx.TAB_TRAVERSAL )
                
        self.SetMinSize( wx.Size( 414,400 ) )
        
        bSizer80 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields:" ), wx.VERTICAL )
        
        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText31 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Action Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        bSizer35.Add( self.m_staticText31, 0, wx.ALL, 5 )
        
        
        bSizer35.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox13Choices = []
        self.m_comboBox13 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Select Action Type", wx.DefaultPosition, wx.DefaultSize, m_comboBox13Choices, 0 )
        self.m_comboBox13.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer35.Add( self.m_comboBox13, 0, wx.ALL, 5 )
        
        
        sbSizer22.Add( bSizer35, 1, wx.EXPAND, 5 )
        
        bSizer354 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText314 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Method", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText314.Wrap( -1 )
        bSizer354.Add( self.m_staticText314, 0, wx.ALL, 5 )
        
        
        bSizer354.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox134Choices = []
        self.m_comboBox134 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Select Method", wx.DefaultPosition, wx.DefaultSize, m_comboBox134Choices, 0 )
        self.m_comboBox134.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer354.Add( self.m_comboBox134, 0, wx.ALL, 5 )
        
        
        sbSizer22.Add( bSizer354, 1, wx.EXPAND, 5 )
        
        #bSizer351 = wx.BoxSizer( wx.HORIZONTAL )
        
        #self.m_staticText311 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Method Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_staticText311.Wrap( -1 )
        #bSizer351.Add( self.m_staticText311, 0, wx.ALL, 5 )
        
        
        #bSizer351.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        #m_comboBox131Choices = []
        #self.m_comboBox131 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Select Method Type", wx.DefaultPosition, wx.DefaultSize, m_comboBox131Choices, 0 )
        #self.m_comboBox131.SetMinSize( wx.Size( 280,-1 ) )
        
        #bSizer351.Add( self.m_comboBox131, 0, wx.ALL, 5 )
        
        
        #sbSizer22.Add( bSizer351, 1, wx.EXPAND, 5 )
        
        #bSizer352 = wx.BoxSizer( wx.HORIZONTAL )
        
        #self.m_staticText312 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Bridge ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_staticText312.Wrap( -1 )
        #bSizer352.Add( self.m_staticText312, 0, wx.ALL, 5 )
        
        
        #bSizer352.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        #m_comboBox132Choices = []
        #self.m_comboBox132 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Select Bridge ID", wx.DefaultPosition, wx.DefaultSize, m_comboBox132Choices, 0 )
        #self.m_comboBox132.SetMinSize( wx.Size( 280,-1 ) )
        
        #bSizer352.Add( self.m_comboBox132, 0, wx.ALL, 5 )
        
        
        #sbSizer22.Add( bSizer352, 1, wx.EXPAND, 5 )
        
        bSizer3541 = wx.BoxSizer( wx.VERTICAL )
        
        #self.m_staticText3141 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Affiliation", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_staticText3141.Wrap( -1 )
        #bSizer3541.Add( self.m_staticText3141, 0, wx.ALL, 5 )
        
        
        #bSizer3541.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        #m_comboBox1341Choices = []
        #self.m_comboBox1341 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Select Affiliation", wx.DefaultPosition, wx.DefaultSize, m_comboBox1341Choices, 0 )
        #self.m_comboBox1341.SetMinSize( wx.Size( 280,-1 ) )
        
        #bSizer3541.Add( self.m_comboBox1341, 0, wx.ALL, 5 )
        
        
        #sbSizer22.Add( bSizer3541, 1, wx.EXPAND, 5 )
        self.affList = ObjectListView(sbSizer22.GetStaticBox(),
            wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, 100),
            style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.affList.cellEditMode = self.affList.CELLEDIT_DOUBLECLICK
        isLeadColumn = ColumnDefn(title='Lead', valueGetter='', align='centre', width=50)
        self.affList.SetColumns([
            ColumnDefn(title='Name', valueGetter='name', align='left', width=100, isEditable=True),
            ColumnDefn('Organization', 'left', -1,'org'),
            isLeadColumn,
        ])
        self.affList.InstallCheckStateColumn(isLeadColumn)
        self.affList.AddObject(Test("",
            ""))
        
        self.affList.SetEmptyListMsg("Affiliations")
        bSizer3541.Add(self.affList, 1, wx.ALL|wx.EXPAND, 5)
        sbSizer22.Add( bSizer3541, 1, wx.EXPAND, 5 )

        #bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
        
        #self.m_staticText24 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Is Action Lead", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_staticText24.Wrap( -1 )
        #bSizer27.Add( self.m_staticText24, 0, wx.ALL, 5 )
        
        
        #bSizer27.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        #self.m_radioBtn3 = wx.RadioButton( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Yes", wx.DefaultPosition, wx.DefaultSize, 0 )
        #bSizer27.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
        
        #self.m_radioBtn4 = wx.RadioButton( sbSizer22.GetStaticBox(), wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, 0 )
        #bSizer27.Add( self.m_radioBtn4, 0, wx.ALL, 5 )
        
        
        #sbSizer22.Add( bSizer27, 1, wx.EXPAND, 5 )
        
        bSizer271 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText241 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Begin Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText241.Wrap( -1 )
        bSizer271.Add( self.m_staticText241, 0, wx.ALL, 5 )
        
        
        bSizer271.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_datePicker5 = wx.DatePickerCtrl( sbSizer22.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
        self.m_datePicker5.SetMinSize( wx.Size( 149,-1 ) )
        
        bSizer271.Add( self.m_datePicker5, 0, wx.ALL, 5 )
        
        self.m_staticText68 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText68.Wrap( -1 )
        bSizer271.Add( self.m_staticText68, 0, wx.ALL, 5 )
        
        self.m_textCtrl46 = wx.TextCtrl( sbSizer22.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl46.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizer271.Add( self.m_textCtrl46, 0, wx.ALL, 5 )
        
        
        sbSizer22.Add( bSizer271, 1, wx.EXPAND, 5 )
        
        
        bSizer80.Add( sbSizer22, 1, wx.EXPAND, 5 )
        
        sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizer2711 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2411 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"End Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2411.Wrap( -1 )
        bSizer2711.Add( self.m_staticText2411, 0, wx.ALL, 5 )
        
        
        bSizer2711.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_datePicker51 = wx.DatePickerCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
        self.m_datePicker51.SetMinSize( wx.Size( 149,-1 ) )
        
        bSizer2711.Add( self.m_datePicker51, 0, wx.ALL, 5 )
        
        self.m_staticText681 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText681.Wrap( -1 )
        bSizer2711.Add( self.m_staticText681, 0, wx.ALL, 5 )
        
        self.m_textCtrl461 = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl461.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizer2711.Add( self.m_textCtrl461, 0, wx.ALL, 5 )
        
        
        sbSizer23.Add( bSizer2711, 1, wx.EXPAND, 5 )
        
        bSizer274 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText244 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Action File Link", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText244.Wrap( -1 )
        bSizer274.Add( self.m_staticText244, 0, wx.ALL, 5 )
        
        
        bSizer274.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl234 = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl234.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer274.Add( self.m_textCtrl234, 0, wx.ALL, 5 )
        
        
        sbSizer23.Add( bSizer274, 1, wx.EXPAND, 5 )
        
        bSizer272 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText242 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u" Action Description", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText242.Wrap( -1 )
        bSizer272.Add( self.m_staticText242, 0, wx.ALL, 5 )
        
        
        bSizer272.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl232 = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_textCtrl232.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer272.Add( self.m_textCtrl232, 0, wx.ALL, 5 )
        
        
        sbSizer23.Add( bSizer272, 1, wx.EXPAND, 5 )
        
        bSizer273 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText243 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Role Description", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText243.Wrap( -1 )
        bSizer273.Add( self.m_staticText243, 0, wx.ALL, 5 )
        
        
        bSizer273.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl233 = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_textCtrl233.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer273.Add( self.m_textCtrl233, 0, wx.ALL, 5 )
        
        
        sbSizer23.Add( bSizer273, 1, wx.EXPAND, 5 )
        
        
        bSizer80.Add( sbSizer23, 1, wx.EXPAND, 5 )
        
        m_sdbSizer10 = wx.StdDialogButtonSizer()
        self.m_sdbSizer10OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer10.AddButton( self.m_sdbSizer10OK )
        self.m_sdbSizer10Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer10.AddButton( self.m_sdbSizer10Cancel )
        m_sdbSizer10.Realize();
        
        bSizer80.Add( m_sdbSizer10, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer80 )
        self.Layout() 
    
    def __del__( self ):
        pass
