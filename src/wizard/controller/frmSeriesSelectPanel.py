import wx
from ObjectListView import ObjectListView
import sys


class SeriesSelectPanel(wx.Panel):
    def __init__( self, parent, label=""):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(774, 360), style=wx.TAB_TRAVERSAL )

        vertical_sizer = wx.BoxSizer(wx.VERTICAL)

        self.static_txt = wx.StaticText(self, wx.ID_ANY,
                u"Select or create new %s." % label, wx.DefaultPosition,
                wx.DefaultSize, 0)
        self.static_txt.Wrap(-1)
        vertical_sizer.Add(self.static_txt, 0, wx.ALL, 5)

        self._auto_width_style = wx.LIST_AUTOSIZE
        if sys.platform == "win32":
            self._auto_width_style = wx.LIST_AUTOSIZE_USEHEADER
        
        self.list_ctrl = ObjectListView(self, wx.ID_ANY, pos=wx.DefaultPosition,
                                        size=wx.DefaultSize, style=wx.LC_REPORT | wx.SUNKEN_BORDER | wx.EXPAND)

        vertical_sizer.Add(self.list_ctrl, 1, wx.ALL|wx.EXPAND)

        self.new_button = wx.Button(self, wx.ID_ANY, u"New %s" % label, wx.DefaultPosition, wx.Size(-1,-1), 0)
        vertical_sizer.Add(self.new_button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(vertical_sizer)
        self.Layout()
        # The panel to use for adding a new series.
        self.Bind(wx.EVT_BUTTON, self.onButtonAdd)

        self.list_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_keyboard_pressed_down)

    def on_keyboard_pressed_down(self, event):
        pass

    def auto_size_table(self):
        for i in range(self.list_ctrl.GetColumnCount()):
            self.list_ctrl.SetColumnWidth(col=i, width=self._auto_width_style)

    def getSeriesData(self):
        raise NotImplementedError

    def addPanel(self, panel):
        self.new_panel = panel
    
    def onButtonAdd(self, event):
        event.Skip()

    def __del__( self ):
        pass


