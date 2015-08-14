
import wx
import wx.lib.agw.ultimatelistctrl as ULC

from controller.frmVirtualList import VirtualList
from controller.frmVirtualGrid import VirtualGrid, GridBase
from lib.ObjectListView.ObjectListView import VirtualObjectListView

class DataConfigPanelView(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(DataConfigPanelView, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(2, 1, 0, 0)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #self.m_listCtrl1 = VirtualList(self, size=wx.Size(1000, 400))
        
        #self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,400 ), wx.LC_REPORT | wx.LC_VIRTUAL | wx.LC_HRULES | wx.LC_VRULES )
        
        self.m_listCtrl1 = VirtualGrid(self, id=wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.Size(1000, 400))
        
        supa_sizer.Add( self.m_listCtrl1, 0, wx.ALL, 5 )
                
        fgSizer13 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer13.SetFlexibleDirection( wx.BOTH )
        fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Time:" ), wx.HORIZONTAL )
        
        fgSizer10 = wx.FlexGridSizer( 3, 2, 0, 0 )
        fgSizer10.SetFlexibleDirection( wx.BOTH )
        fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_radioBtn3 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"UTC Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer10.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
        
        m_choice3Choices = []
        self.m_choice3 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        fgSizer10.Add( self.m_choice3, 0, wx.ALL, 5 )
        
        self.m_radioBtn4 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Local Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer10.Add( self.m_radioBtn4, 0, wx.ALL, 5 )
        
        m_choice4Choices = [ u"TIMESTAMP" ]
        self.m_choice4 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
        self.m_choice4.SetSelection( 0 )
        fgSizer10.Add( self.m_choice4, 0, wx.ALL, 5 )
        
        self.m_staticText6 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Time Zone", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        fgSizer10.Add( self.m_staticText6, 0, wx.ALL, 5 )

        boxSizer = wx.BoxSizer(wx.HORIZONTAL)        

        m_choice5Choices = [ u"-7" ]
        self.m_choice5 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
        self.m_choice5.SetSelection( 0 )
        boxSizer.Add( self.m_choice5, 0, wx.ALL, 5 )
                
        self.m_checkBox1 = wx.CheckBox(sbSizer3.GetStaticBox(),\
                wx.ID_ANY, u"DST", wx.DefaultPosition, wx.DefaultSize,\
                0)
        boxSizer.Add(self.m_checkBox1, 0, wx.ALL, 5)

        fgSizer10.Add(boxSizer, 0, wx.ALL, 5)     
        
        sbSizer3.Add( fgSizer10, 1, wx.EXPAND, 5 )
        
        fgSizer13.Add( sbSizer3, 1, wx.EXPAND, 5 )
        
        fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer12.SetFlexibleDirection( wx.BOTH )
        fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_listCtrl3 = ULC.UltimateListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 685,150 ), agwStyle=wx.LC_VRULES | wx.LC_HRULES | wx.LC_REPORT )
        fgSizer12.Add( self.m_listCtrl3, 0, wx.ALL, 5 )
        
        button_right_sizer = wx.BoxSizer( wx.VERTICAL )
                
        self.m_button8 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_button8.SetForegroundColour( wx.Colour( 91, 196, 117 ) )
        self.m_button8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        button_right_sizer.Add( self.m_button8, 0, wx.ALL, 5 )
        
        self.m_button9 = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        button_right_sizer.Add( self.m_button9, 0, wx.ALL, 5 )
        
        self.m_button10 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        self.m_button10.SetForegroundColour( wx.Colour( 255, 88, 88 ) )
        
        button_right_sizer.Add( self.m_button10, 0, wx.ALL, 5 )
        
        
        fgSizer12.Add( button_right_sizer, 1, wx.EXPAND, 5 )
        
        
        fgSizer13.Add( fgSizer12, 1, wx.EXPAND, 5 )        

        supa_sizer.Add(fgSizer13, 1, wx.EXPAND, 5)
        
        self.SetSizer(supa_sizer)
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.onAddNew, self.m_button8)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.onColClick,
            self.m_listCtrl1)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onColClick,
            self.m_listCtrl1)

    def __del__(self):
        pass
    
    def onAddNew(self, event):
        event.Skip()

    def onColClick(self, event):
        event.Skip()

        
