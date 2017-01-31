import wx
from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog
from src.wizard.controller.frmAddNewActionsPanel import AddNewActionsPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel
from ObjectListView import ColumnDefn


class ActionsSelectPanel(SeriesSelectPanel):
    def __init__(self, parent, existing_result=None):
        super(ActionsSelectPanel, self).__init__(parent, "Action")
        self.parent = parent
        self.existing_result = existing_result

        self.list_ctrl.SetColumns([
            ColumnDefn('Id', 'left', 70, 'ActionID'),
            ColumnDefn('Type', 'left', 100, 'ActionTypeCV'),
            ColumnDefn('Description', 'left', 500, 'ActionDescription'),
            ColumnDefn('Method Id', 'left', 90, 'MethodID'),
            ColumnDefn('Begin Time', 'left', 125, 'BeginDateTime'),
            ColumnDefn('End Time', 'left', 125, 'EndDateTime'),
        ])

        self.list_ctrl.SetObjects(self.getSeriesData())
        if not self.parent.database:
            self.new_button.Enable(False)

        self.select_existing_series()

        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.enable)
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.disable)
        # self.Bind(wx.EVT_SHOW, self.onShow)

        self.list_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_keyboard_pressed_down)

    def on_keyboard_pressed_down(self, event):
        pass

    def select_existing_series(self):
        if self.existing_result is None:
            return

        index = -1
        data = self.list_ctrl.GetObjects()
        for i in range(len(data)):
            if self.existing_result.FeatureActionObj.ActionObj.ActionID == data[i].ActionID:
                index = i
                break

        if index >= 0:
            self.list_ctrl.Select(index)
            self.list_ctrl.SetFocus()

    def onShow(self, event):
        if self.list_ctrl.GetSelectedObject():
            self.parent.btnNext.Enable(True)  
        else:
            self.parent.btnNext.Enable(False)  
        event.Skip()        

    def enable(self, event):
        if self.existing_result is not None:
            self.existing_result.FeatureActionObj.ActionObj = self.list_ctrl.GetSelectedObject()
        self.parent.btnNext.Enable(True)

    def disable(self, event):
        self.parent.btnNext.Enable(False)

    def getSeriesData(self):
        if self.parent.database:
            read = self.parent.database.getReadSession()
            return read.getActions()
        return []

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self,
            u'Create New Action')
        newActionsPanel = AddNewActionsPanelController(dlg,
            self.parent.database)
        dlg.addPanel(newActionsPanel)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            self.list_ctrl.SetObjects(self.getSeriesData())

        #else:
        #    pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


