import wx

class AddNewSourcePanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,444 ), style = wx.TAB_TRAVERSAL )
        
        self.SetMinSize( wx.Size( 300,470 ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields:" ), wx.VERTICAL )
        
        self.organization_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, u'a',
                wx.DefaultPosition, wx.DefaultSize,
                style=wx.TE_NOHIDESEL)
        self.organization_txt.ShowSearchButton( False )
        self.organization_txt.ShowCancelButton( False )
        self.organization_txt.SetMinSize( wx.Size( 280,25 ) )
        self.organization_txt.SetDescriptiveText(u"Organization")
        self.organization_txt.SetForegroundColour((0,0,0))
        self.organization_txt.SetValue(u'')
        sbSizer1.Add( self.organization_txt, 0, wx.ALL, 5 )
        
        self.description_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, wx.EmptyString,
                wx.DefaultPosition, wx.DefaultSize, 0)
        self.description_txt.ShowSearchButton( False )
        self.description_txt.ShowCancelButton( False )
        self.description_txt.SetMinSize( wx.Size( 280,25 ) )
        self.description_txt.SetDescriptiveText(u"Description")
        sbSizer1.Add( self.description_txt, 0, wx.ALL, 5 )
        
        self.citation_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, wx.EmptyString,
                wx.DefaultPosition, wx.DefaultSize, 0)
        self.citation_txt.ShowSearchButton( False )
        self.citation_txt.ShowCancelButton( False )
        self.citation_txt.SetMinSize( wx.Size( 280,25 ) )
        self.citation_txt.SetDescriptiveText(u"Citation")
        sbSizer1.Add( self.citation_txt, 0, wx.ALL, 5 )
        
        self.contact_name_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, wx.EmptyString,
                wx.DefaultPosition, wx.DefaultSize, 0)
        self.contact_name_txt.ShowSearchButton( False )
        self.contact_name_txt.ShowCancelButton( False )
        self.contact_name_txt.SetDescriptiveText(u"Contact Name")
        self.contact_name_txt.SetMinSize( wx.Size( 280,25 ) )
        
        sbSizer1.Add( self.contact_name_txt, 0, wx.ALL, 5 )
        
        self.contact_addr_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, wx.EmptyString,
                wx.DefaultPosition, wx.DefaultSize, 0)
        self.contact_addr_txt.ShowSearchButton( False )
        self.contact_addr_txt.ShowCancelButton( False )
        self.contact_addr_txt.SetMinSize( wx.Size( 280,25 ) )
        self.contact_addr_txt.SetDescriptiveText(u"Contact Address")
        
        sbSizer1.Add( self.contact_addr_txt, 0, wx.ALL, 5 )
        
        self.contact_phone_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, wx.EmptyString,
                wx.DefaultPosition, wx.DefaultSize, 0)
        self.contact_phone_txt.ShowSearchButton( False )
        self.contact_phone_txt.ShowCancelButton( False )
        self.contact_phone_txt.SetMinSize( wx.Size( 280,25 ) )
        self.contact_phone_txt.SetDescriptiveText(u"Contact Phone")
        
        sbSizer1.Add( self.contact_phone_txt, 0, wx.ALL, 5 )
        
        self.contact_email_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, wx.EmptyString,
                wx.DefaultPosition, wx.DefaultSize, 0)
        self.contact_email_txt.ShowSearchButton( False )
        self.contact_email_txt.ShowCancelButton( False )
        self.contact_email_txt.SetMinSize( wx.Size( 280,25 ) )
        self.contact_email_txt.SetDescriptiveText(u"Contact Email")
        
        sbSizer1.Add( self.contact_email_txt, 0, wx.ALL, 5 )
        
        self.state_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, wx.EmptyString,
                wx.DefaultPosition, wx.DefaultSize, 0)
        self.state_txt.ShowSearchButton( False )
        self.state_txt.ShowCancelButton( False )
        self.state_txt.SetMinSize( wx.Size( 280,25 ) )
        self.state_txt.SetDescriptiveText(u"State")
        
        sbSizer1.Add( self.state_txt, 0, wx.ALL, 5 )
        
        bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.city_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, wx.EmptyString,
                wx.DefaultPosition, wx.DefaultSize, 0)
        self.city_txt.ShowSearchButton( False )
        self.city_txt.ShowCancelButton( False )
        self.city_txt.SetMinSize( wx.Size( 160,25 ) )
        self.city_txt.SetDescriptiveText(u"City")
        
        bSizer28.Add( self.city_txt, 0, wx.ALL, 5 )
        
        self.zip_txt = wx.SearchCtrl(sbSizer1.GetStaticBox(),
                wx.ID_ANY, wx.EmptyString,
                wx.DefaultPosition, wx.DefaultSize, 0)
        self.zip_txt.ShowSearchButton( False )
        self.zip_txt.ShowCancelButton( False )
        self.zip_txt.SetMinSize( wx.Size( 110,25 ) )
        self.zip_txt.SetDescriptiveText(u"Zip")
        
        bSizer28.Add( self.zip_txt, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer28, 1, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        m_comboBox1Choices = []
        self.m_comboBox1 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"ISO Metadata", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
        self.m_comboBox1.SetMinSize( wx.Size( 235,-1 ) )
        
        bSizer8.Add( self.m_comboBox1, 0, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 40,27 ), 0 )
        self.m_button2.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer8.Add( self.m_button2, 0, wx.ALL, 5 )
        
        
        sbSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        self.link_txt = wx.SearchCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.link_txt.ShowSearchButton( False )
        self.link_txt.ShowCancelButton( False )
        self.link_txt.SetMinSize( wx.Size( 280,25 ) )
        self.link_txt.SetDescriptiveText(u"Link")
        
        sbSizer2.Add( self.link_txt, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
        
        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize();
        
        bSizer1.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer1 )
        #self.Layout()
    
    def __del__( self ):
        pass
