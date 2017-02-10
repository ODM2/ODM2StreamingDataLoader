import wx

from ObjectListView import ObjectListView, ColumnDefn

class SeriesSelectPanelView(wx.Panel):
    '''
    A SeriesSelectPanelView is a wx.Panel
    which contains an object list view.
    
    Only code that deals with graphical 
    aspects is in this class.
    '''
    def __init__(self, parent):
        # Init base class.
        wx.Panel.__init__(self, parent, id=wx.ID_ANY,
                          pos=wx.DefaultPosition,
                          size=wx.Size(900, 500))
        # A sizer that is oriented vertically.
        fgSizer = wx.BoxSizer(wx.VERTICAL)
        btSizer = wx.BoxSizer(wx.HORIZONTAL)
        # A sizer with a line around it.
        sbSizer = wx.StaticBoxSizer(\
            wx.StaticBox(self, wx.ID_ANY,
                         "Select or create a time series result."),
            wx.VERTICAL)
        # sbbSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.VERTICAL))
        # ObjectListView table.
        self.listCtrl = \
            ObjectListView(sbSizer.GetStaticBox(), id=wx.ID_ANY,
                           pos=wx.DefaultPosition,
                           size=wx.DefaultSize,
                           style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        # Customize the list control's message
        # when it is empty.
        self.listCtrl.oddRowsBackColor = wx.Colour(255, 248, 229)
        self.listCtrl.evenRowsBackColor = wx.Colour(204, 229, 255)
        self.listCtrl.SetEmptyListMsg("No existing time series results.")
        self.listCtrl.SetObjects(None)
        # self.listCtrl.SetColumns([
        #     ColumnDefn(title='Result ID', width=70, valueGetter='ResultID'),
        #     ColumnDefn(title='Samp. Feat. Code', width=110, valueGetter='SamplingFeatureCode'),
        #     ColumnDefn(title='Samp. Feat. Name', width=110, valueGetter='SamplingFeatureName'),
        #     ColumnDefn(title='Variable Code', width=100, valueGetter='VariableCode'),
        #     ColumnDefn(title='Variable Name', width=100, valueGetter='VariableNameCV'),
        #     ColumnDefn(title='Units Name', width=80, valueGetter='UnitsName'),
        #     ColumnDefn(title='Method Code', width=100, valueGetter='MethodCode'),
        #     ColumnDefn(title='Method Name', width=100, valueGetter='MethodName'),
        #     ColumnDefn(title='Proc. Level Code', width=110, valueGetter='ProcessingLevelCode'),
        #     ColumnDefn(title='Proc. Level Def.', width=110, valueGetter='ProcessingLevelDefinition'),
        # ])

        columns = ['ResultID', 'SamplingFeatureCode', 'SamplingFeatureName', 'MethodCode', 'MethodName',
                          'VariableCode', 'VariableNameCV', 'ProcessingLevelCode', 'ProcessingLevelDefinition',
                          'UnitsName', 'ValueCount',
                   ]
        defn= [
            ColumnDefn(title=key, align="left", minimumWidth=100, valueGetter=key,
                       stringConverter='%s')

            for key in columns]

        self.listCtrl.SetColumns(defn)
        self.editBtn = wx.Button(self,
                                wx.ID_ANY,
                                "Edit Result",
                                wx.DefaultPosition,
                                wx.DefaultSize,
                                style=0)

        self.newBtn = wx.Button(self,
                                wx.ID_ANY,
                                "Create New Result",
                                wx.DefaultPosition,
                                wx.DefaultSize,
                                style=0)
        self.editBtn.Enable(False)

        # Sizer at the bottom with the Ok and
        # Cancel buttons.
        #btSizer.Add(self.newBtn, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        #btSizer.Add(self.editBtn, 0, wx.ALL|wx.ALIGN_RIGHT, 5)

        dlgBtnSizer = wx.StdDialogButtonSizer()
        editBtnSizer = wx.BoxSizer(wx.HORIZONTAL)
        #dlgBtnSizer.Add(btSizer, 1, wx.EXPAND, 5)
        self.okBtn = wx.Button(self, wx.ID_OK)
        cancelBtn = wx.Button(self, wx.ID_CANCEL)
        #dlgBtnSizer.AddButton(self.editBtn)
        #dlgBtnSizer.AddButton(self.newBtn)
        # dlgBtnSizer.Add(self.newBtn, 0, wx.ALIGHT_RIGHT, 5)
        # dlgBtnSizer.Add(self.editBtn, 0, wx.ALIGHT_RIGHT, 5)
        # dlgBtnSizer.Add(btSizer, 0, wx.ALIGN_RIGHT, 5)
        editBtnSizer.Add(self.editBtn)
        dlgBtnSizer.AddButton(self.okBtn)
        dlgBtnSizer.AddButton(cancelBtn)
        editBtnSizer.Add(self.newBtn)
        dlgBtnSizer.Realize()
        # Add it to the sizer.
        # The EXPAND flag along with the number 1 will
        # enable the list to fill the panel.
        sbSizer.Add(self.listCtrl, 1, wx.ALL|wx.EXPAND, 5)
        fgSizer.Add(sbSizer, 1, wx.EXPAND, 5)
        fgSizer.Add(editBtnSizer, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        fgSizer.Add(dlgBtnSizer, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        # Assign the sizer to the panel.
        self.SetSizer(fgSizer)
        self.Layout()


    # ================== #
    # # Event Handlers # #
    # ================== #


