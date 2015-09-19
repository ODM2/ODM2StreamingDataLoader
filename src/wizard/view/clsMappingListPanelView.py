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
            pos=wx.DefaultPosition, size=wx.Size(644,330))
        # Declare a sizer with one column.
        fgSizer = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer.SetFlexibleDirection(wx.BOTH)
        fgSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        # Declare a fancy, new ObjectListView.
        self.listCtrl = ObjectListView(self, wx.ID_ANY,
            pos=wx.DefaultPosition, size=wx.Size(630,250),
            style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        # Add it to the sizer.
        fgSizer.Add(self.listCtrl, 0, wx.ALL, 5)
        # Make fgSizer the one for this panel.
        self.SetSizer(fgSizer)
        self.Layout()



