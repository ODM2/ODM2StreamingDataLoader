import wx

try:
    from agw import pycollapsiblepane as PCP
except ImportError:
    import wx.lib.agw.pycollapsiblepane as PCP


class NewAffiliationView(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 542,300 ), style = wx.TAB_TRAVERSAL )
        
        self.SetMinSize( wx.Size( 542,300 ) )
        
        bSizer80 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Person:" ), wx.VERTICAL )
        
        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText31 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Select existing person", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        bSizer35.Add( self.m_staticText31, 0, wx.ALL, 5 )
        
        
        bSizer35.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox13Choices = []
        self.m_comboBox13 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Select Person", wx.DefaultPosition, wx.DefaultSize, m_comboBox13Choices, 0 )
        self.m_comboBox13.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer35.Add( self.m_comboBox13, 0, wx.ALL, 5 )
        
        
        sbSizer22.Add( bSizer35, 1, wx.EXPAND, 10 )

        cpSizer = wx.BoxSizer( wx.VERTICAL )
        self.cp = cp = PCP.PyCollapsiblePane(self, wx.ID_ANY, "Add new person...", agwStyle=wx.CP_GTK_EXPANDER, style=wx.CP_DEFAULT_STYLE)
        self.MakePaneContent(cp.GetPane())
                        
        cpSizer.Add( cp, 1, wx.LEFT|wx.EXPAND, 25 )
        sbSizer22.Add( cpSizer, 1, wx.EXPAND|wx.GROW, 5)
        
        
        bSizer80.Add( sbSizer22, 1, wx.EXPAND, 5 )
        
        sbSizer221 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Orgnaization:" ), wx.VERTICAL )
        
        bSizer351 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText311 = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, u"Select existing organization", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText311.Wrap( -1 )
        bSizer351.Add( self.m_staticText311, 0, wx.ALL, 5 )
        
        
        bSizer351.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox131Choices = []
        self.m_comboBox131 = wx.ComboBox( sbSizer221.GetStaticBox(), wx.ID_ANY, u"Select Organization", wx.DefaultPosition, wx.DefaultSize, m_comboBox131Choices, 0 )
        self.m_comboBox131.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer351.Add( self.m_comboBox131, 0, wx.ALL, 5 )
        
        
        sbSizer221.Add( bSizer351, 1, wx.EXPAND, 5 )
        
        
        bSizer80.Add( sbSizer221, 1, wx.EXPAND, 5 )
        
        m_sdbSizer10 = wx.StdDialogButtonSizer()
        self.m_sdbSizer10OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer10.AddButton( self.m_sdbSizer10OK )
        self.m_sdbSizer10Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer10.AddButton( self.m_sdbSizer10Cancel )
        m_sdbSizer10.Realize();
        
        bSizer80.Add( m_sdbSizer10, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer80 )
        self.Layout()
        




    def MakePaneContent(self, pane):
        
        nameLbl = wx.StaticText(pane, -1, "Name:")
        name = wx.TextCtrl(pane, -1, "");
        
        addrLbl = wx.StaticText(pane, -1, "Address:")
        addr1 = wx.TextCtrl(pane, -1, "");
        addr2 = wx.TextCtrl(pane, -1, "");
        
        cstLbl = wx.StaticText(pane, -1, "City, State, Zip:")
        city  = wx.TextCtrl(pane, -1, "", size=(150,-1));
        state = wx.TextCtrl(pane, -1, "", size=(50,-1));
        zip   = wx.TextCtrl(pane, -1, "", size=(70,-1));
        
        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(nameLbl, 0, 
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(name, 0, wx.EXPAND)
        addrSizer.Add(addrLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(addr1, 0, wx.EXPAND)
        addrSizer.Add((5,5)) 
        addrSizer.Add(addr2, 0, wx.EXPAND)
        
        addrSizer.Add(cstLbl, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        
        cstSizer = wx.BoxSizer(wx.HORIZONTAL)
        cstSizer.Add(city, 1)
        cstSizer.Add(state, 0, wx.LEFT|wx.RIGHT, 5)
        cstSizer.Add(zip)
        addrSizer.Add(cstSizer, 0, wx.EXPAND)
        
        border = wx.BoxSizer()
        border.Add(addrSizer, 1, wx.EXPAND|wx.ALL, 5)
        pane.SetSizer(border)



