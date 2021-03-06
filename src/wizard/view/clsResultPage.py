import wx
import wx.xrc
import wx.richtext as rt
import wx.lib.masked as masked

import wx.lib.agw.floatspin as FS

from src.wizard.controller.frmDigitOnly import DigitValidator
from src.wizard.controller.frmRequiredComboValidator \
    import RequiredComboValidator
###########################################################################
## Class AddNewResult
###########################################################################

class ResultPageView ( wx.Panel ):
        
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(450, 600), style=wx.TAB_TRAVERSAL)
        
        self.SetMinSize(wx.Size(450, 600))
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        sbSizerSum = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Summary:"), wx.VERTICAL )
        
        bSizerSum = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txtSum = rt.RichTextCtrl(sbSizerSum.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY | wx.STATIC_BORDER | wx.VSCROLL )
        self.txtSum.SetMinSize(wx.Size(440, 100))
        
        bSizerSum.Add(self.txtSum, 0, wx.ALL, 5)
        sbSizerSum.Add(bSizerSum, 1, wx.EXPAND, 5)
        bSizer.Add(sbSizerSum, 1, wx.EXPAND, 5)
        
        sbSizerReq = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Required Fields:"), wx.VERTICAL)
        
        bSizerSamp = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticSamp = wx.StaticText(sbSizerReq.GetStaticBox(), wx.ID_ANY, u"Sampled Medium", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticSamp.Wrap(-1)
        bSizerSamp.Add(self.staticSamp, 0, wx.ALL, 5)

        bSizerSamp.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        
        self.comboSamp = wx.ComboBox( sbSizerReq.GetStaticBox(), style=wx.CB_READONLY, validator=RequiredComboValidator())
        self.comboSamp.SetMinSize(wx.Size(280, -1))
        
        bSizerSamp.Add(self.comboSamp, 0, wx.ALL, 5)
        sbSizerReq.Add(bSizerSamp, 0, wx.EXPAND, 5)
        
        bSizerAgg = wx.BoxSizer(wx.HORIZONTAL)
        
        self.staticAgg = wx.StaticText(sbSizerReq.GetStaticBox(), wx.ID_ANY, u"Aggregation Statistic", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticAgg.Wrap(-1)
        bSizerAgg.Add(self.staticAgg, 0, wx.ALL, 5)

        bSizerAgg.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.comboAgg = wx.ComboBox( sbSizerReq.GetStaticBox(), wx.ID_ANY, style=wx.CB_READONLY, validator=RequiredComboValidator())
        self.comboAgg.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizerAgg.Add( self.comboAgg, 0, wx.ALL, 5 )
        
        
        sbSizerReq.Add( bSizerAgg, 0, wx.EXPAND, 5 )
        
        
        bSizer.Add( sbSizerReq, 1, wx.EXPAND, 5 )
        
        sbSizerOpt = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Fields:" ), wx.VERTICAL )
        
        bSizerResultDT = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticResultDT = wx.StaticText( sbSizerOpt.GetStaticBox(), label="Result Date Time")
        self.staticResultDT.Wrap(-1)
        bSizerResultDT.Add(self.staticResultDT, 0, wx.ALL, 5)

        bSizerResultDT.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        
        self.datePickerResult = wx.DatePickerCtrl(sbSizerOpt.GetStaticBox(), style=wx.DP_ALLOWNONE)
        self.datePickerResult.SetMinSize(wx.Size(160, -1))
        self.datePickerResult.SetValue(wx.DateTime().Now())
        
        bSizerResultDT.Add(self.datePickerResult, 0, wx.ALL, 5)
       
        self.timeResult = masked.TimeCtrl(sbSizerOpt.GetStaticBox(),
                                          value='00:00:00',
                                          name='time',
                                          format='HHMMSS')
    
        h = self.timeResult.GetSize().height
    
        spinner = wx.SpinButton(\
            sbSizerOpt.GetStaticBox(), wx.ID_ANY,
            wx.DefaultPosition, (-1,h), wx.SP_VERTICAL)
        spinner.SetValue(0)

        self.timeResult.BindSpinButton(spinner)
   
        self.timeResult.SetMinSize( wx.Size( 100,-1 ) )
        
        bSizerResultDT.Add( self.timeResult, 0, wx.TOP, 5 )
        bSizerResultDT.Add( spinner, 0, wx.TOP, 5 )
                 
        
        
        sbSizerOpt.Add( bSizerResultDT, 1, wx.EXPAND, 5 )
        
        bSizerValid = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticValidDT = wx.StaticText(sbSizerOpt.GetStaticBox(), label="Valid Date Time")
        self.staticValidDT.Wrap(-1)
        bSizerValid.Add(self.staticValidDT, 0, wx.ALL, 5)
        
        
        bSizerValid.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.dateValidDT = wx.DatePickerCtrl(sbSizerOpt.GetStaticBox(), style=wx.DP_ALLOWNONE)
        self.dateValidDT.SetMinSize(wx.Size(160, -1))
        self.dateValidDT.SetValue(wx.DateTime().Now())
        
        bSizerValid.Add( self.dateValidDT, 0, wx.ALL, 5 )
        
        self.timeValid = masked.TimeCtrl(sbSizerOpt.GetStaticBox(),
                                         wx.ID_ANY,
                                         '00:00:00',
                                         wx.DefaultPosition,
                                         wx.DefaultSize,
                                         wx.TE_PROCESS_TAB,
                                         validator=wx.DefaultValidator,
                                         name='time',
                                         format='HHMMSS')
    
        h = self.timeValid.GetSize().height
    
        spinner2 = wx.SpinButton(\
            sbSizerOpt.GetStaticBox(), wx.ID_ANY,
            wx.DefaultPosition, (-1,h), wx.SP_VERTICAL)
        spinner2.SetValue(0)

        self.timeValid.BindSpinButton(spinner2)
   
        self.timeValid.SetMinSize( wx.Size( 100,-1 ) )
        
        bSizerValid.Add( self.timeValid, 0, wx.TOP, 5 )
        bSizerValid.Add( spinner2, 0, wx.TOP, 5 )
        
        sbSizerOpt.Add( bSizerValid, 1, wx.EXPAND, 5 )
        
        bSizerUTC = wx.BoxSizer(wx.HORIZONTAL)
        
        self.staticUTCValid = wx.StaticText(sbSizerOpt.GetStaticBox(), label="UTC Offset")
        self.staticUTCValid.Wrap(-1)
        bSizerUTC.Add(self.staticUTCValid, 0, wx.ALL, 5)
        bSizerUTC.AddSpacer((0, 0), 1, wx.EXPAND, 5)
        
        self.spinUTCValid = wx.SpinCtrl(sbSizerOpt.GetStaticBox(), style=wx.SP_ARROW_KEYS, min=-10, max=10)
        self.spinUTCValid.SetMinSize(wx.Size(50, -1))
        self.spinUTCValid.SetRange(-12, 14)
        
        bSizerUTC.Add(self.spinUTCValid, 0, wx.ALL, 5)
        
        
        sbSizerOpt.Add( bSizerUTC, 1, wx.EXPAND, 5 )
        
        bSizerStatus = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticStatus = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticStatus.Wrap( -1 )
        bSizerStatus.Add( self.staticStatus, 0, wx.ALL, 5 )
        
        
        bSizerStatus.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.comboStatus = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, value="Select Status", style=wx.CB_READONLY)
        self.comboStatus.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizerStatus.Add( self.comboStatus, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerStatus, 1, wx.EXPAND, 5 )
        
        bSizerTax = wx.BoxSizer( wx.HORIZONTAL )
        
        staticTax = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Taxonomic Classifier", wx.DefaultPosition, wx.DefaultSize, 0)
        staticTax.Wrap(-1)
        bSizerTax.Add( staticTax, 0, wx.ALL, 5 )
        
        
        bSizerTax.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.comboTax = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, value="Select Taxonomic Classifier", style=wx.CB_READONLY)
        self.comboTax.SetMinSize( wx.Size( 280,-1 ) )
        
        bSizerTax.Add( self.comboTax, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerTax, 1, wx.EXPAND, 5 )
        
        bSizerSamp = wx.BoxSizer( wx.HORIZONTAL )

        staticSR = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Spatial References", wx.DefaultPosition, wx.DefaultSize, 0 )
        staticSR.Wrap( -1 )
        bSizerSamp.Add( staticSR, 0, wx.ALL, 5 )
    
    
        bSizerSamp.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
    
        choicesSR = []
        self.comboSR = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Select Spatial References", wx.DefaultPosition, wx.DefaultSize, choicesSR, style=wx.CB_READONLY)
        self.comboSR.SetMinSize( wx.Size( 230,-1 ))
        bSizerSamp.Add( self.comboSR, 0, wx.ALL, 5 )
        
        self.btnNewSR = wx.Button( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 40,27 ), 0 )
        self.btnNewSR.SetFont( wx.Font( 15, 70, 90, 92, False, wx.EmptyString ) )
    
        bSizerSamp.Add( self.btnNewSR, 0, wx.ALL, 5 )

        sbSizerOpt.Add( bSizerSamp, 1, wx.EXPAND, 5 )
        
        bSizerX = wx.BoxSizer( wx.HORIZONTAL )
        
        self.static_x_location = wx.StaticText(sbSizerOpt.GetStaticBox(), label="X Location")
        self.static_x_location.Wrap(-1)
        bSizerX.Add(self.static_x_location, 0, wx.ALL, 5)
        
        bSizerX.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.txtX = FS.FloatSpin(sbSizerOpt.GetStaticBox(), wx.ID_ANY,wx.DefaultPosition, wx.DefaultSize, min_val=0, max_val=9999, increment=1.00, value=0.00, agwStyle=FS.FS_LEFT)
        self.txtX.SetFormat("%f")
        self.txtX.SetDigits(3)
        self.txtX.SetMinSize( wx.Size( 70,-1 ) )
        
        bSizerX.Add( self.txtX, 0, wx.ALL, 5 )
        
        self.staticXUnits = wx.StaticText( sbSizerOpt.GetStaticBox(), label="Units")
        self.staticXUnits.Wrap( -1 )
        bSizerX.Add( self.staticXUnits, 0, wx.ALL, 5 )
        
        comboXUnitsChoices = []
        self.comboXUnits = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboXUnitsChoices, style=wx.CB_READONLY)
        self.comboXUnits.SetMinSize(wx.Size(160, -1))
        
        bSizerX.Add( self.comboXUnits, 0, wx.ALL, 5 )
        
        sbSizerOpt.Add( bSizerX, 1, wx.EXPAND, 5 )
        
        bSizerY = wx.BoxSizer( wx.HORIZONTAL )
        
        self.staticY = wx.StaticText(sbSizerOpt.GetStaticBox(), label="Y Location")
        self.staticY.Wrap(-1)
        bSizerY.Add(self.staticY, 0, wx.ALL, 5)
        
        
        bSizerY.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5)
        
        self.txtY = FS.FloatSpin( sbSizerOpt.GetStaticBox(), wx.ID_ANY,wx.DefaultPosition, wx.DefaultSize, min_val=0, max_val=9999, increment=1.00, value=0.00, agwStyle=FS.FS_LEFT)
        self.txtY.SetFormat("%f")
        self.txtY.SetDigits(3)
        self.txtY.SetMinSize( wx.Size( 70,-1 ) )
        
        bSizerY.Add( self.txtY, 0, wx.ALL, 5 )
        
        self.staticYUnits = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staticYUnits.Wrap( -1 )
        bSizerY.Add( self.staticYUnits, 0, wx.ALL, 5 )
        
        comboYUnitsChoices = []
        self.comboYUnits = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboYUnitsChoices, style=wx.CB_READONLY)
        self.comboYUnits.SetMinSize( wx.Size( 160,-1 ) )
        
        bSizerY.Add( self.comboYUnits, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerY, 1, wx.EXPAND, 5 )
        
        bSizerZ = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText24413 = wx.StaticText( sbSizerOpt.GetStaticBox(), label="Z Location")
        self.m_staticText24413.Wrap(-1)
        bSizerZ.Add(self.m_staticText24413, 0, wx.ALL, 5)
        
        
        bSizerZ.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.txtZ = FS.FloatSpin( sbSizerOpt.GetStaticBox(), wx.ID_ANY,wx.DefaultPosition, wx.DefaultSize, min_val=0, max_val=9999, increment=1.00, value=0.00, agwStyle=FS.FS_LEFT)
        self.txtZ.SetFormat("%f")
        self.txtZ.SetDigits(3)
        self.txtZ.SetMinSize( wx.Size( 70,-1 ) )

        bSizerZ.Add( self.txtZ, 0, wx.ALL, 5 )
        
        self.m_staticText422110 = wx.StaticText( sbSizerOpt.GetStaticBox(), wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText422110.Wrap( -1 )
        bSizerZ.Add( self.m_staticText422110, 0, wx.ALL, 5 )
        
        comboZUnitsChoices = []
        self.comboZUnits = wx.ComboBox( sbSizerOpt.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboZUnitsChoices, style=wx.CB_READONLY)
        self.comboZUnits.SetMinSize( wx.Size( 160,-1 ) )
        
        bSizerZ.Add( self.comboZUnits, 0, wx.ALL, 5 )
        
        
        sbSizerOpt.Add( bSizerZ, 1, wx.EXPAND, 5 )
        
        bSizerIntended = wx.BoxSizer( wx.HORIZONTAL )

        sbSizerOpt.Add( bSizerIntended, 1, wx.EXPAND, 5 )
        
        
        bSizer.Add( sbSizerOpt, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer )
        self.Layout()

