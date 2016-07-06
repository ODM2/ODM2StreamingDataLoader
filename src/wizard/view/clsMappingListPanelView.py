import wx

from ObjectListView import ObjectListView, ColumnDefn

class MappingListPanelView(wx.Panel):
    '''
    This is the view for the panel that
    has an ObjectListView control on it.

    For more details, have a look at
    frmMappingListPanel.py
    '''
    def __init__(self, parent):
        # Initialize the base class.
        wx.Panel.__init__(self, parent, id=wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.DefaultSize)
        # Declare a sizer with one column.
        fgSizer = wx.BoxSizer(wx.VERTICAL)
        #fgSizer.SetFlexibleDirection(wx.BOTH)
        #fgSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # Declare a fancy, new ObjectListView.
        self.listCtrl = ObjectListView(self, wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.DefaultSize,
            style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        # Change the message to be displayed when its empty.
        self.listCtrl.SetEmptyListMsg("No Mappings")
        # Add it to the sizer.
        fgSizer.Add(self.listCtrl, 1, wx.ALL|wx.EXPAND, 5)
        # Make fgSizer the one for this panel.
        self.SetSizer(fgSizer)
        self.Layout()


        
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect,
            self.listCtrl)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onDoubleClick,
            self.listCtrl)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.onDeselect,
            self.listCtrl)

        savebutton = wx.Button(self, id=wx.ID_SAVE, pos=wx.DefaultPosition)
        savebutton.Bind(wx.EVT_BUTTON, self.onSaveButton)

        exitbutton = wx.Button(self, id=wx.ID_EXIT, pos=wx.DefaultPosition)
        exitbutton.Bind(wx.EVT_BUTTON, self.onExitButton)
        btSizer = wx.BoxSizer(wx.HORIZONTAL)
        btSizer.AddSpacer((0,10),0, wx.EXPAND)
        btSizer.Add(savebutton, 0, wx.ALL | wx.ALIGN_RIGHT, 2)
        btSizer.Add(exitbutton, 0, wx.ALL | wx.ALIGN_RIGHT, 2)
        fgSizer.Add(btSizer, 0, wx.ALL | wx.ALIGN_RIGHT, 0)

    def onSaveButton(self, event):
        if (self.parent.currentPath == None):
            self.parent.onFileSaveAsClick(event)
        else:
            self.parent.onFileSaveClick(event)

    def onExitButton(self, event):
        self.parent.checkForSavedChanges()
        self.parent.Close()

    def onSelect(self, event):
        event.Skip()

    def onDeselect(self, event):
        event.Skip()

    def onDoubleClick(self, event):
        event.Skip()



