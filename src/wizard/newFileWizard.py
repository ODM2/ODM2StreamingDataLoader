# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 668,300 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Location:" ), wx.HORIZONTAL )
		
		fgSizer3 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_radioBtn1 = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Local File", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 500,-1 ), 0 )
		self.m_textCtrl2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		fgSizer3.Add( self.m_button1, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_radioBtn2 = wx.RadioButton( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Remote File", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		fgSizer3.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		fgSizer3.Add( self.m_button2, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		sbSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options:" ), wx.VERTICAL )
		
		fgSizer7 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer7.AddSpacer( ( 5, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Delimiter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer7.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 35, 0), 1, wx.EXPAND, 5 )
		
		m_choice1Choices = [ u"Comma", u"Tab", u"Custom" ]
		self.m_choice1 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		fgSizer7.Add( self.m_choice1, 0, wx.TOP, 5 )
		
		
		sbSizer2.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 2, 6, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer5.AddSpacer( ( 5, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Run Every", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		
		fgSizer5.AddSpacer( ( 33, 0), 1, wx.EXPAND, 5 )
		
		self.m_spinCtrl1 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 4 )
		fgSizer5.Add( self.m_spinCtrl1, 0, wx.TOP, 5 )
		
		
		fgSizer5.AddSpacer( ( 10, 0), 1, wx.EXPAND, 5 )
		
		m_choice2Choices = [ u"Hours", u"Minutes", wx.EmptyString ]
		self.m_choice2 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 1 )
		fgSizer5.Add( self.m_choice2, 0, wx.TOP, 5 )
		
		
		sbSizer2.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		fgSizer8 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer8.AddSpacer( ( 5, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Start Date and Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		
		fgSizer8.AddSpacer( ( 30, 0), 1, wx.EXPAND, 5 )
		
		self.m_datePicker3 = wx.DatePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer8.Add( self.m_datePicker3, 0, wx.TOP, 5 )
		
		self.m_datePicker4 = wx.DatePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer8.Add( self.m_datePicker4, 0, wx.TOP, 5 )
		
		
		sbSizer2.Add( fgSizer8, 1, wx.EXPAND, 5 )
		
		fgSizer9 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer9.AddSpacer( ( 5, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Column Headers (Line Number)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer9.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_spinCtrl2 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 10 )
		fgSizer9.Add( self.m_spinCtrl2, 0, wx.TOP, 5 )
		
		
		sbSizer2.Add( fgSizer9, 1, wx.EXPAND, 5 )
		
		fgSizer11 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer11.AddSpacer( ( 5, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Data Begins (Line Number)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer11.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		
		fgSizer11.AddSpacer( ( 25, 0), 1, wx.EXPAND, 5 )
		
		self.m_spinCtrl4 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		fgSizer11.Add( self.m_spinCtrl4, 0, wx.TOP, 5 )
		
		
		sbSizer2.Add( fgSizer11, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1010,600 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer8 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_listCtrl1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1000,400 ), wx.LC_ICON|wx.LC_REPORT|wx.LC_VIRTUAL )
		fgSizer8.Add( self.m_listCtrl1, 0, wx.ALL, 5 )
		
		fgSizer13 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Time" ), wx.HORIZONTAL )
		
		fgSizer10 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_radioBtn3 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"UTC Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
		
		m_choice3Choices = []
		self.m_choice3 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		fgSizer10.Add( self.m_choice3, 0, wx.ALL, 5 )
		
		self.m_radioBtn4 = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Local Date Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer10.Add( self.m_radioBtn4, 0, wx.ALL, 5 )
		
		m_choice4Choices = [ u"TIMESTAMP" ]
		self.m_choice4 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		fgSizer10.Add( self.m_choice4, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Time Zone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer10.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		m_choice5Choices = [ u"-7" ]
		self.m_choice5 = wx.Choice( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 0 )
		fgSizer10.Add( self.m_choice5, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( fgSizer10, 1, wx.EXPAND, 5 )
		
		
		fgSizer13.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_listCtrl3 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 750,-1 ), wx.LC_ICON|wx.LC_REPORT )
		fgSizer12.Add( self.m_listCtrl3, 0, wx.ALL, 5 )
		
		
		fgSizer13.Add( fgSizer12, 1, wx.EXPAND, 5 )
		
		
		fgSizer8.Add( fgSizer13, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer8 )
		self.Layout()
	
	def __del__( self ):
		pass
	

