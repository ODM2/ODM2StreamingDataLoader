import wx

from src.controllers.Database import Database
from ObjectListView import ObjectListView, ColumnDefn

from collections import namedtuple

class SeriesSelectPanel(wx.Panel):
    '''
        The base class for a series select panel.
        There are six types of series represented by
        this base class:
            - SamplingFeature
            - Variable
            - Units
            - Processing Level
            - Actions
            - Results
        Each of these types of series implements
        the Object List View differently, so those
        details are abstracted out of this class.

        On the other hand, some functionality is the
        same across all classes, so those details
        are defined in this base class.
    '''
    def __init__( self, parent, label):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 644,330 ), style = wx.TAB_TRAVERSAL )
        
        fgSizer1 = wx.FlexGridSizer( 0, 1, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.static_txt = wx.StaticText(self, wx.ID_ANY,
                u"Please select a " + label, wx.DefaultPosition,
                wx.DefaultSize, 0)
        self.static_txt.Wrap(-1)
        fgSizer1.Add(self.static_txt, 0, wx.ALL, 5)
        
        self.list_ctrl = ObjectListView(self, wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.Size(630,250),
            style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        fgSizer1.Add(self.list_ctrl, 0, wx.ALL, 5)

        self.new_button = wx.Button(self, wx.ID_ANY,
                u"Add New " + label, wx.DefaultPosition,
                wx.Size(-1,-1), 0)
        fgSizer1.Add(self.new_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        self.SetSizer(fgSizer1)
        self.Layout()
        # The panel to use for adding a new series.
        self.label = label
        self.Bind(wx.EVT_BUTTON, self.onButtonAdd)

        print "Database handle: ", parent.parent.db
        self.db = parent.parent.db

    def getSeriesData(self):
        raise NotImplementedError

    def addPanel(self, panel):
        self.new_panel = panel
    
    def onButtonAdd(self, event):
        event.Skip()

    def __del__( self ):
        pass


