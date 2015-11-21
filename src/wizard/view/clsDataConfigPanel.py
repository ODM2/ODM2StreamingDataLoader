
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
