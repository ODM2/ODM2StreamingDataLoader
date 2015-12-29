import wx

from src.wizard.controller.frmRequiredValidator \
    import RequiredValidator

class NewSpatialReferenceView(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 542,300 ), style = wx.TAB_TRAVERSAL )
        
        self.SetMinSize( wx.Size( 400,250 ) )
        
        bSizer80 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"Code:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        bSizer35.Add( self.m_staticText31, 0, wx.ALL, 5 )
        
        
        bSizer35.AddSpacer((0, 0), 1, wx.EXPAND, 5 )
        
        self.textCode = wx.TextCtrl(self, wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), 0)
        bSizer35.Add(self.textCode, 1, wx.ALL, 5)
        
        
        bSizer80.Add(bSizer35, 0, wx.EXPAND, 5 )
        
        bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
        
        name = wx.StaticText(self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        name.Wrap( -1 )
        bSizer36.Add(name, 0, wx.ALL, 5 )
        
        
        bSizer36.AddSpacer((0, 0), 1, wx.EXPAND, 5 )
        
        self.textName = wx.TextCtrl(self, wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1),
            validator=RequiredValidator())
        bSizer36.Add(self.textName, 1, wx.ALL, 5)
        
        
        bSizer80.Add(bSizer36, 0, wx.EXPAND, 5 )
        
        bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
        
        desc = wx.StaticText(self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
        desc.Wrap( -1 )
        bSizer37.Add(desc, 0, wx.ALL, 5 )
        
        
        bSizer37.AddSpacer((0, 0), 1, wx.EXPAND, 5 )
        
        self.textDesc = wx.TextCtrl(self, wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,70), wx.TE_MULTILINE)
        bSizer37.Add(self.textDesc, 1, wx.ALL, 5)
        
        
        bSizer80.Add(bSizer37, 0, wx.EXPAND, 5 )
        
        bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
        
        link = wx.StaticText(self, wx.ID_ANY, u"Link:", wx.DefaultPosition, wx.DefaultSize, 0 )
        link.Wrap( -1 )
        bSizer38.Add(link, 0, wx.ALL, 5 )
        
        
        bSizer38.AddSpacer((0, 0), 1, wx.EXPAND, 5 )
        
        self.textLink = wx.TextCtrl(self, wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), 0)
        bSizer38.Add(self.textLink, 1, wx.ALL, 5)
        
        
        bSizer80.Add(bSizer38, 0, wx.EXPAND, 5 )
        
        m_sdbSizer10 = wx.StdDialogButtonSizer()
        self.m_sdbSizer10OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer10.AddButton( self.m_sdbSizer10OK )
        self.m_sdbSizer10Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer10.AddButton( self.m_sdbSizer10Cancel )
        m_sdbSizer10.Realize();
        
        bSizer80.Add( m_sdbSizer10, 0, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer80 )
        self.Layout()
        



