import wx

from ObjectListView import ObjectListView, ColumnDefn


class SeriesSelectPanelView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=wx.Size(900, 500))

        top_panel = wx.Panel(self)
        body_panel = wx.Panel(self)
        footer_panel = wx.Panel(self)

        # TOP PANEL CONTENT
        heading_text = wx.StaticText(top_panel, label='Select or create a time series result')
        self.editBtn = wx.Button(top_panel, label='Edit Result')
        self.newBtn = wx.Button(top_panel, label='Create New Result')

        top_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        top_panel_header_text_sizer = wx.BoxSizer(wx.VERTICAL)
        top_panel_button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # top_panel_button_sizer.Add(heading_text, 0, wx.EXPAND | wx.TOP | wx.LEFT, 5)
        top_panel_header_text_sizer.Add(heading_text, 1, wx.EXPAND, 0)

        top_panel_button_sizer.Add(top_panel_header_text_sizer, 0, wx.ALIGN_BOTTOM | wx.BOTTOM, 2)
        top_panel_button_sizer.AddSpacer((0, 0), 1, wx.EXPAND | wx.ALL)
        top_panel_button_sizer.Add(self.editBtn, 0, wx.EXPAND | wx.ALL, 2)
        top_panel_button_sizer.Add(self.newBtn, 0, wx.EXPAND | wx.ALL ^ wx.RIGHT, 2)

        top_panel_sizer.Add(top_panel_button_sizer, 0, wx.EXPAND | wx.ALL, 0)
        top_panel.SetSizer(top_panel_sizer)

        # BODY PANEL CONTENT
        self.listCtrl = ObjectListView(body_panel, style=wx.LC_REPORT)

        ####################### MOVES THIS TO THE CONTROLLER
        self.listCtrl.oddRowsBackColor = wx.Colour(255, 248, 229)
        self.listCtrl.evenRowsBackColor = wx.Colour(204, 229, 255)
        self.listCtrl.SetEmptyListMsg("No existing time series results.")
        self.listCtrl.SetObjects(None)

        columns = [
            'ResultID', 'SamplingFeatureCode', 'SamplingFeatureName', 'MethodCode', 'MethodName',
            'VariableCode', 'VariableNameCV', 'ProcessingLevelCode', 'ProcessingLevelDefinition',
            'UnitsName', 'ValueCount'
        ]

        defn = [
            ColumnDefn(title=key, align="left", minimumWidth=100, valueGetter=key,
                       stringConverter='%s')
            for key in columns]

        self.listCtrl.SetColumns(defn)

        ############### END

        body_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        body_panel_sizer.Add(self.listCtrl, 1, wx.EXPAND | wx.ALL, 0)
        body_panel.SetSizer(body_panel_sizer)

        # FOOTER PANEL CONTENT
        break_line = wx.StaticLine(footer_panel)
        # self.okBtn = wx.Button(footer_panel, label='OK', style=wx.)
        # cancelBtn = wx.Button(footer_panel, label='Cancel')
        self.okBtn = wx.Button(footer_panel, wx.ID_OK)
        cancelBtn = wx.Button(footer_panel, wx.ID_CANCEL)

        footer_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        footer_panel_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        footer_panel_button_sizer.AddSpacer((0, 0), 1, wx.EXPAND, 2)
        footer_panel_button_sizer.Add(cancelBtn, 0, wx.EXPAND | wx.ALL, 4)
        footer_panel_button_sizer.Add(self.okBtn, 0, wx.EXPAND | wx.ALL, 4)

        footer_panel_sizer.Add(break_line, 0, wx.EXPAND | wx.TOP, 5)
        footer_panel_sizer.Add(footer_panel_button_sizer, 0, wx.ALIGN_RIGHT)
        footer_panel.SetSizer(footer_panel_sizer)

        # A sizer that is oriented vertically.
        # fgSizer = wx.BoxSizer(wx.VERTICAL)
        # sbSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Select or create a time series result."), wx.VERTICAL)
        #
        # # ObjectListView table.
        # self.listCtrl = \
        #     ObjectListView(sbSizer.GetStaticBox(), id=wx.ID_ANY,
        #                    pos=wx.DefaultPosition,
        #                    size=wx.DefaultSize,
        #                    style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        # # Customize the list control's message
        # # when it is empty.
        # self.listCtrl.oddRowsBackColor = wx.Colour(255, 248, 229)
        # self.listCtrl.evenRowsBackColor = wx.Colour(204, 229, 255)
        # self.listCtrl.SetEmptyListMsg("No existing time series results.")
        # self.listCtrl.SetObjects(None)
        #
        # columns = [
        #     'ResultID', 'SamplingFeatureCode', 'SamplingFeatureName', 'MethodCode', 'MethodName',
        #     'VariableCode', 'VariableNameCV', 'ProcessingLevelCode', 'ProcessingLevelDefinition',
        #     'UnitsName', 'ValueCount'
        # ]
        #
        # defn = [
        #     ColumnDefn(title=key, align="left", minimumWidth=100, valueGetter=key,
        #                stringConverter='%s')
        #     for key in columns]
        #
        # self.listCtrl.SetColumns(defn)
        # self.editBtn = wx.Button(self, label="Edit Result")
        # self.newBtn = wx.Button(self, label="Create New Result")
        #
        # self.editBtn.Enable(False)
        #
        # dlgBtnSizer = wx.StdDialogButtonSizer()
        # editBtnSizer = wx.BoxSizer(wx.HORIZONTAL)
        # self.okBtn = wx.Button(self, wx.ID_OK)
        # cancelBtn = wx.Button(self, wx.ID_CANCEL)
        #
        # editBtnSizer.Add(self.editBtn)
        # dlgBtnSizer.AddButton(self.okBtn)
        # dlgBtnSizer.AddButton(cancelBtn)
        # editBtnSizer.Add(self.newBtn)
        # dlgBtnSizer.Realize()
        # # Add it to the sizer.
        # # The EXPAND flag along with the number 1 will
        # # enable the list to fill the panel.
        # sbSizer.Add(self.listCtrl, 1, wx.ALL|wx.EXPAND, 5)
        # fgSizer.Add(sbSizer, 1, wx.EXPAND, 5)
        # fgSizer.Add(editBtnSizer, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        # fgSizer.Add(dlgBtnSizer, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        # # Assign the sizer to the panel.
        # self.SetSizer(fgSizer)

        master_sizer = wx.BoxSizer(wx.VERTICAL)
        master_sizer.Add(top_panel, 0, wx.EXPAND | wx.ALL, 0)
        master_sizer.Add(body_panel, 1, wx.EXPAND | wx.ALL, 0)
        master_sizer.Add(footer_panel, 0, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(master_sizer)
