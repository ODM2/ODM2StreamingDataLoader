import wx


from src.wizard.controller.frmRequiredValidator \
    import RequiredValidator
from src.wizard.controller.frmRequiredComboValidator \
    import RequiredComboValidator

class OrganizationPanelView(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 542,300 ), style = wx.TAB_TRAVERSAL )
        
        self.SetMinSize( wx.Size( 450,400 ) )
        
        bSizer80 = wx.BoxSizer( wx.VERTICAL )
        
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
        
        self.SetSizer( bSizer80 )
        self.Layout()
        




