import wx
from src.wizard.controller.frmDigitOnly import DigitValidator
from src.wizard.controller.frmRequiredValidator import RequiredValidator

class AddNewSampFeatPanelView ( wx.Panel ):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 459,626 ), style = wx.TAB_TRAVERSAL )
                
        self.SetMinSize( wx.Size( 459,626 ) )
        self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)        
        bSizer111 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer25 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields:" ), wx.VERTICAL )
        
        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
        
        #self.m_staticText35 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Sampling Feature UUID", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_staticText35.Wrap( -1 )
        #bSizer41.Add( self.m_staticText35, 0, wx.ALL, 5 )
        
        
        bSizer41.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        #self.m_textCtrl30 = wx.TextCtrl( sbSizer25.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_textCtrl30.Enable( False )
        
        #bSizer41.Add( self.m_textCtrl30, 0, wx.ALL, 5 )
        
        
        sbSizer25.Add( bSizer41, 1, wx.EXPAND, 5 )
        
        bSizer411 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText351 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Sampling Feature Code", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText351.Wrap( -1 )
        bSizer411.Add( self.m_staticText351, 0, wx.ALL, 5 )
        
        
        bSizer411.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl301 = wx.TextCtrl( sbSizer25.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, validator=RequiredValidator() )
        self.m_textCtrl301.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer411.Add( self.m_textCtrl301, 0, wx.ALL, 5 )
        
        
        sbSizer25.Add( bSizer411, 1, wx.EXPAND, 5 )
        
        bSizer532 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText422 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Sampling Feature Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText422.Wrap( -1 )
        bSizer532.Add( self.m_staticText422, 0, wx.ALL, 5 )
        
        
        bSizer532.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl30 = wx.TextCtrl( sbSizer25.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl30.Enable(False)
        self.m_textCtrl30.SetMinSize( wx.Size( 280,-1 ) )

        #m_comboBox82Choices = []
        #self.m_comboBox82 = wx.ComboBox( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Select Sampling Feature Type", wx.DefaultPosition, wx.DefaultSize, m_comboBox82Choices, 0 )
        #self.m_comboBox82.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer532.Add( self.m_textCtrl30, 0, wx.ALL, 5 )
        
        
        sbSizer25.Add( bSizer532, 1, wx.EXPAND, 5 )
        
        bSizer53 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Site Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42.Wrap( -1 )
        bSizer53.Add( self.m_staticText42, 0, wx.ALL, 5 )
        
        
        bSizer53.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox8Choices = []
        self.m_comboBox8 = wx.ComboBox( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Select Site Type", wx.DefaultPosition, wx.DefaultSize, m_comboBox8Choices, style=wx.CB_READONLY )
        self.m_comboBox8.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer53.Add( self.m_comboBox8, 0, wx.ALL, 5 )
        
        
        sbSizer25.Add( bSizer53, 1, wx.EXPAND, 5 )
        
        bSizer68 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText52 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText52.Wrap( -1 )
        bSizer68.Add( self.m_staticText52, 0, wx.ALL, 5 )
        
        
        bSizer68.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl35 = wx.TextCtrl( sbSizer25.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 , validator=DigitValidator())
        self.m_textCtrl35.SetMinSize( wx.Size( 102,-1 ) )
        
        bSizer68.Add( self.m_textCtrl35, 0, wx.ALL, 5 )
        
        self.m_staticText53 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText53.Wrap( -1 )
        bSizer68.Add( self.m_staticText53, 0, wx.ALL, 5 )
        
        self.m_textCtrl36 = wx.TextCtrl( sbSizer25.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 , validator=DigitValidator())
        self.m_textCtrl36.SetMinSize( wx.Size( 102,-1 ) )
        
        bSizer68.Add( self.m_textCtrl36, 0, wx.ALL, 5 )
        
        
        sbSizer25.Add( bSizer68, 1, wx.EXPAND, 5 )
        
        bSizer5322 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4222 = wx.StaticText( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Spatial References", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4222.Wrap( -1 )
        bSizer5322.Add( self.m_staticText4222, 0, wx.ALL, 5 )
        
        
        bSizer5322.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox822Choices = []
        self.m_comboBox822 = wx.ComboBox( sbSizer25.GetStaticBox(), wx.ID_ANY, u"Select Spatial References", wx.DefaultPosition, wx.DefaultSize, m_comboBox822Choices, style=wx.CB_READONLY)
        self.m_comboBox822.SetMinSize( wx.Size( 230,-1 ) )
        
        bSizer5322.Add( self.m_comboBox822, 0, wx.ALL, 5 )
        
        self.m_button411 = wx.Button( sbSizer25.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 40,27 ), 0 )
        self.m_button411.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
        
        bSizer5322.Add( self.m_button411, 0, wx.ALL, 5 )
        
        
        sbSizer25.Add( bSizer5322, 1, wx.EXPAND, 5 )
        
        
        bSizer111.Add( sbSizer25, 1, wx.EXPAND, 5 )
        
        sbSizer24 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizer412 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText352 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Sampling Feature Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText352.Wrap( -1 )
        bSizer412.Add( self.m_staticText352, 0, wx.ALL, 5 )
        
        
        bSizer412.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl302 = wx.TextCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl302.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer412.Add( self.m_textCtrl302, 0, wx.ALL, 5 )
        
        
        sbSizer24.Add( bSizer412, 1, wx.EXPAND, 5 )
        
        bSizer5321 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4221 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Sampling Feature Geotype", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4221.Wrap( -1 )
        bSizer5321.Add( self.m_staticText4221, 0, wx.ALL, 5 )
        
        
        bSizer5321.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        #m_comboBox821Choices = []
        #self.m_comboBox821 = wx.ComboBox( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Select Sampling Feature Geotype", wx.DefaultPosition, wx.DefaultSize, m_comboBox821Choices, 0 )
        #self.m_comboBox821.SetMinSize( wx.Size( 280,-1 ) )
        
        self.m_geotypeTxt = wx.TextCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_geotypeTxt.Enable( False )
        self.m_geotypeTxt.SetMinSize( wx.Size( 280,-1 ) )
        bSizer5321.Add( self.m_geotypeTxt, 0, wx.ALL, 5 )
        
        sbSizer24.Add( bSizer5321, 1, wx.EXPAND, 5 )
        
        bSizer4121 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3521 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Feature Geometry", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3521.Wrap( -1 )
        bSizer4121.Add( self.m_staticText3521, 0, wx.ALL, 5 )
        
        
        bSizer4121.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl3021 = wx.TextCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl3021.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer4121.Add( self.m_textCtrl3021, 0, wx.ALL, 5 )
        
        
        sbSizer24.Add( bSizer4121, 1, wx.EXPAND, 5 )
        
        bSizer4122 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3522 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Elevation_m", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3522.Wrap( -1 )
        bSizer4122.Add( self.m_staticText3522, 0, wx.ALL, 5 )
        
        
        bSizer4122.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl3022 = wx.TextCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 , validator=RequiredValidator())
        self.m_textCtrl3022.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer4122.Add( self.m_textCtrl3022, 0, wx.ALL, 5 )
        
        
        sbSizer24.Add( bSizer4122, 1, wx.EXPAND, 5 )
        
        bSizer53211 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText42211 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Elevation Datum", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42211.Wrap( -1 )
        bSizer53211.Add( self.m_staticText42211, 0, wx.ALL, 5 )
        
        
        bSizer53211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_comboBox8211Choices = []
        self.m_comboBox8211 = wx.ComboBox( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Select Elevation Datum", wx.DefaultPosition, wx.DefaultSize, m_comboBox8211Choices, wx.CB_READONLY)
        self.m_comboBox8211.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer53211.Add( self.m_comboBox8211, 0, wx.ALL, 5 )
        
        
        sbSizer24.Add( bSizer53211, 1, wx.EXPAND, 5 )
        
        bSizer413 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText353 = wx.StaticText( sbSizer24.GetStaticBox(), wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText353.Wrap( -1 )
        bSizer413.Add( self.m_staticText353, 0, wx.ALL, 5 )
        
        
        bSizer413.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl303 = wx.TextCtrl( sbSizer24.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_textCtrl303.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizer413.Add( self.m_textCtrl303, 0, wx.ALL, 5 )
        
        
        sbSizer24.Add( bSizer413, 1, wx.EXPAND, 5 )
        
        
        bSizer111.Add( sbSizer24, 1, wx.EXPAND, 5 )
        
        m_sdbSizer11 = wx.StdDialogButtonSizer()
        self.m_sdbSizer11OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer11.AddButton( self.m_sdbSizer11OK )
        self.m_sdbSizer11Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer11.AddButton( self.m_sdbSizer11Cancel )
        m_sdbSizer11.Realize();
        
        bSizer111.Add( m_sdbSizer11, 1, wx.EXPAND, 5 )
        
        self.Bind(wx.EVT_BUTTON, self.onOK, self.m_sdbSizer11OK)

        self.SetSizer( bSizer111 )
        self.Layout() 
    
    def __del__( self ):
        pass

    def onOK(self, event):
        event.Skip()


class TestFrame(wx.Frame):
    def __init__(self, parent):
         wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
         self.panel = AddNewSampFeatPanelView(self)
if __name__ == '__main__':
    app = wx.App()
    frame = TestFrame(None)
    frame.Show()
    app.MainLoop()

