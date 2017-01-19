import wx
from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog
from src.wizard.controller.frmAddNewSampFeatPanel import AddNewSampFeatPanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel
from ObjectListView import ColumnDefn


class SampFeatSelectPanel(SeriesSelectPanel):
    def __init__(self, parent, existing_result=None):
        super(SampFeatSelectPanel, self).__init__(parent, "Sampling Feature")
        self.parent = parent
        self.list_ctrl.SetColumns([
            ColumnDefn('Code', 'left', 120, 'SamplingFeatureCode'),
            ColumnDefn('Name', 'left', 120, 'SamplingFeatureName'),
            ColumnDefn('Type', 'left', 120, 'SamplingFeatureTypeCV'),
            ColumnDefn('Description', 'left', 120, 'SamplingFeatureDescription'),
            ColumnDefn('Geotype', 'left', 120, 'SamplingFeatureGeotypeCV'),
            ColumnDefn('Elevation', 'left', 120, 'Elevation_m'),
        ])
        self.existing_result = existing_result

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
            if self.existing_result.SamplingFeatureCode == data[i].SamplingFeatureCode:
                index = i
                break

        if index >= 0:
            self.list_ctrl.Select(index)
            self.list_ctrl.SetFocus()

    def onShow(self, event):
        if self.list_ctrl.GetSelectedObject():
            self.parent.btnNext.Enable()
        else:
            self.parent.btnNext.Disable()
        event.Skip()

    def enable(self, event):
        self.parent.btnNext.Enable()
        event.Skip()
    
    def disable(self, event):
        self.parent.btnNext.Disable()
        event.Skip()

    def getSeriesData(self):
        if self.parent.database:
            read = self.parent.database.getReadSession()
            return read.getSamplingFeatures(type="site")
        return []

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, 'Create New Sampling Feature')
        newSampFeatPnl = AddNewSampFeatPanelController(dlg, self.parent.database)
        dlg.addPanel(newSampFeatPnl)
        dlg.CenterOnScreen()

        if dlg.ShowModal() == wx.ID_OK:
            # Refresh List.
            self.list_ctrl.SetObjects(self.getSeriesData())

        dlg.Destroy()
        event.Skip()
