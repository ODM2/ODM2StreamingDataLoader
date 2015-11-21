
import wx
import wx.lib.masked as masked
import operator

from src.wizard.controller.frmFilePathValidator import FilePathValidator
from src.wizard.controller.frmURLValidator import URLValidator

class FileConfigPanelView(wx.Panel):
    def __init__(self, parent, **kwargs):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,253 ), style = wx.TAB_TRAVERSAL )
                
        fgSizer1 = wx.FlexGridSizer( 0, 1, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Data File Location:" ), wx.HORIZONTAL )
        
        fgSizer3 = wx.FlexGridSizer( 2, 3, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.local_file_radio = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Local File", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.local_file_radio, 0, wx.ALL, 5 )
        
        self.local_file_txt = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( -1,-1 ), validator=FilePathValidator() )
        self.local_file_txt.SetMinSize( wx.Size( 450,-1 ) )
        
        fgSizer3.Add( self.local_file_txt, 0, wx.ALL, 5 )
        
        self.local_file_btn = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Choose File...", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        fgSizer3.Add( self.local_file_btn, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        self.remote_file_radio = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Remote File", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.remote_file_radio, 0, wx.ALL, 5 )
        
        self.remote_file_txt = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), validator=URLValidator() )
        self.remote_file_txt.SetMinSize( wx.Size( 450,-1 ) )
        
        fgSizer3.Add( self.remote_file_txt, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
        
        
        fgSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
        
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options:" ), wx.VERTICAL )
        
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Column Headers (Line Number)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        
        bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_spinCtrl2 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 0, 0 )
        self.m_spinCtrl2.SetMinSize( wx.Size( 100,-1 ) )
        self.m_spinCtrl2.SetRange(0,999)
        self.m_spinCtrl2.SetValue(1)

        bSizer2.Add( self.m_spinCtrl2, 0, wx.TOP, 5 )
        
        
        gSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Data Begins (Line Number)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        
        bSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_spinCtrl4 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 0, 0 ) 
        self.m_spinCtrl4.SetMinSize( wx.Size( 100,-1 ) )

        self.m_spinCtrl4.SetRange(0,999)
        self.m_spinCtrl4.SetValue(2)        

        bSizer3.Add( self.m_spinCtrl4, 0, wx.TOP, 5 )
        
        
        gSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        
        bSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_datePicker3 = wx.DatePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
        self.m_datePicker3.SetMinSize( wx.Size( 100,-1 ) )
        
        bSizer4.Add( self.m_datePicker3, 0, wx.TOP, 5 )
        
        
        gSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText71 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Start Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText71.Wrap( -1 )
        bSizer7.Add( self.m_staticText71, 0, wx.ALL, 5 )
        
        
        bSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_timePicker1 = masked.TimeCtrl(\
            sbSizer2.GetStaticBox(), wx.ID_ANY,
            '00:00:00', wx.DefaultPosition,
            wx.DefaultSize, wx.TE_PROCESS_TAB,
            validator=wx.DefaultValidator,
            name = 'time',
            format = 'HHMMSS')
        
        h = self.m_timePicker1.GetSize().height
        
        self.spinner = wx.SpinButton(\
            sbSizer2.GetStaticBox(), wx.ID_ANY,
            wx.DefaultPosition, (-1,h), wx.SP_VERTICAL)
        
        self.m_timePicker1.BindSpinButton(self.spinner)
        
        
        self.m_timePicker1.SetMinSize( wx.Size( 100,-1 ) )
        
        bSizer7.Add( self.m_timePicker1, 0, wx.TOP, 5 )
        bSizer7.Add( self.spinner, 0, wx.TOP, 5 )
        
        
        gSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Delimiter", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        
        bSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_choice1Choices = [ u"Comma", u"Tab", u"Custom" ]
        self.m_choice1 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        self.m_choice1.SetMinSize( wx.Size( 100,-1 ) )
        
        bSizer6.Add( self.m_choice1, 0, wx.TOP, 5 )
        
        
        gSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Run Every", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        
        bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_spinCtrl1 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 4 )
        self.m_spinCtrl1.SetMinSize( wx.Size( 70,-1 ) )
        self.m_spinCtrl1.SetRange(1,999)
        self.m_spinCtrl1.SetValue(15)        
        
        bSizer5.Add( self.m_spinCtrl1, 0, wx.ALL|wx.TOP, 5 )
        
        m_choice2Choices = [ u"Hour", u"Minute", u"Day"]
        self.m_choice2 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 1 )
        self.m_choice2.SetMinSize( wx.Size( 100,-1 ) )
        
        bSizer5.Add( self.m_choice2, 0, wx.TOP, 5 )
        gSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
        sbSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )
        fgSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
       
        self.remote_file_txt.Enable(False)
        
        self.Bind(wx.EVT_RADIOBUTTON, self.onFileSelect,
            self.local_file_radio)
        self.Bind(wx.EVT_RADIOBUTTON, self.onFileSelect,
            self.remote_file_radio)
        self.Bind(wx.EVT_BUTTON, self.onFileSelectPath,
            self.local_file_btn) 
        self.m_spinCtrl2.Bind(wx.EVT_SPINCTRL, self.onColumnSpin)
        self.m_spinCtrl2.Bind(wx.EVT_TEXT, self.onColumnSpin)

        self.SetSizer( fgSizer1 )
        self.Layout()

    def onFileSelect(self, event):
        event.Skip()
    
    def onFileSelectPath(self, event):
        event.Skip()
    
    def onColumnSpin(self, event):
        event.Skip()

    def __del__(self):
        pass

