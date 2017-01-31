import wx
from src.wizard.controller.frmAddNewProcLevelPanel import AddNewProcLevelPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel
from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog
from ObjectListView import ColumnDefn


class ProcLevelSelectPanel(SeriesSelectPanel):
    def __init__(self, parent, existing_result=None):
        super(ProcLevelSelectPanel, self).__init__(parent, "Processing Level")
        self.parent = parent
        self.existing_result = existing_result

        self.list_ctrl.SetColumns([
            ColumnDefn('Code', 'left', 120, 'ProcessingLevelCode'),
            ColumnDefn('Definition', 'left', 120, 'Definition'),
            ColumnDefn('Explanation', 'left', 120, 'Explanation'),
        ])

        self.list_ctrl.SetObjects(self.getSeriesData())
        if not self.parent.database:
            self.new_button.Enable(False)

        self.select_existing_series()
        self.auto_size_table()

        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.enable)
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.disable)
        self.Bind(wx.EVT_SHOW, self.onShow)

        self.list_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_keyboard_pressed_down)

    def on_keyboard_pressed_down(self, event):
        pass

    def select_existing_series(self):
        if self.existing_result is None:
            return

        index = -1
        data = self.list_ctrl.GetObjects()
        for i in range(len(data)):
            if self.existing_result.ProcessingLevelObj.ProcessingLevelCode == data[i].ProcessingLevelCode:
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
            self.existing_result.ProcessingLevelObj = self.list_ctrl.GetSelectedObject()
        self.parent.btnNext.Enable(True)

    def disable(self, event):
        self.parent.btnNext.Enable(False)

    def getSeriesData(self):
        if self.parent.database:
            read = self.parent.database.getReadSession()
            return read.getProcessingLevels()
        return []

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, 'Create New Processing Level')
        newProcLevelPanel = AddNewProcLevelPanelController(dlg, self.parent.database)
        dlg.addPanel(newProcLevelPanel)
        dlg.CenterOnScreen()

        if dlg.ShowModal() == wx.ID_OK:
            self.list_ctrl.SetObjects(self.getSeriesData())

        dlg.Destroy()
        event.Skip()
