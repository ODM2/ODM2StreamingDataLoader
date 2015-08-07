import wx

class SeriesSelectPanel(wx.Panel):
    def __init__( self, parent, label ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 644,330 ), style = wx.TAB_TRAVERSAL )
        
        fgSizer1 = wx.FlexGridSizer( 0, 1, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.static_txt = wx.StaticText(self, wx.ID_ANY,
                u"Please select a " + label, wx.DefaultPosition,
                wx.DefaultSize, 0)
        self.static_txt.Wrap(-1)
        fgSizer1.Add(self.static_txt, 0, wx.ALL, 5)
        
        self.list_ctrl = wx.ListCtrl(self, wx.ID_ANY,
                wx.DefaultPosition, wx.Size(630,250),
                wx.LC_ICON)
        fgSizer1.Add(self.list_ctrl, 0, wx.ALL, 5)
        
        self.new_button = wx.Button(self, wx.ID_ANY,
                u"Add New " + label, wx.DefaultPosition,
                wx.Size(100,-1), 0)
        fgSizer1.Add(self.new_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        
        self.SetSizer(fgSizer1)
        self.Layout()

    def setLabels(self, string):
        print dir(self.static_txt)
    
    def __del__( self ):
        pass


