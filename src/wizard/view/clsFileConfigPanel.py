
import wx
import wx.lib.masked as masked
import operator

from controller.frmFilePathValidator import FilePathValidator

class FileConfigPanelView(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(FileConfigPanelView, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(2, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        
        file_location_sizer = wx.StaticBoxSizer(\
            wx.StaticBox(self, wx.ID_ANY, u'Location:'),
            wx.HORIZONTAL)

        file_location_flex_sizer = wx.FlexGridSizer(2, 3, 0, 0)
        file_location_flex_sizer.SetFlexibleDirection(wx.BOTH)
        file_location_flex_sizer.SetNonFlexibleGrowMode(\
            wx.FLEX_GROWMODE_SPECIFIED)
      
        self.local_file_radio = wx.RadioButton(\
            file_location_sizer.GetStaticBox(),
            wx.ID_ANY, u'Local File', wx.DefaultPosition,
            wx.DefaultSize, style=wx.RB_GROUP)
        file_location_flex_sizer.Add(self.local_file_radio, 0,
            wx.ALL | wx.RB_GROUP, 5)
        self.local_file_radio.SetValue(True)

        self.local_file_txt =  wx.TextCtrl(\
            file_location_sizer.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString, wx.Point(-1,-1), wx.Size(500,-1),
            validator=FilePathValidator())
        file_location_flex_sizer.Add(self.local_file_txt, 0,
            wx.ALL, 5)

        self.local_file_btn =  wx.Button(\
            file_location_sizer.GetStaticBox(), 49,
            u'...', wx.DefaultPosition, wx.Size(40,-1))
        file_location_flex_sizer.Add(self.local_file_btn, 0,
            wx.ALIGN_RIGHT | wx.ALL, 5)

        
        self.remote_file_radio = wx.RadioButton(\
            file_location_sizer.GetStaticBox(),
            wx.ID_ANY, u'Remote File', wx.DefaultPosition,
            wx.DefaultSize)
        file_location_flex_sizer.Add(self.remote_file_radio, 0,
            wx.ALL, 5)

        self.remote_file_txt =  wx.TextCtrl(\
            file_location_sizer.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString, wx.Point(-1,-1), wx.Size(500,-1))
        file_location_flex_sizer.Add(self.remote_file_txt, 0,
            wx.ALL, 5)

        self.remote_file_txt.Enable(False)
        
        self.Bind(wx.EVT_RADIOBUTTON, self.onFileSelect,
            self.local_file_radio)
        self.Bind(wx.EVT_RADIOBUTTON, self.onFileSelect,
            self.remote_file_radio)
        self.Bind(wx.EVT_BUTTON, self.onFileSelectPath,
            self.local_file_btn)
        
        file_location_sizer.Add(file_location_flex_sizer,
            1, wx.EXPAND, 5)
       
        supa_sizer.Add(file_location_sizer, 1, wx.EXPAND, 5)

        
        options_sizer = wx.StaticBoxSizer(wx.StaticBox(self,
            wx.ID_ANY, u'Options:'), wx.VERTICAL)
        
        options_flex_sizer = wx.FlexGridSizer(0, 4, 0, 0)
        options_flex_sizer.SetFlexibleDirection(wx.BOTH)
        options_flex_sizer.SetNonFlexibleGrowMode(\
                wx.FLEX_GROWMODE_SPECIFIED)

        options_flex_sizer.AddSpacer((5, 0), 1, wx.EXPAND, 5)
        
        self.delimiter_static = wx.StaticText(\
                options_sizer.GetStaticBox(), wx.ID_ANY,
                u'Delimiter', wx.DefaultPosition, wx.DefaultSize, 0)
        self.delimiter_static.Wrap(-1)
        options_flex_sizer.Add(self.delimiter_static, 0, wx.ALL, 5)

        options_flex_sizer.AddSpacer((35, 0), 1, wx.EXPAND, 5)

        m_choice1Choices = [ u'Comma', u'Tab', u'Custom' ]
        self.m_choice1 = wx.Choice(options_sizer.GetStaticBox(),
            wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
            m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        options_flex_sizer.Add(self.m_choice1, 0, wx.TOP, 5)
                
                
        options_sizer.Add(options_flex_sizer, 1, wx.EXPAND, 5)
                
        options_flex_sizer2 = wx.FlexGridSizer(2, 6, 0, 0)
        options_flex_sizer2.SetFlexibleDirection(wx.BOTH)
        options_flex_sizer2.SetNonFlexibleGrowMode(\
            wx.FLEX_GROWMODE_SPECIFIED )
                
                
        options_flex_sizer2.AddSpacer((5, 0), 1, wx.EXPAND, 5)
                
        self.m_staticText2 = wx.StaticText(\
            options_sizer.GetStaticBox(), wx.ID_ANY,
            u'Run Every', wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        options_flex_sizer2.Add(self.m_staticText2, 0, wx.ALL, 5)
                
                
        options_flex_sizer2.AddSpacer((33, 0), 1, wx.EXPAND, 5)
                
        self.m_spinCtrl1 = wx.SpinCtrl(options_sizer.GetStaticBox(),
            wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
            wx.Size(50,-1), wx.SP_ARROW_KEYS, 0, 10, 4)
        options_flex_sizer2.Add( self.m_spinCtrl1, 0, wx.TOP, 5)
                
                
        options_flex_sizer2.AddSpacer((10, 0), 1, wx.EXPAND, 5)
                
        m_choice2Choices = [u'Hours', u'Minutes']
        self.m_choice2 = wx.Choice(options_sizer.GetStaticBox(),
            wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
            m_choice2Choices, 0)
        self.m_choice2.SetSelection(1)
        options_flex_sizer2.Add(self.m_choice2, 0, wx.TOP, 5)
                
                
        options_sizer.Add(options_flex_sizer2, 1, wx.EXPAND, 5)
                
        options_flex_sizer3 = wx.FlexGridSizer(0, 6, 0, 0)
        options_flex_sizer3.SetFlexibleDirection(wx.BOTH)
        options_flex_sizer3.SetNonFlexibleGrowMode(\
            wx.FLEX_GROWMODE_SPECIFIED)
                
        options_flex_sizer3.AddSpacer((5, 0), 1, wx.EXPAND, 5)
                
        self.m_staticText6 = wx.StaticText(\
            options_sizer.GetStaticBox(), wx.ID_ANY,
            u'Start Date and Time', wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        options_flex_sizer3.Add(self.m_staticText6, 0, wx.ALL, 5)
                
                
        options_flex_sizer3.AddSpacer((30, 0), 1, wx.EXPAND, 5)
                
        self.m_datePicker3 = wx.DatePickerCtrl(\
            options_sizer.GetStaticBox(), wx.ID_ANY,
            wx.DefaultDateTime, wx.DefaultPosition,
            wx.DefaultSize, wx.DP_DEFAULT)
        options_flex_sizer3.Add(self.m_datePicker3, 0, wx.TOP, 5)
                
        self.m_timePicker1 = masked.TimeCtrl(\
            options_sizer.GetStaticBox(), wx.ID_ANY,
            '00:00:00', wx.DefaultPosition,
            wx.DefaultSize, wx.TE_PROCESS_TAB,
            validator=wx.DefaultValidator,
            name = 'time',
            format = 'HHMMSS')
        
        h = self.m_timePicker1.GetSize().height
        
        self.spinner = wx.SpinButton(\
            options_sizer.GetStaticBox(), wx.ID_ANY,
            wx.DefaultPosition, (-1,h), wx.SP_VERTICAL)
        
        self.m_timePicker1.BindSpinButton(self.spinner)
        
        options_flex_sizer3.Add(self.m_timePicker1, 0, wx.TOP, 5)
        options_flex_sizer3.Add(self.spinner, 0, wx.TOP, 5)
                
                
        options_sizer.Add(options_flex_sizer3, 1, wx.EXPAND, 5)
                
        options_flex_sizer4 = wx.FlexGridSizer(0, 3, 0, 0)
        options_flex_sizer4.SetFlexibleDirection(wx.BOTH)
        options_flex_sizer4.SetNonFlexibleGrowMode(\
            wx.FLEX_GROWMODE_SPECIFIED)
                
                
        options_flex_sizer4.AddSpacer((5, 0), 1, wx.EXPAND, 5)
                
        self.m_staticText7 = wx.StaticText(\
            options_sizer.GetStaticBox(), wx.ID_ANY,
            u'Column Headers (Line Number)', wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        options_flex_sizer4.Add(self.m_staticText7, 0, wx.ALL, 5)
                
        self.m_spinCtrl2 = wx.SpinCtrl(options_sizer.GetStaticBox(),\
            wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
            wx.Size(50,-1), wx.SP_ARROW_KEYS, 0, 0, 0)
        options_flex_sizer4.Add(self.m_spinCtrl2, 0, wx.TOP, 5)
        self.m_spinCtrl2.SetRange(0, 999)
        self.m_spinCtrl2.SetValue(0)

                
        options_sizer.Add(options_flex_sizer4, 1, wx.EXPAND, 5)
                
        options_flex_sizer5 = wx.FlexGridSizer(0, 4, 0, 0)
        options_flex_sizer5.SetFlexibleDirection(wx.BOTH)
        options_flex_sizer5.SetNonFlexibleGrowMode(\
            wx.FLEX_GROWMODE_SPECIFIED )
                
                
        options_flex_sizer5.AddSpacer((5, 0), 1, wx.EXPAND, 5)
        
        self.m_staticText9 = wx.StaticText(\
            options_sizer.GetStaticBox(), wx.ID_ANY,
            u'Data Begins (Line Number)', wx.DefaultPosition,
            wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        options_flex_sizer5.Add(self.m_staticText9, 0, wx.ALL, 5)
        
        
        options_flex_sizer5.AddSpacer((25, 0), 1, wx.EXPAND, 5)
        
        self.m_spinCtrl4 = wx.SpinCtrl(\
            options_sizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
            wx.DefaultPosition, wx.Size(50,-1), wx.SP_ARROW_KEYS,
            0, 0, 0)
        options_flex_sizer5.Add(self.m_spinCtrl4, 0, wx.TOP, 5)
        self.m_spinCtrl4.SetRange(0, 999)
        self.m_spinCtrl4.SetValue(0)
        
        
        options_sizer.Add(options_flex_sizer5, 1, wx.EXPAND, 5)
        
        supa_sizer.Add(options_sizer, 1, wx.EXPAND, 5)
        
        self.SetSizer(supa_sizer)
        self.Layout()

    def onFileSelect(self, event):
        event.Skip()
    
    def onFileSelectPath(self, event):
        event.Skip()

    def __del__(self):
        pass

