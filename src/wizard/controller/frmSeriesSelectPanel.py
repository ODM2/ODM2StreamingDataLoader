import wx

from src.controllers.Database import Database
from ObjectListView import ObjectListView, ColumnDefn

from collections import namedtuple

class SeriesSelectPanel(wx.Panel):
    '''
    '''
    def __init__( self, parent, label=""):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 774,360 ), style = wx.TAB_TRAVERSAL )
        
        fgSizer1 = wx.BoxSizer(wx.VERTICAL)#wx.FlexGridSizer( 0, 1, 0, 0 )
        #fgSizer1.SetFlexibleDirection( wx.BOTH )
        #fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.static_txt = wx.StaticText(self, wx.ID_ANY,
                u"Select or create new %s." % label, wx.DefaultPosition,
                wx.DefaultSize, 0)
        self.static_txt.Wrap(-1)
        fgSizer1.Add(self.static_txt, 0, wx.ALL, 5)
        
        self.list_ctrl = ObjectListView(self, wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.DefaultSize,
            style=wx.LC_REPORT|wx.SUNKEN_BORDER|wx.EXPAND)
        fgSizer1.Add(self.list_ctrl, 1, wx.ALL|wx.EXPAND)

        self.new_button = wx.Button(self, wx.ID_ANY,
                u"New %s" % label, wx.DefaultPosition,
                wx.Size(-1,-1), 0)
        fgSizer1.Add(self.new_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5)
        
        self.SetSizer(fgSizer1)
        self.Layout()
        # The panel to use for adding a new series.
        self.Bind(wx.EVT_BUTTON, self.onButtonAdd)

        #print "Database handle: ", parent.parent.db
        #self.db = parent.parent.db

    def getSeriesData(self):
        raise NotImplementedError

    def addPanel(self, panel):
        self.new_panel = panel
    
    def onButtonAdd(self, event):
        event.Skip()

    def __del__( self ):
        pass


