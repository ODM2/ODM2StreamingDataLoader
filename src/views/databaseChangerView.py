__author__ = 'Jacob'
# -*- coding: utf-8 -*-

# ##########################################################################
# # Python code generated with wxFormBuilder (version Feb 26 2014)
# # http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.propgrid as wxpg

import logging
from src.common.logger import LoggerTool

tool = LoggerTool()
logger = tool.setupLogger(__name__, __name__ + '.log', 'w', logging.DEBUG)

###########################################################################
## Class DatabaseChanger
###########################################################################

ID_CreateTree = wx.ID_HIGHEST + 1
ID_CreateGrid = ID_CreateTree + 1
ID_CreateText = ID_CreateTree + 2
ID_CreateHTML = ID_CreateTree + 3
ID_CreateNotebook = ID_CreateTree + 4
ID_CreateSizeReport = ID_CreateTree + 5
ID_GridContent = ID_CreateTree + 6
ID_TextContent = ID_CreateTree + 7
ID_TreeContent = ID_CreateTree + 8
ID_HTMLContent = ID_CreateTree + 9
ID_NotebookContent = ID_CreateTree + 10
ID_SizeReportContent = ID_CreateTree + 11


class DatabaseChangerView(wx.Panel):
    def __init__(self, param):
        wx.Panel.__init__(self, parent=param['parent'], id=param['id'], pos=wx.DefaultPosition, size=wx.Size(663, 390),
                          style=wx.TAB_TRAVERSAL)

        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        self.saveBtn = wx.Button(self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_mgr.AddPane(self.saveBtn,
                           wx.aui.AuiPaneInfo().Bottom().CaptionVisible(False).CloseButton(False).PaneBorder(
                               False).Movable(False).Dock().Resizable().FloatingSize(wx.Size(104, 60)).DockFixed(
                               False).TopDockable(False).LeftDockable(False).RightDockable(False).Floatable(False).Row(
                               1))

        self.nextBtn = wx.Button(self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_mgr.AddPane(self.nextBtn, wx.aui.AuiPaneInfo().Bottom().CaptionVisible(False).CloseButton(False).Movable(
            False).Dock().Resizable().FloatingSize(wx.Size(104, 60)).DockFixed(False).TopDockable(False).LeftDockable(
            False).RightDockable(False).Floatable(False).Row(1))

        # WARNING: wxPython code generation isn't supported for this widget yet.
        self.m_propertyGridManager1 = pg = wxpg.PropertyGridManager(self,
                                                                    style=wxpg.PG_SPLITTER_FROM_AUTO_CENTER | wxpg.PG_TOOLBAR)

        self.m_mgr.AddPane(self.m_propertyGridManager1,
                           wx.aui.AuiPaneInfo().Center().CaptionVisible(False).CloseButton(False).Movable(
                               False).Dock().Resizable().FloatingSize(wx.Size(460, 361)).DockFixed(
                               False).BottomDockable(False).TopDockable(False).LeftDockable(False).RightDockable(
                               False).Floatable(False))
        self._exampleLayout(self.m_propertyGridManager1)
        self.m_mgr.Update()

        # Connect Events
        self.saveBtn.Bind(wx.EVT_BUTTON, self.mybuttonclick)


    def _exampleLayout(self, pg):
        pg.AddPage("Page 1 - Testing All")

        pg.Append(wxpg.PropertyCategory("1 - File Properties"))
        pg.Append(wxpg.FileProperty("File", value=""))

        pg.Append(wxpg.EnumProperty("Delimiter", "Enum", ['<Comma Delimited>', '<Tab Delimited>'], [10, 11], 10))

        #pg.Append(wxpg.StringProperty("String", value="Some Text"))
        #pg.Append(wxpg.IntProperty("Int", value=100))
        #pg.Append(wxpg.FloatProperty("Float", value=100.0))
        #pg.Append(wxpg.BoolProperty("Bool", value=True))
        #pg.Append(wxpg.BoolProperty("Bool_with_Checkbox", value=True))
        #pg.SetPropertyAttribute("Bool_with_Checkbox", "UseCheckbox", True)

        pg.Append(wxpg.PropertyCategory("2 - Database Properties"))
        pg.Append(
            wxpg.LongStringProperty("LongString", value="This is a\\nmulti-line string\\nwith\\ttabs\\nmixed\\tin."))
        pg.Append(wxpg.DirProperty("Dir", value="C:\\Windows"))
        pg.Append(wxpg.ArrayStringProperty("ArrayString", value=['A', 'B', 'C']))

        pg.Append(wxpg.EditEnumProperty("EditEnum", "EditEnumProperty", ['A', 'B', 'C'], [0, 1, 2], "Text Not in List"))

        pg.Append(wxpg.PropertyCategory("3 - Advanced Properties"))
        pg.Append(wxpg.DateProperty("Date", value=wx.DateTime_Now()))
        pg.Append(wxpg.SystemColourProperty("SystemColour"))
        pg.Append(wxpg.ImageFileProperty("ImageFile"))
        pg.Append(wxpg.MultiChoiceProperty("MultiChoice", choices=['wxWidgets', 'QT', 'GTK+']))


    #def __del__(self):
    #    self.m_mgr.UnInit()



    # Virtual event handlers, overide them in your derived class
    def mybuttonclick(self, event):
        event.Skip()


def create(parent):
    name = u'test_databaseChangerview'
    title = u'test_databaseChangerview'
    return MainFrame(parent, name, title)


class MainFrame(wx.Frame):
    def __init__(self, parent, name, title):
        wx.Frame.__init__(self, id=wx.ID_ANY, name=name, parent=parent, size=wx.Size(663, 390),
                          style=wx.DEFAULT_FRAME_STYLE, title=title)
        param = {}
        param['id'] = wx.ID_ANY
        param['parent'] = self
        param['name'] = u'test_databaseChangerview'
        param['size'] = wx.Size(663, 390)
        param['style'] = None

        view = DatabaseChangerView(param)

        self._createMenubar()

    def _createMenubar(self):
        print "Making Menu"
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

if __name__ == "__main__":
    app = wx.App(False)
    frame = create(None)
    frame.Show()
    app.MainLoop()
'''
[wxID_FRMDBCONFIG, wxID_FRMDBCONFIGBOXCONNECTION, wxID_FRMDBCONFIGBTNCANCEL,
 wxID_FRMDBCONFIGBTNSAVE, wxID_FRMDBCONFIGBTNTEST, wxID_FRMDBCONFIGdbComboBox,
 wxID_FRMDBCONFIGLBLDBNAME, wxID_FRMDBCONFIGLBLDBTYPE, wxID_FRMDBCONFIGLBLPASS,
 wxID_FRMDBCONFIGLBLSERVER, wxID_FRMDBCONFIGLBLUSER, wxID_FRMDBCONFIGPNLCONNECTION,
 wxID_FRMDBCONFIGPNLMAIN, wxID_FRMDBCONFIGTXTDBNAME, wxID_FRMDBCONFIGTXTPASS,
 wxID_FRMDBCONFIGTXTSERVER, wxID_FRMDBCONFIGTXTUSER, wxID_FRAME1BOXCONNECTION,
 wxID_FRAME1LBLUSER, wxID_FRAME1TXTPASS, wxID_FRAME1LBLDBNAME, wxID_FRAME1TXTSERVER
] = [wx.NewId() for _init_ctrls in range(22)]


class DatabaseChangerView(wx.Panel):
    def __init__(self, dict):
        wx.Panel.__init__(self, id=dict['id'], parent=dict['parent'], name=dict['name'], size=dict['size'])
        self._init_ctrls(dict['parent'])

    def _init_coll_boxSizer3_Items(self, parent):
        # generated method, don't edit
        parent.AddWindow(self.lblDbType, 25, border=5, flag=wx.ALL | wx.GROW)
        parent.AddWindow(self.dbComboBox, 75, border=5, flag=wx.GROW | wx.ALL)

    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit
        parent.AddSizer(self.boxSizer3, 17, border=5, flag=wx.GROW | wx.ALL)
        parent.AddWindow(self.pnlConnection, 66, border=5, flag=wx.GROW | wx.ALL)
        parent.AddSizer(self.boxSizer2, 17, border=5, flag=wx.ALL | wx.GROW)

    def _init_coll_boxSizer2_Items(self, parent):
        # generated method, don't edit
        parent.AddWindow(self.btnTest, 33, border=5, flag=wx.GROW | wx.ALL)
        parent.AddWindow(self.btnSave, 33, border=5, flag=wx.ALL | wx.GROW)
        parent.AddWindow(self.btnCancel, 33, border=5, flag=wx.GROW | wx.ALL)

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.boxSizer2 = wx.BoxSizer(orient=wx.HORIZONTAL)
        self.boxSizer3 = wx.BoxSizer(orient=wx.HORIZONTAL)

        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_boxSizer2_Items(self.boxSizer2)
        self._init_coll_boxSizer3_Items(self.boxSizer3)

        self.pnlMain.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        self.pnlMain = wx.Panel(id=wxID_FRMDBCONFIGPNLMAIN, name=u'pnlMain',
                                parent=self, pos=wx.Point(0, 0), size=wx.Size(457, 270),
                                style=wx.TAB_TRAVERSAL)

        self.lblDbType = wx.StaticText(id=wxID_FRMDBCONFIGLBLDBTYPE,
                                       label=u'Connection Type:', name=u'lblDbType', parent=self.pnlMain,
                                       pos=wx.Point(10, 10), size=wx.Size(101, 25), style=0)

        self.dbComboBox = wx.ComboBox(choices=["Microsoft SQL Server", "MySQL"], id=wxID_FRMDBCONFIGdbComboBox,
                                      name='dbComboBox', parent=self.pnlMain, pos=wx.Point(121, 10),
                                      size=wx.Size(326, 21), style=0,
                                      value=u'')
        # self.dbComboBox.SetLabel(u'Microsoft SQL Server')

        self.btnTest = wx.Button(id=wxID_FRMDBCONFIGBTNTEST,
                                 label=u'Test Connection', name=u'btnTest', parent=self.pnlMain,
                                 pos=wx.Point(10, 233), size=wx.Size(139, 27), style=0)

        self.btnSave = wx.Button(id=wxID_FRMDBCONFIGBTNSAVE,
                                 label=u'Save Connection', name=u'btnSave', parent=self.pnlMain,
                                 pos=wx.Point(159, 233), size=wx.Size(139, 27), style=0)

        self.btnCancel = wx.Button(id=wxID_FRMDBCONFIGBTNCANCEL,
                                   label=u'Cancel', name=u'btnCancel', parent=self.pnlMain,
                                   pos=wx.Point(308, 233), size=wx.Size(139, 27), style=0)

        self.pnlConnection = wx.Panel(id=wxID_FRMDBCONFIGPNLCONNECTION,
                                      name=u'pnlConnection', parent=self.pnlMain, pos=wx.Point(5, 50),
                                      size=wx.Size(447, 168), style=wx.TAB_TRAVERSAL)

        self.boxConnection = wx.StaticBox(id=wxID_FRAME1BOXCONNECTION,
                                          label=u'Microsoft SQL Server', name=u'boxConnection',
                                          parent=self.pnlConnection, pos=wx.Point(8, 8), size=wx.Size(432, 152),
                                          style=0)

        # ----------------------------

        self.lblServer = wx.StaticText(id=wxID_FRMDBCONFIGLBLSERVER,
                                       label=u'Server Address:', name=u'lblServer',
                                       parent=self.pnlConnection, pos=wx.Point(64, 40), size=wx.Size(79, 16), style=0)

        self.txtServer = wx.TextCtrl(id=wxID_FRAME1TXTSERVER, name=u'txtServer',
                                     parent=self.pnlConnection, pos=wx.Point(160, 32),
                                     size=wx.Size(248, 21), style=0, value=u'')

        self.lblDBName = wx.StaticText(id=wxID_FRAME1LBLDBNAME,
                                       label=u'Database Name:', name=u'lblDBName',
                                       parent=self.pnlConnection, pos=wx.Point(64, 72), size=wx.Size(81, 13), style=0)

        self.txtDBName = wx.TextCtrl(id=wxID_FRMDBCONFIGTXTDBNAME,
                                     name=u'txtDBName', parent=self.pnlConnection, pos=wx.Point(160, 64),
                                     size=wx.Size(248, 21), style=0, value=u'')

        self.lblUser = wx.StaticText(id=wxID_FRAME1LBLUSER,
                                     label=u'User ID:', name=u'lblUser',
                                     parent=self.pnlConnection, pos=wx.Point(64, 104), size=wx.Size(76, 13), style=0)

        self.txtUser = wx.TextCtrl(id=wxID_FRMDBCONFIGTXTUSER, name=u'txtUser',
                                   parent=self.pnlConnection, pos=wx.Point(160, 96),
                                   size=wx.Size(248, 21), style=0, value=u'')
        self._init_sizers()

        self.lblPass = wx.StaticText(id=wxID_FRMDBCONFIGLBLPASS,
                                     label=u'Password:', name=u'lblPass',
                                     parent=self.pnlConnection, pos=wx.Point(56, 136), size=wx.Size(86, 13), style=0)

        self.txtPass = wx.TextCtrl(id=wxID_FRAME1TXTPASS, name=u'txtPass',
                                   parent=self.pnlConnection, pos=wx.Point(160, 128),
                                   size=wx.Size(248, 21), style=wx.PASSWORD, value=u'')


def create(parent):
    name = u'test_databaseChangerview'
    title = u'test_databaseChangerview'
    return MainFrame(parent, name, title)


class MainFrame(wx.Frame):
    def __init__(self, parent, name, title):
        wx.Frame.__init__(self, id=2, name=name, parent=parent, size=wx.Size(473, 308),
                          style=wx.DEFAULT_FRAME_STYLE, title=title)
        param = {}
        param['id'] = 1
        param['parent'] = self
        param['name'] = u'test_databaseChangerview'
        param['size'] = wx.Size(473, 308)
        param['style'] = None

        view = DatabaseChangerView(param)


if __name__ == "__main__":
    app = wx.App(False)
    frame = create(None)
    frame.Show()
    app.MainLoop()
'''