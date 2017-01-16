import wx
from src.wizard.controller.frmRequiredComboValidator \
    import RequiredComboValidator
from src.wizard.controller.frmRequiredValidator \
    import RequiredValidator
from src.wizard.controller.frmDigitOnly \
    import DigitValidator
from ObjectListView import ObjectListView, ColumnDefn

import wx.lib.masked as masked

class Test():
    def __init__(self, name, org, orgId):
        self.name = name
        self.org = org
        self.orgId = orgId

class AffiliationsList(ObjectListView):
    def __init__(self, *args, **kwargs):
        ObjectListView.__init__(self, *args, **kwargs)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)
        #self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.onDeselect)
        #self.Bind(wx.EVT_LEFT_DOWN, self.onClick)
        self.selected = set()
        self.selectedItems = []
        self.lastSelected = -1
        self.deleting = -1

class AddNewActionsPanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 414,650 ), style = wx.TAB_TRAVERSAL )
                
        self.SetMinSize( wx.Size( 414,675 ) )
        
        bSizer80 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields" ), wx.VERTICAL )
        
        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText31 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Action Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        bSizer35.Add( self.m_staticText31, 0, wx.ALL, 5 )
        
        
        bSizer35.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox13Choices = []
        self.m_comboBox13 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Select Action Type", wx.DefaultPosition, wx.DefaultSize, m_comboBox13Choices, validator=RequiredComboValidator())
        self.m_comboBox13.SetMinSize( wx.Size( 280,-1 ) )

        self.m_comboBox13.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.on_show_combo)
        self.m_comboBox13.Bind(wx.EVT_COMBOBOX_CLOSEUP, self.on_hide_combo)
        
        bSizer35.Add( self.m_comboBox13, 0, wx.ALL, 5 )
        sbSizer22.Add( bSizer35, 0, wx.EXPAND, 5 )
        
        bSizer354 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText314 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Method", wx.DefaultPosition, wx.DefaultSize,0)
        self.m_staticText314.Wrap( -1 )
        bSizer354.Add( self.m_staticText314, 0, wx.ALL, 5 )
        
        
        bSizer354.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox134Choices = []
        self.m_comboBox134 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Select Method", wx.DefaultPosition, wx.DefaultSize, m_comboBox134Choices, validator=RequiredComboValidator() )
        self.m_comboBox134.SetMinSize( wx.Size( 230,-1 ) )
        
        bSizer354.Add( self.m_comboBox134, 0, wx.ALL, 5 )
        
        self.btnNewMethod = wx.Button(sbSizer22.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size(40,27), 0)
        self.btnNewMethod.SetFont(wx.Font(15,70,90,92,False,wx.EmptyString))
        bSizer354.Add(self.btnNewMethod, 0, wx.ALL, 5)
        
        sbSizer22.Add( bSizer354, 0, wx.EXPAND, 5 )
        
        
        bSizer3541 = wx.BoxSizer( wx.VERTICAL )
        affSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText3141 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Affiliations", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_staticText3141.Wrap( -1 )
        affSizer.Add(self.m_staticText3141, 0, wx.ALL, 5)
        
        
        self.m_b = wx.Button( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Create Affiliation", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_b.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
        
        affSizer.Add(self.m_b, 0, wx.ALL, 5)
        bSizer3541.Add( affSizer, 0, wx.ALL, 5 )
        
        #sbSizer22.Add( bSizer3541, 1, wx.EXPAND, 5 )
        self.affList = AffiliationsList(sbSizer22.GetStaticBox(),
            wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1, 150),
            style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        #self.affList.cellEditMode = self.affList.CELLEDIT_DOUBLECLICK
        isLeadColumn = ColumnDefn(title='Lead', valueGetter='', align='centre', width=50)
        self.affList.SetColumns([
            isLeadColumn,
            ColumnDefn(title='Person', valueGetter='name', align='left', width=100),
            ColumnDefn('Organization', 'left', 500,'organization'),
        ])
        self.affList.InstallCheckStateColumn(isLeadColumn)
        #self.affList.AddObject(Test("","",
        #    ""))
        
        self.affList.SetEmptyListMsg("Affiliations")
        bSizer3541.Add(self.affList, 1, wx.ALL|wx.EXPAND, 5)
        sbSizer22.Add( bSizer3541, 1, wx.EXPAND, 5 )

        
        bSizer271 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText241 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Begin Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText241.Wrap( -1 )
        bSizer271.Add( self.m_staticText241, 0, wx.ALL, 5 )
        
        
        bSizer271.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_datePicker5 = wx.DatePickerCtrl( sbSizer22.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
        self.m_datePicker5.SetMinSize( wx.Size( 149,-1 ) )
        
        bSizer271.Add( self.m_datePicker5, 0, wx.ALL, 5 )
        
        self.m_timePicker1 = masked.TimeCtrl(\
            sbSizer22.GetStaticBox(), wx.ID_ANY,
            '00:00:00', wx.DefaultPosition,
            wx.DefaultSize, wx.TE_PROCESS_TAB,
            validator=wx.DefaultValidator,
            name = 'time',
            format = 'HHMMSS')
    
        h = self.m_timePicker1.GetSize().height
    
        self.spinner = wx.SpinButton(\
            sbSizer22.GetStaticBox(), wx.ID_ANY,
            wx.DefaultPosition, (-1,h), wx.SP_VERTICAL)
        self.spinner.SetValue(0)

        self.m_timePicker1.BindSpinButton(self.spinner)
   
        self.m_timePicker1.SetMinSize( wx.Size( 100,-1 ) )

        bSizer271.Add( self.m_timePicker1, 0, wx.TOP, 5 )
        bSizer271.Add( self.spinner, 0, wx.TOP, 5 )
        
        
        sbSizer22.Add( bSizer271, 0, wx.EXPAND, 5 )
        
        bSizerTime = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText68 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText68.Wrap( -1 )
        bSizer271.Add( self.m_staticText68, 0, wx.ALL, 5 )
        

        self.spinUTCBegin = wx.SpinCtrl( sbSizer22.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        self.spinUTCBegin.SetMinSize( wx.Size( 50,-1 ) ) 
        self.spinUTCBegin.SetRange(-12,14)       
        self.spinUTCBegin.SetValue(0)       
        
        bSizerTime.Add(self.m_staticText68, 0, wx.ALL, 5)
        bSizerTime.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        bSizerTime.Add(self.spinUTCBegin, 0, wx.ALL, 5)

        sbSizer22.Add(bSizerTime, 0, wx.EXPAND, 5)

        bSizer80.Add( sbSizer22, 0, wx.EXPAND, 5 )
        
        sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields" ), wx.VERTICAL )
        
        bSizer2711 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2411 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"End Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2411.Wrap( -1 )
        bSizer2711.Add( self.m_staticText2411, 0, wx.ALL, 5 )
        
        
        bSizer2711.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_datePicker51 = wx.DatePickerCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize,wx.DP_ALLOWNONE )
        self.m_datePicker51.SetMinSize( wx.Size( 149,-1 ) )
        self.m_datePicker51.SetValue(wx.DateTime()) 
        bSizer2711.Add( self.m_datePicker51, 0, wx.ALL, 5 )
        
        self.m_timePicker2 = masked.TimeCtrl(\
            sbSizer23.GetStaticBox(), wx.ID_ANY,
            '00:00:00', wx.DefaultPosition,
            wx.DefaultSize, wx.TE_PROCESS_TAB,
            validator=wx.DefaultValidator,
            name = 'time',
            format = 'HHMMSS')
    
        h = self.m_timePicker2.GetSize().height
    
        self.spinner2 = wx.SpinButton(\
            sbSizer23.GetStaticBox(), wx.ID_ANY,
            wx.DefaultPosition, (-1,h), wx.SP_VERTICAL)
    
        self.m_timePicker2.BindSpinButton(self.spinner2)
   
        self.m_timePicker2.SetMinSize( wx.Size( 100,-1 ) )

        bSizer2711.Add( self.m_timePicker2, 0, wx.TOP, 5 )
        bSizer2711.Add( self.spinner2, 0, wx.TOP, 5 )
        #self.m_staticText681 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_staticText681.Wrap( -1 )
        #bSizer2711.Add( self.m_staticText681, 0, wx.ALL, 5 )
        
        #self.spinUTCEnd = wx.SpinCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        #self.spinUTCEnd.SetMinSize( wx.Size( 50,-1 ) ) 
        #self.spinUTCEnd.SetRange(-12,14)       
        

        #self.m_textCtrl461 = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_textCtrl461.SetMinSize( wx.Size( 50,-1 ) )
        
        #bSizer2711.Add( self.spinUTCEnd, 0, wx.ALL, 5 )
        
        
        sbSizer23.Add( bSizer2711, 0, wx.EXPAND, 5 )
        
        bSizer274 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText244 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Action File Link", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText244.Wrap( -1 )
        bSizer274.Add( self.m_staticText244, 0, wx.ALL, 5 )
        
        
        bSizer274.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl234 = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl234.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer274.Add( self.m_textCtrl234, 0, wx.ALL, 5 )
        
        
        sbSizer23.Add( bSizer274, 0, wx.EXPAND, 5 )
        
        bSizer272 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText242 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u" Action Description", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText242.Wrap( -1 )
        bSizer272.Add( self.m_staticText242, 0, wx.ALL, 5 )
        
        
        bSizer272.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl232 = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(280, 70), wx.TE_MULTILINE )
        #self.m_textCtrl232.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer272.Add( self.m_textCtrl232, 0, wx.ALL, 5 )
        
        
        sbSizer23.Add( bSizer272, 1, wx.EXPAND, 5 )
        
        bSizer273 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText243 = wx.StaticText( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Role Description", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText243.Wrap( -1 )
        bSizer273.Add( self.m_staticText243, 0, wx.ALL, 5 )
        
        
        bSizer273.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl233 = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(280, 70), wx.TE_MULTILINE )
        #self.m_textCtrl233.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer273.Add( self.m_textCtrl233, 0, wx.ALL, 5 )
        
        
        sbSizer23.Add( bSizer273, 0, wx.EXPAND, 5 )
        
        
        bSizer80.Add( sbSizer23, 0, wx.EXPAND, 5 )
        
        m_sdbSizer10 = wx.StdDialogButtonSizer()
        self.m_sdbSizer10OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer10.AddButton( self.m_sdbSizer10OK )
        self.m_sdbSizer10Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer10.AddButton( self.m_sdbSizer10Cancel )
        m_sdbSizer10.Realize()
        
        bSizer80.Add( m_sdbSizer10, 1, wx.EXPAND, 5 )

        self.SetSizer( bSizer80 )
        self.Layout()

        self.__size_of_combo = self.m_comboBox13.GetSize()

    def on_show_combo(self, event):
        combo = event.GetEventObject()
        combo.SetSize(combo.GetBestSize())

    def on_hide_combo(self, event):
        combo = event.GetEventObject()
        combo.SetSize(self.__size_of_combo)

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None)
    frame.SetSizer(wx.BoxSizer(wx.VERTICAL)) 
    pnl = AddNewActionsPanelView(frame)
    frame.CenterOnScreen()
    frame.Show()
    app.MainLoop()
