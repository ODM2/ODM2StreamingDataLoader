
import wx
#import wx.lib.agw.ultimatelistctrl as ULC
from ObjectListView import ObjectListView, ColumnDefn

from src.wizard.controller.frmVirtualList import VirtualList
from src.wizard.controller.frmVirtualGrid import VirtualGrid, GridBase
#from lib.ObjectListView.ObjectListView import VirtualObjectListView


class DataConfigPanelView(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 922,519 ), style = wx.TAB_TRAVERSAL )
        
        bSizerMain = wx.BoxSizer( wx.VERTICAL )
        
        bSizerTop = wx.BoxSizer( wx.HORIZONTAL )
        
        sbSizerTime = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Date Time Column:" ), wx.VERTICAL )
        
        choiceTimeColChoices = []
        self.choiceTimeCol = wx.Choice( sbSizerTime.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 160,-1 ), choiceTimeColChoices, 0 )
        self.choiceTimeCol.SetSelection( 0 )
        sbSizerTime.Add( self.choiceTimeCol, 0, wx.ALL, 10 )
        
        self.spinUTCOffset = wx.SpinCtrl( sbSizerTime.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        self.spinUTCOffset.SetMinSize( wx.Size( 160,-1 ) )
        
        sbSizerTime.Add( self.spinUTCOffset, 0, wx.ALL, 10 )
        
        
        bSizerTop.Add( sbSizerTime, 0, wx.EXPAND, 10 )
        
        sbSizerData = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Data Columns:" ), wx.VERTICAL )
        
        self.m_listCtrl1 = VirtualGrid(self, id=wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.Size(-1, 250))
        
        sbSizerData.Add(self.m_listCtrl1, 0, wx.ALL, 10)
        
        bSizerTop.Add( sbSizerData, 1, wx.EXPAND, 10 )
        
        
        bSizerMain.Add( bSizerTop, 0, wx.EXPAND|wx.ALL, 10 )
        
        bSizerBottom = wx.BoxSizer( wx.VERTICAL )
        
        sbSizerMappings = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Mappings:" ), wx.VERTICAL )
        
        # ObjectListView table.
        self.m_listCtrl3 = \
                ObjectListView(sbSizerMappings.GetStaticBox(),
                           id=wx.ID_ANY,
                           pos=wx.DefaultPosition,
                           size=wx.Size(-1,200),
                           style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        # Customize the list control's message
        # when it is empty.
        self.m_listCtrl3.oddRowsBackColor = wx.Colour(255, 248, 229)
        self.m_listCtrl3.evenRowsBackColor = wx.Colour(204, 229, 255)
        self.m_listCtrl3.SetEmptyListMsg(\
            "No columns mapped")
        self.m_listCtrl3.SetObjects(None)
        self.m_listCtrl3.SetColumns([
            ColumnDefn('Data Column','left',150,'variableName'),
            ColumnDefn('Result ID','left',70,'resultID'),
            ColumnDefn('Samp. Feat. Code','left',110,'samplingFeatureCode'),
            ColumnDefn('Samp. Feat. Name','left',110,'samplingFeatureName'),
            ColumnDefn('Variable Code','left',100,'variableCode'),
            ColumnDefn('Variable Name','left',100,'variableNameCV'),
            ColumnDefn('Units Name','left',80,'unitsName'),
            ColumnDefn('Method Code','left',100,'methodCode'),
            ColumnDefn('Method Name','left',100,'methodName'),
            ColumnDefn('Proc. Level Code','left',110,'processingLevelCode'),])  
        
        sbSizerMappings.Add(self.m_listCtrl3, 1, wx.EXPAND|wx.ALL)
        
        bSizerBottom.Add( sbSizerMappings, 0, wx.EXPAND|wx.ALL)
        
        
        bSizerMain.Add( bSizerBottom, 1, wx.EXPAND|wx.ALL, 10 )
        
        
        self.SetSizer( bSizerMain )
        self.Layout()
        
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.onColClick,
            self.m_listCtrl1)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.onCellClick,
            self.m_listCtrl1)
        self.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.onCellClick,
            self.m_listCtrl1)
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,\
            self.onColDoubleClick, self.m_listCtrl1)
        self.Bind(wx.EVT_CHOICE, self.onTimeChoice,\
            self.choiceTimeCol)
    
    def __del__(self):
        pass
    
    def onAddNew(self, event):
        event.Skip()

    def onColClick(self, event):
        event.Skip()
    
    def onCellClick(self, event):
        event.Skip()
    
    def onTimeSelect(self, event):
        event.Skip()
    
    def onTimeChoice(self, event):
        event.Skip()
    
    def onColDoubleClick(self, event):
        event.Skip()
"""
class DataConfigPanelView(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(DataConfigPanelView, self).__init__(parent, **kwargs)

        supa_sizer = wx.FlexGridSizer(3, 1, 10, 10)
        supa_sizer.SetFlexibleDirection(wx.BOTH)
        supa_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #self.m_listCtrl1 = VirtualList(self, size=wx.Size(1000, 400))
        
        #self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,400 ), wx.LC_REPORT | wx.LC_VIRTUAL | wx.LC_HRULES | wx.LC_VRULES )
        
        self.m_listCtrl1 = VirtualGrid(self, id=wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.Size(1000, 400))
        
        self.infoTxt = wx.StaticText(self, wx.ID_ANY, u"Double-click column headings to create mapping.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.infoTxt.Wrap( -1 )
        supa_sizer.Add( self.infoTxt, 0, wx.ALL, 10 )
        
        supa_sizer.Add( self.m_listCtrl1, 0, wx.ALL, 10 )
                
        fgSizer13 = wx.FlexGridSizer( 0, 2, 10, 10 )
        fgSizer13.SetFlexibleDirection( wx.BOTH )
        fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Date Time:" ), wx.HORIZONTAL )
        
        fgSizer10 = wx.FlexGridSizer( 3, 2, 10, 10 )
        fgSizer10.SetFlexibleDirection( wx.BOTH )
        fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_radioBtn3 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"UTC", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer10.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
        
        m_choice3Choices = []
        self.m_choice3 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        fgSizer10.Add( self.m_choice3, 0, wx.ALL, 5 )
        self.m_choice3.SetMinSize( wx.Size( 170,-1 ) )
        
        self.m_radioBtn4 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Local", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer10.Add( self.m_radioBtn4, 0, wx.ALL, 5 )

        self.m_radioBtn4.SetValue(False)
        self.m_radioBtn3.SetValue(True)

        self.m_choice4 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, [], 0 )
        self.m_choice4.SetSelection( 0 )
        fgSizer10.Add( self.m_choice4, 0, wx.ALL, 10 )
        self.m_choice4.SetMinSize( wx.Size( 170,-1 ) )
        
        self.m_choice4.Enable(False)

        self.m_staticText6 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Time Zone", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        fgSizer10.Add( self.m_staticText6, 0, wx.ALL, 10 )

        boxSizer = wx.BoxSizer(wx.HORIZONTAL)        

        m_choice5Choices = [ u"-7" ]
        self.m_choice5 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
        self.m_choice5.SetSelection( 0 )
        boxSizer.Add( self.m_choice5, 0, wx.ALL, 10 )
                

        fgSizer10.Add(boxSizer, 0, wx.ALL, 10)     
        
        sbSizer3.Add( fgSizer10, 1, wx.EXPAND, 10 )
        
        fgSizer13.Add( sbSizer3, 1, wx.EXPAND, 10 )
        
        fgSizer12 = wx.FlexGridSizer( 0, 2, 10, 10 )
        fgSizer12.SetFlexibleDirection( wx.BOTH )
        fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        #self.m_listCtrl3 = ULC.UltimateListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 685,150 ), agwStyle=wx.LC_VRULES | wx.LC_HRULES | wx.LC_REPORT )

        # ObjectListView table.
        self.m_listCtrl3 = \
                ObjectListView(self, id=wx.ID_ANY,
                           pos=wx.DefaultPosition,
                           size=wx.Size(700,-1),
                           style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        # Customize the list control's message
        # when it is empty.
        self.m_listCtrl3.oddRowsBackColor = wx.Colour(255, 248, 229)
        self.m_listCtrl3.evenRowsBackColor = wx.Colour(204, 229, 255)
        self.m_listCtrl3.SetEmptyListMsg(\
            "No columns mapped")
        self.m_listCtrl3.SetObjects(None)
        self.m_listCtrl3.SetColumns([
            ColumnDefn('Data Column','left',150,'variableName'),
            ColumnDefn('Result ID','left',70,'resultID'),
            ColumnDefn('Samp. Feat. Code','left',110,'samplingFeatureCode'),
            ColumnDefn('Samp. Feat. Name','left',110,'samplingFeatureName'),
            ColumnDefn('Variable Code','left',100,'variableCode'),
            ColumnDefn('Variable Name','left',100,'variableNameCV'),
            ColumnDefn('Units Name','left',80,'unitsName'),
            ColumnDefn('Method Code','left',100,'methodCode'),
            ColumnDefn('Method Name','left',100,'methodName'),
            ColumnDefn('Proc. Level Code','left',110,'processingLevelCode'),])  
        
        fgSizer12.Add( self.m_listCtrl3, 0, wx.ALL, 10 )
        
        #button_right_sizer = wx.BoxSizer( wx.VERTICAL )
                
        #self.m_button8 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        #self.m_button8.SetForegroundColour( wx.Colour( 91, 196, 117 ) )
        #self.m_button8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        #button_right_sizer.Add( self.m_button8, 0, wx.ALL, 5 )
        
        #self.m_button9 = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        #button_right_sizer.Add( self.m_button9, 0, wx.ALL, 5 )
        
        #self.m_button10 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        #self.m_button10.SetForegroundColour( wx.Colour( 255, 88, 88 ) )
        
        #button_right_sizer.Add( self.m_button10, 0, wx.ALL, 5 )
        
        
        #fgSizer12.Add( button_right_sizer, 1, wx.EXPAND, 5 )
        
        
        fgSizer13.Add( fgSizer12, 1, wx.EXPAND, 10 )        

        supa_sizer.Add(fgSizer13, 1, wx.EXPAND, 10)
        
        self.SetSizer(supa_sizer)
        self.Layout()

        #self.Bind(wx.EVT_BUTTON, self.onAddNew, self.m_button8)
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.onColClick,
            self.m_listCtrl1)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.onCellClick,
            self.m_listCtrl1)
        self.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.onCellClick,
            self.m_listCtrl1)
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK,\
            self.onColDoubleClick, self.m_listCtrl1)
        self.Bind(wx.EVT_RADIOBUTTON, self.onTimeSelect,\
            self.m_radioBtn4)
        self.Bind(wx.EVT_RADIOBUTTON, self.onTimeSelect,\
            self.m_radioBtn3)
        self.Bind(wx.EVT_CHOICE, self.onTimeChoice,\
            self.m_choice3)
        self.Bind(wx.EVT_CHOICE, self.onTimeChoice,\
            self.m_choice4)
"""
