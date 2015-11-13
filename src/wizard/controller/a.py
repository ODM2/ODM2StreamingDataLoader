import wx
import wx.lib.agw.pycollapsiblepane as PCP

class MyFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, -1, "PyCollapsiblePane Demo")

        panel = wx.Panel(self)

        title = wx.StaticText(panel, label="PyCollapsiblePane")
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        title.SetForegroundColour("black")

        self.cp = cp = PCP.PyCollapsiblePane(panel, label="Some Data",
                                             agwStyle=wx.CP_GTK_EXPANDER,
                                             style=wx.CP_DEFAULT_STYLE)

        self.MakePaneContent(cp.GetPane())

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(title, 0, wx.ALL, 25)
        sizer.Add(cp, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 25)

        panel.SetSizer(sizer)
        sizer.Layout()


    def MakePaneContent(self, pane):
        ''' Just makes a few controls to put on `PyCollapsiblePane`. '''

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
                      wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(name, 0, wx.EXPAND)
        addrSizer.Add(addrLbl, 0,
                      wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(addr1, 0, wx.EXPAND)
        addrSizer.Add((5,5))
        addrSizer.Add(addr2, 0, wx.EXPAND)

        addrSizer.Add(cstLbl, 0,
                      wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)

        cstSizer = wx.BoxSizer(wx.HORIZONTAL)
        cstSizer.Add(city, 1)
        cstSizer.Add(state, 0, wx.LEFT | wx.RIGHT, 5)
        cstSizer.Add(zip)
        addrSizer.Add(cstSizer, 0, wx.EXPAND)

        border = wx.BoxSizer()
        border.Add(addrSizer, 1, wx.EXPAND | wx.ALL, 5)
        pane.SetSizer(border)


# our normal wxApp-derived class, as usual

app = wx.App(0)

frame = MyFrame(None)
app.SetTopWindow(frame)
frame.Show()

app.MainLoop()
