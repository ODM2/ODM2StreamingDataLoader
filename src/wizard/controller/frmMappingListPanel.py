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
        # Add the columns to the list control.
        self.listCtrl.SetColumns([
            ColumnDefn('ID', 'left', 100, ''),
            ColumnDefn('Server', 'left', 100, ''),
            ColumnDefn('Database', 'left', 100, ''),
            ColumnDefn('Data File Location', 'left', 130, ''),
            ColumnDefn('Scheduled Period', 'left', 100, ''),
            ColumnDefn('Scheduled Begin Time', 'left', 100, ''),
            ColumnDefn('Last Update', 'left', 100, ''),
        ])
        self.listCtrl.SetObjects(None)


