import wx
from src.wizard.controller.frmAddNewUnitPanel import AddNewUnitPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel
from ObjectListView import ColumnDefn
from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog


class UnitSelectPanel(SeriesSelectPanel):
    def __init__(self, parent, existing_result=None):
        super(UnitSelectPanel, self).__init__(parent, "Unit")
        self.parent = parent
        self.existing_result = existing_result

        self.list_ctrl.SetColumns([
            ColumnDefn('Abbreviation', 'left', 120, 'UnitsAbbreviation'),
            ColumnDefn('Name', 'left', 120, 'UnitsName'),
            ColumnDefn('Type', 'left', 120, 'UnitsTypeCV'),
            ColumnDefn('Link', 'left', 120, 'UnitsLink'),
        ])

        self.list_ctrl.SetObjects(self.getSeriesData())
        if not self.parent.database:
            self.new_button.Enable(False)

        self.select_existing_series()
        self.auto_size_table()

        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.enable)
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.disable)
        self.Bind(wx.EVT_SHOW, self.onShow)

    def select_existing_series(self):
        if self.existing_result is None:
            return

        index = -1
        data = self.list_ctrl.GetObjects()
        for i in range(len(data)):
            if self.existing_result.UnitsObj.UnitsName == data[i].UnitsName:
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
            self.existing_result.UnitsObj = self.list_ctrl.GetSelectedObject()
        self.parent.btnNext.Enable(True)

    def disable(self, event):
        self.parent.btnNext.Enable(False)

    def getSeriesData(self):
        if self.parent.database:
            read = self.parent.database.getReadSession()
            return read.getUnits()
        return []

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, 'Create New Unit')
        controller = AddNewUnitPanelController(dlg, self.parent.database)
        dlg.addPanel(controller)
        dlg.CenterOnScreen()

        if dlg.ShowModal() == wx.ID_OK and controller.units is not None:
            self.list_ctrl.SetObjects(self.getSeriesData())
            self.list_ctrl.SelectObject(modelObject=controller.units, ensureVisible=True)
        else:
          pass

        dlg.Destroy()
        event.Skip()
