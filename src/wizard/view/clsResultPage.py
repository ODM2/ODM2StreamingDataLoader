import wx
import wx.xrc
import wx.richtext as rt

###########################################################################
## Class AddNewResult
###########################################################################

class ResultPageView ( wx.Panel ):
        
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 459,540 ), style = wx.TAB_TRAVERSAL )
        
        self.SetMinSize( wx.Size( 455,540 ) )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        sbSizerSum = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Summary:" ), wx.VERTICAL )
        
        bSizerSum = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txtSum = rt.RichTextCtrl( sbSizerSum.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.STATIC_BORDER|wx.VSCROLL )
        self.txtSum.SetMinSize( wx.Size( 440,100 ) )
        
        bSizerSum.Add( self.txtSum, 0, wx.ALL, 5 )
        
        
        sbSizerSum.Add( bSizerSum, 1, wx.EXPAND, 5 )
        
        
        bSizer.Add( sbSizerSum, 1, wx.EXPAND, 5 )
        
        sbSizerReq = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Required Fields:" ), wx.VERTICAL )
        
        bSizerSamp = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticSamp = wx.StaticText( sbSizerReq.GetStaticBox(), wx.ID_ANY, u"Sampled Medium", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticSamp.Wrap( -1 )
        bSizerSamp.Add( self.staticSamp, 0, wx.ALL, 5 )
        
        
        bSizerSamp.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        comboSampChoices = []
        self.comboSamp = wx.ComboBox( sbSizerReq.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboSampChoices, 0 )
        self.comboSamp.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizerSamp.Add( self.comboSamp, 0, wx.ALL, 5 )
        
        
        sbSizerReq.Add( bSizerSamp, 0, wx.EXPAND, 5 )
        
        bSizerAgg = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticAgg = wx.StaticText( sbSizerReq.GetStaticBox(), wx.ID_ANY, u"Aggregation Statistic", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticAgg.Wrap( -1 )
        bSizerAgg.Add( self.staticAgg, 0, wx.ALL, 5 )
        
        
        bSizerAgg.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        comboAggChoices = []
        self.comboAgg = wx.ComboBox( sbSizerReq.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboAggChoices, 0 )
        self.comboAgg.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizerAgg.Add( self.comboAgg, 0, wx.ALL, 5 )
        
        
        sbSizerReq.Add( bSizerAgg, 0, wx.EXPAND, 5 )
        
        
        bSizer.Add( sbSizerReq, 1, wx.EXPAND, 5 )
        
        sbSizerOpt = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizerResultDT = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticResultDT = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Result Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticResultDT.Wrap( -1 )
        bSizerResultDT.Add( self.staticResultDT, 0, wx.ALL, 5 )
        
        
        bSizerResultDT.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.datePickerResult = wx.DatePickerCtrl( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
        self.datePickerResult.SetMinSize( wx.Size( 119,-1 ) )
        
        bSizerResultDT.Add( self.datePickerResult, 0, wx.ALL, 5 )
        
        self.staticUTCResult = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticUTCResult.Wrap( -1 )
        bSizerResultDT.Add( self.staticUTCResult, 0, wx.ALL, 5 )
        
        self.spinUTCResult = wx.SpinCtrl( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        self.spinUTCResult.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizerResultDT.Add( self.spinUTCResult, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerResultDT, 1, wx.EXPAND, 5 )
        
        bSizerValid = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticValidDT = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Valid Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticValidDT.Wrap( -1 )
        bSizerValid.Add( self.staticValidDT, 0, wx.ALL, 5 )
        
        
        bSizerValid.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.dateValidDT = wx.DatePickerCtrl( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
        self.dateValidDT.SetMinSize( wx.Size( 119,-1 ) )
        
        bSizerValid.Add( self.dateValidDT, 0, wx.ALL, 5 )
        
        self.staticUTCValid = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticUTCValid.Wrap( -1 )
        bSizerValid.Add( self.staticUTCValid, 0, wx.ALL, 5 )
        
        self.spinUTCValid = wx.SpinCtrl( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
        self.spinUTCValid.SetMinSize( wx.Size( 50,-1 ) )
        
        bSizerValid.Add( self.spinUTCValid, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerValid, 1, wx.EXPAND, 5 )
        
        bSizerStatus = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticStatus = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticStatus.Wrap( -1 )
        bSizerStatus.Add( self.staticStatus, 0, wx.ALL, 5 )
        
        
        bSizerStatus.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        comboStatusChoices = []
        self.comboStatus = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Select Status", wx.DefaultPosition, wx.DefaultSize, comboStatusChoices, 0 )
        self.comboStatus.SetMinSize( wx.Size( 260,-1 ) )
        
        bSizerStatus.Add( self.comboStatus, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerStatus, 1, wx.EXPAND, 5 )
        
        bSizerX = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticX = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"X Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticX.Wrap( -1 )
        bSizerX.Add( self.staticX, 0, wx.ALL, 5 )
        
        
        bSizerX.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.txtX = wx.TextCtrl( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtX.SetMinSize( wx.Size( 70,-1 ) )
        
        bSizerX.Add( self.txtX, 0, wx.ALL, 5 )
        
        self.staticXUnits = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Units ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticXUnits.Wrap( -1 )
        bSizerX.Add( self.staticXUnits, 0, wx.ALL, 5 )
        
        comboXUnitsChoices = []
        self.comboXUnits = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboXUnitsChoices, 0 )
        self.comboXUnits.SetMinSize( wx.Size( 115,-1 ) )
        
        bSizerX.Add( self.comboXUnits, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerX, 1, wx.EXPAND, 5 )
        
        bSizerY = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticY = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Y Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticY.Wrap( -1 )
        bSizerY.Add( self.staticY, 0, wx.ALL, 5 )
        
        
        bSizerY.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.txtY = wx.TextCtrl( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtY.SetMinSize( wx.Size( 70,-1 ) )
        
        bSizerY.Add( self.txtY, 0, wx.ALL, 5 )
        
        self.staticYUnits = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Units ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticYUnits.Wrap( -1 )
        bSizerY.Add( self.staticYUnits, 0, wx.ALL, 5 )
        
        comboYUnitsChoices = []
        self.comboYUnits = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboYUnitsChoices, 0 )
        self.comboYUnits.SetMinSize( wx.Size( 115,-1 ) )
        
        bSizerY.Add( self.comboYUnits, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerY, 1, wx.EXPAND, 5 )
        
        bSizerZ = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText24413 = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Z Location", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24413.Wrap( -1 )
        bSizerZ.Add( self.m_staticText24413, 0, wx.ALL, 5 )
        
        
        bSizerZ.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.txtZ = wx.TextCtrl( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtZ.SetMinSize( wx.Size( 70,-1 ) )
        
        bSizerZ.Add( self.txtZ, 0, wx.ALL, 5 )
        
        self.m_staticText422110 = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Units ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText422110.Wrap( -1 )
        bSizerZ.Add( self.m_staticText422110, 0, wx.ALL, 5 )
        
        comboZUnitsChoices = []
        self.comboZUnits = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboZUnitsChoices, 0 )
        self.comboZUnits.SetMinSize( wx.Size( 115,-1 ) )
        
        bSizerZ.Add( self.comboZUnits, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerZ, 1, wx.EXPAND, 5 )
        
        bSizerIntended = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText244131 = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Intended Time Spacing", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText244131.Wrap( -1 )
        bSizerIntended.Add( self.m_staticText244131, 0, wx.ALL, 5 )
        
        
        bSizerIntended.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.txtIntended = wx.TextCtrl( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtIntended.SetMinSize( wx.Size( 70,-1 ) )
        
        bSizerIntended.Add( self.txtIntended, 0, wx.ALL, 5 )
        
        self.m_staticText4221101 = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Units ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4221101.Wrap( -1 )
        bSizerIntended.Add( self.m_staticText4221101, 0, wx.ALL, 5 )
        
        comboIntendedUnitsChoices = []
        self.comboIntendedUnits = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboIntendedUnitsChoices, 0 )
        self.comboIntendedUnits.SetMinSize( wx.Size( 115,-1 ) )
        
        bSizerIntended.Add( self.comboIntendedUnits, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerIntended, 1, wx.EXPAND, 5 )
        
        
        bSizer.Add( sbSizerOpt, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer )
        self.Layout()

