import wx


from src.wizard.controller.frmRequiredValidator \
    import RequiredValidator
from src.wizard.controller.frmRequiredComboValidator \
    import RequiredComboValidator

class AffiliationPanelView(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 542,300 ), style = wx.TAB_TRAVERSAL )
        
        self.SetMinSize( wx.Size( 450,400 ) )
        
        bSizer80 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer221 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required:" ), wx.VERTICAL )
        
        bSizer351 = wx.BoxSizer( wx.HORIZONTAL )
        
        lblPerson = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, 
            u"Person:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblPerson.Wrap( -1 )
        bSizer351.Add(lblPerson, 0, wx.ALL, 5 )
        
        bSizer351.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.textPerson = wx.TextCtrl(sbSizer221.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), 0)
        self.textPerson.Enable(False)
        bSizer351.Add(self.textPerson, 0, wx.ALL, 5)
        
        
        sbSizer221.Add( bSizer351, 0, wx.EXPAND, 5 ) #denver
        
        newOrgSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        lblStart = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, 
            u"Start Date:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblStart.Wrap( -1 )
        newOrgSizer.Add(lblStart, 0, wx.ALL, 5 )
        
        newOrgSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
       
        self.dateStart = wx.DatePickerCtrl( sbSizer221.GetStaticBox(),
            wx.ID_ANY, wx.DefaultDateTime,
            wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )  
        
        newOrgSizer.Add( self.dateStart, 0, wx.ALL, 5 )
        sbSizer221.Add(newOrgSizer, 0, wx.EXPAND, 5) #Denver
        
        newOrgSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        
        lblEmail = wx.StaticText( sbSizer221.GetStaticBox(), wx.ID_ANY, 
            u"E-Mail:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblEmail.Wrap( -1 )
        newOrgSizer1.Add(lblEmail, 0, wx.ALL, 5 )
        newOrgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
       
        self.textEmail = wx.TextCtrl(sbSizer221.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), validator=RequiredValidator())
        newOrgSizer1.Add(self.textEmail, 0, wx.ALL, 5)
        

        sbSizer221.Add(newOrgSizer1, 0, wx.EXPAND, 5 ) # Denver
        bSizer80.Add( sbSizer221, 0, wx.EXPAND, 5 )
        
        sbOptional = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional:" ), wx.VERTICAL )
        
        bSizerOrg = wx.BoxSizer( wx.HORIZONTAL )
        
        lblOrg = wx.StaticText( sbOptional.GetStaticBox(), wx.ID_ANY, 
            u"Organization:", wx.DefaultPosition, wx.DefaultSize, 0)
        lblOrg.Wrap( -1 )
        bSizerOrg.Add(lblOrg, 0, wx.ALL, 5 )
        
        bSizerOrg.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.textOrg = wx.TextCtrl(sbOptional.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), 0)
        self.textOrg.Enable(False)
        bSizerOrg.Add(self.textOrg, 0, wx.ALL, 5)
        
        sbOptional.Add(bSizerOrg, 0, wx.EXPAND, 5)
        
        bSizerOrg2 = wx.BoxSizer( wx.HORIZONTAL )
        
        lblPrimary = wx.StaticText( sbOptional.GetStaticBox(), wx.ID_ANY, 
            u"Primary Contact", wx.DefaultPosition, wx.DefaultSize, 0)
        lblPrimary.Wrap( -1 )
        bSizerOrg2.Add(lblPrimary, 0, wx.ALL, 5 )
        
        bSizerOrg2.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.checkPrimary = wx.CheckBox(sbOptional.GetStaticBox(), wx.ID_ANY)
        self.checkPrimary.SetValue(False)
        bSizerOrg2.Add(self.checkPrimary, 0, wx.ALL, 5)
        
        sbOptional.Add(bSizerOrg2, 0, wx.EXPAND, 5)
        
        bSizerOrg3 = wx.BoxSizer( wx.HORIZONTAL )
        
        lblEnd = wx.StaticText( sbOptional.GetStaticBox(), wx.ID_ANY, 
            u"End Date", wx.DefaultPosition, wx.DefaultSize, 0)
        lblEnd.Wrap( -1 )
        bSizerOrg3.Add(lblEnd, 0, wx.ALL, 5 )
        
        bSizerOrg3.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.dateEnd = wx.DatePickerCtrl( sbOptional.GetStaticBox(),
            wx.ID_ANY, wx.DefaultDateTime,
            wx.DefaultPosition, wx.DefaultSize, wx.DP_ALLOWNONE )  
        self.dateEnd.SetValue(wx.DateTime())
        bSizerOrg3.Add(self.dateEnd, 0, wx.ALL, 5 )
        
        sbOptional.Add(bSizerOrg3, 0, wx.EXPAND, 5)
        
        bSizerOrg4 = wx.BoxSizer( wx.HORIZONTAL )
        
        lblPhone = wx.StaticText( sbOptional.GetStaticBox(), wx.ID_ANY, 
            u"Phone Number", wx.DefaultPosition, wx.DefaultSize, 0)
        lblPhone.Wrap( -1 )
        bSizerOrg4.Add(lblPhone, 0, wx.ALL, 5 )
        
        bSizerOrg4.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.textPhone = wx.TextCtrl(sbOptional.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), 0)
        bSizerOrg4.Add(self.textPhone, 0, wx.ALL, 5 )
        
        sbOptional.Add(bSizerOrg4, 0, wx.EXPAND, 5)
        
        bSizerOrg5 = wx.BoxSizer( wx.HORIZONTAL )
        
        lblAddr = wx.StaticText( sbOptional.GetStaticBox(), wx.ID_ANY, 
            u"Address", wx.DefaultPosition, wx.DefaultSize, 0)
        lblAddr.Wrap( -1 )
        bSizerOrg5.Add(lblAddr, 0, wx.ALL, 5 )
        
        bSizerOrg5.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.textAddr = wx.TextCtrl(sbOptional.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), 0)
        bSizerOrg5.Add(self.textAddr, 0, wx.ALL, 5 )
        
        sbOptional.Add(bSizerOrg5, 0, wx.EXPAND, 5)

        bSizerOrg6 = wx.BoxSizer( wx.HORIZONTAL )
        
        lblLink = wx.StaticText( sbOptional.GetStaticBox(), wx.ID_ANY, 
            u"Person Link", wx.DefaultPosition, wx.DefaultSize, 0)
        lblLink.Wrap( -1 )
        bSizerOrg6.Add(lblLink, 0, wx.ALL, 5 )
        
        bSizerOrg6.AddSpacer((0,0), 1, wx.EXPAND, 5)
        
        self.textLink = wx.TextCtrl(sbOptional.GetStaticBox(), wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition, wx.Size(280,-1), 0)
        bSizerOrg6.Add(self.textLink, 0, wx.ALL, 5 )
        
        sbOptional.Add(bSizerOrg6, 0, wx.EXPAND, 5)
        
        bSizer80.Add( sbOptional, 0, wx.EXPAND, 5 )
        self.SetSizer( bSizer80 )
        self.Layout()
        




