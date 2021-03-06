import wx

try:
    from agw import pycollapsiblepane as PCP
except ImportError:
    import wx.lib.agw.pycollapsiblepane as PCP

from src.wizard.controller.frmRequiredValidator \
    import RequiredValidator
from src.wizard.controller.frmRequiredComboValidator \
    import RequiredComboValidator

class NewAffiliationView(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 542,300 ), style = wx.TAB_TRAVERSAL )
        
        self.SetMinSize( wx.Size( 442,550 ) )
        
        bSizer80 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Person:" ), wx.VERTICAL )
        
        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText31 = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Existing person", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        bSizer35.Add( self.m_staticText31, 0, wx.ALL, 5 )
        
        
        bSizer35.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox13Choices = []
        self.m_comboBox13 = wx.ComboBox( sbSizer22.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, m_comboBox13Choices, 0 )
        self.m_comboBox13.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer35.Add( self.m_comboBox13, 0, wx.ALL, 5 )
        
        
        sbSizer22.Add( bSizer35, 0, wx.EXPAND, 10 ) # Denver

        newPersonSizer = wx.BoxSizer( wx.VERTICAL )
        firstMiddleSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        lblFirst = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"First Name:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        firstMiddleSizer.Add(lblFirst, 0, wx.ALL, 5)
        
        firstMiddleSizer.AddSpacer((0,0), 1, wx.EXPAND, 5)

        self.textFirst = wx.TextCtrl(sbSizer22.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(100,-1), validator=RequiredValidator())
        firstMiddleSizer.Add(self.textFirst, 0, wx.ALL, 5)
        
        lblMiddle = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Middle:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        firstMiddleSizer.Add(lblMiddle, 0, wx.ALL, 5)
        
        self.textMiddle = wx.TextCtrl(sbSizer22.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(100,-1), 0)
        firstMiddleSizer.Add(self.textMiddle, 0, wx.ALL, 5)
        
        newPersonSizer.Add(firstMiddleSizer, 0, wx.EXPAND, 5) #denver

        lastSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        lblLast = wx.StaticText( sbSizer22.GetStaticBox(), wx.ID_ANY, u"Last Name:",
            wx.DefaultPosition, wx.DefaultSize, 0)
        lastSizer.Add(lblLast, 0, wx.ALL, 5)
        
        lastSizer.AddSpacer((0,0), 1, wx.EXPAND, 5)

        self.textLast = wx.TextCtrl(sbSizer22.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), validator=RequiredValidator())
        lastSizer.Add(self.textLast, 0, wx.ALL, 5)
        
        newPersonSizer.Add(lastSizer, 0, wx.EXPAND, 5) # Denver

        sbSizer22.Add(newPersonSizer, 0, wx.EXPAND, 5) # Denver
        #self.cp = cp = PCP.PyCollapsiblePane(self, wx.ID_ANY, "Add new person...", agwStyle=wx.CP_GTK_EXPANDER, style=wx.CP_DEFAULT_STYLE)
        #self.MakePaneContent(cp.GetPane())
                        
        #cpSizer.Add( cp, 1, wx.LEFT|wx.EXPAND, 25 )
        #sbSizer22.Add( cpSizer, 1, wx.EXPAND|wx.GROW, 5)
        
        
        bSizer80.Add( sbSizer22, 0, wx.EXPAND, 5 ) # Denver
        
        sbSizer221 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Orgnaization:" ), wx.VERTICAL )
        
        bSizer351 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText311 = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, u"Existing organization", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText311.Wrap( -1 )
        bSizer351.Add( self.m_staticText311, 0, wx.ALL, 5 )
        
        
        bSizer351.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox131Choices = []
        self.m_comboBox131 = wx.ComboBox( sbSizer221.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, m_comboBox131Choices, 0 )
        self.m_comboBox131.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer351.Add( self.m_comboBox131, 0, wx.ALL, 5 )
        
        
        sbSizer221.Add( bSizer351, 0, wx.EXPAND, 5 ) #denver
        
        newOrgSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        lblType = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, 
            u"Type:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblType.Wrap( -1 )
        newOrgSizer.Add(lblType, 0, wx.ALL, 5 )
        
        newOrgSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        typeChoices = []
        self.orgTypeCombo = wx.ComboBox( sbSizer221.GetStaticBox(), wx.ID_ANY,
            u"Select Type", wx.DefaultPosition, wx.DefaultSize,
            typeChoices, validator=RequiredComboValidator() )
        self.orgTypeCombo.SetMinSize(wx.Size( 280,-1 ) )
        
        newOrgSizer.Add( self.orgTypeCombo, 0, wx.ALL, 5 )
        sbSizer221.Add(newOrgSizer, 0, wx.EXPAND, 5) #Denver
        
        newOrgSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        
        lblCode = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, 
            u"Code:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblCode.Wrap( -1 )
        newOrgSizer1.Add(lblCode, 0, wx.ALL, 5 )
        newOrgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
       
        self.textCode = wx.TextCtrl(sbSizer221.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), validator=RequiredValidator())
        newOrgSizer1.Add(self.textCode, 0, wx.ALL, 5)
        

        sbSizer221.Add(newOrgSizer1, 0, wx.EXPAND, 5 ) # Denver
        
        newOrgSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        lblName = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, 
            u"Name:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblName.Wrap( -1 )
        newOrgSizer2.Add(lblName, 0, wx.ALL, 5 )
        
        newOrgSizer2.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.textName = wx.TextCtrl(sbSizer221.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), validator=RequiredValidator())
        newOrgSizer2.Add(self.textName, 0, wx.ALL, 5)
        
        sbSizer221.Add(newOrgSizer2, 0, wx.EXPAND, 5) #Denevr
        
        newOrgSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        
        lblDesc = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, 
            u"Description:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblName.Wrap(-1)
        newOrgSizer3.Add(lblDesc, 0, wx.ALL, 5 )
        
        newOrgSizer3.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.textDesc = wx.TextCtrl(sbSizer221.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,70), wx.TE_MULTILINE)
        newOrgSizer3.Add(self.textDesc, 0, wx.ALL, 5)
        
        sbSizer221.Add(newOrgSizer3, 0, wx.EXPAND, 5) #Denver
        
        newOrgSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        lblLink = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, 
            u"Link:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblLink.Wrap(-1)
        newOrgSizer4.Add(lblLink, 0, wx.ALL, 5 )
        
        newOrgSizer4.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.textLink = wx.TextCtrl(sbSizer221.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), 0)
        newOrgSizer4.Add(self.textLink, 0, wx.ALL, 5)
        
        sbSizer221.Add(newOrgSizer4, 0, wx.EXPAND, 5) # Denver
        
        newOrgSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        lblParent = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, 
            u"Parent Organization:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblParent.Wrap(-1)
        newOrgSizer5.Add(lblParent, 0, wx.ALL, 5 )
        
        newOrgSizer5.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.comboParent = wx.ComboBox(sbSizer221.GetStaticBox(), wx.ID_ANY, u"Select Parent Organization", wx.DefaultPosition, wx.DefaultSize, [], 0)
        self.comboParent.SetMinSize(wx.Size(280,-1))
        newOrgSizer5.Add(self.comboParent, 0, wx.ALL, 5)
        
        sbSizer221.Add(newOrgSizer5, 0, wx.EXPAND, 5)
        bSizer80.Add( sbSizer221, 0, wx.EXPAND, 5 )
        
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



