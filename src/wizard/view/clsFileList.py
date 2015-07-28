
import wx
import operator

class FileListView(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(FileListView, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(2, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        size = tuple(map(operator.sub, parent.GetSize(), (20, 150)))
        
        self.fileListCtrl = wx.ListCtrl(self, wx.ID_ANY,
                        wx.DefaultPosition, size,
                        wx.LC_HRULES | \
                        wx.LC_REPORT | wx.LC_VRULES)
       
        self.fileListCtrl.InsertColumn(0, 'ID')
        self.fileListCtrl.InsertColumn(1, 'Server')
        self.fileListCtrl.InsertColumn(2, 'Database')
        self.fileListCtrl.InsertColumn(3, 'File Location')
        self.fileListCtrl.InsertColumn(4, 'Period')
        self.fileListCtrl.InsertColumn(5, 'Begin')
        self.fileListCtrl.InsertColumn(6, 'Last Update')
        supa_sizer.Add(self.fileListCtrl, 0, wx.ALL, 5)

        '''
        bottom_sizer = wx.FlexGridSizer(0, 2, 0, 0)
        bottom_sizer.SetFlexibleDirection(wx.BOTH)
        bottom_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
       
        left_bottom_sizer = wx.StaticBoxSizer(wx.StaticBox(self,
                        wx.ID_ANY, u'Time'), wx.HORIZONTAL)

        left_bottom_sizer_flex = wx.FlexGridSizer(3, 2, 0, 0)
        left_bottom_sizer_flex.SetFlexibleDirection(wx.BOTH)
        left_bottom_sizer_flex.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
       
        self.date_time_radio = wx.RadioButton(\
                        left_bottom_sizer.GetStaticBox(),
                        wx.ID_ANY, u'UTC Date Time',
                        wx.DefaultPosition, wx.DefaultSize, 0)
        left_bottom_sizer_flex.Add(self.date_time_radio, 0, wx.ALL, 5)
    

        self.date_time_choice = wx.Choice(\
                        left_bottom_sizer.GetStaticBox(), wx.ID_ANY,
                        wx.DefaultPosition, wx.DefaultSize,
                        [], 0 )
        left_bottom_sizer_flex.Add(self.date_time_choice, 0, wx.ALL, 5)
            
        self.local_date_time_radio = wx.RadioButton(\
                        left_bottom_sizer.GetStaticBox(),
                        wx.ID_ANY, u'Local Date Time',
                        wx.DefaultPosition, wx.DefaultSize, 0)
        left_bottom_sizer_flex.Add(self.local_date_time_radio, 0,
                        wx.ALL, 5)

        self.local_date_time_choice = wx.Choice(\
                        left_bottom_sizer.GetStaticBox(), wx.ID_ANY,
                        wx.DefaultPosition, wx.DefaultSize,
                        [], 0 )
        left_bottom_sizer_flex.Add(self.local_date_time_choice, 0,
                        wx.ALL, 5)
        
        self.time_zone_static = wx.StaticText(\
                        left_bottom_sizer.GetStaticBox(), wx.ID_ANY,
                        u'Time Zone', wx.DefaultPosition,
                        wx.DefaultSize, 0)
        self.time_zone_static.Wrap(-1)
        left_bottom_sizer_flex.Add(self.time_zone_static, 0, wx.ALL, 5)


        self.time_zone_choice = wx.Choice(\
                        left_bottom_sizer.GetStaticBox(), wx.ID_ANY,
                        wx.DefaultPosition, wx.DefaultSize,
                        [], 0 )
        left_bottom_sizer_flex.Add(self.time_zone_choice, 0, wx.ALL, 5)
       
        
        right_bottom_sizer_flex = wx.FlexGridSizer(0, 2, 0, 0)
        right_bottom_sizer_flex.SetFlexibleDirection(wx.BOTH)
        right_bottom_sizer_flex.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        

        self.fileListCtrl2 = wx.ListCtrl(self, wx.ID_ANY,
                        wx.DefaultPosition, wx.Size( 750,-1 ),
                        wx.LC_ICON | wx.LC_REPORT)
        right_bottom_sizer_flex.Add(self.fileListCtrl2, 0, wx.ALL, 5)
        
        
        left_bottom_sizer.Add(left_bottom_sizer_flex, 1, wx.EXPAND, 5)
        bottom_sizer.Add(left_bottom_sizer, 1, wx.EXPAND, 5)
        bottom_sizer.Add(right_bottom_sizer_flex, 1, wx.EXPAND, 5)

        supa_sizer.Add(bottom_sizer, 1, wx.EXPAND, 5)
        '''

        self.SetSizer(supa_sizer)
        self.Layout()

    def __del__(self):
        pass

