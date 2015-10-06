import wx

from src.wizard.view.clsMappingListPanelView import MappingListPanelView

from ObjectListView import ObjectListView, ColumnDefn

class MappingListPanel(MappingListPanelView):
    '''
    This is basically a panel with an
    ObjectListView control on it.

    The list items are mappings within
    a yaml configuration file.
    '''
    def __init__(self, parent):
        # Initialize the base class.
        super(MappingListPanel, self).__init__(parent)
        # Keep a handle to the parent.
        self.parent = parent
        # Add the columns to the list control.
        self.listCtrl.SetColumns([
            ColumnDefn('ID', 'left', 100, 'id'),
            ColumnDefn('Server', 'left', 100, 'server'),
            ColumnDefn('Database', 'left', 150, 'db'),
            ColumnDefn('Data File Location', 'left', 200, 'path'),
            ColumnDefn('Scheduled Period', 'left', 120, 'period'),
            ColumnDefn('Scheduled Begin Time', 'left', 150, 'begin'),
            ColumnDefn('Last Update', 'left', 100, 'update'),
        ])
        self.listCtrl.SetObjects(None)

    def setObjects(self, obj):
        '''
            Wrapper method which calls this panel's
            object list view control SetObjects 
            method.
        '''
        self.listCtrl.SetObjects(obj)

    def onSelect(self, event):
        self.parent.tb.EnableTool(20, True)
        self.parent.tb.EnableTool(30, True)
        event.Skip()

    def onDeselect(self, event):
        self.parent.tb.EnableTool(20, False)
        self.parent.tb.EnableTool(30, False)
        event.Skip()

    def onDoubleClick(self, event):
        self.parent.onEditButtonClick(event) 
        event.Skip()
