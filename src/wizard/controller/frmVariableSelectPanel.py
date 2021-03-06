import wx
from src.wizard.controller.frmNewSeriesDialog import NewSeriesDialog
from src.wizard.controller.frmAddNewVariablePanel import AddNewVariablePanelController
from src.wizard.controller.frmSeriesSelectPanel import SeriesSelectPanel
from ObjectListView import ColumnDefn


class VariableSelectPanel(SeriesSelectPanel):
    def __init__(self, parent, existing_result=None):
        super(VariableSelectPanel, self).__init__(parent, "Variable")
        self.parent = parent
        self.existing_result = existing_result

        self.list_ctrl.SetColumns([
            ColumnDefn('Code', 'left', 120, 'VariableCode'),
            ColumnDefn('Name', 'left', 120, 'VariableNameCV'),
            ColumnDefn('Type', 'left', 120, 'VariableTypeCV'),
            ColumnDefn('Definition', 'left', 120, 'VariableDefinition'),
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
            if self.existing_result.VariableObj.VariableCode == data[i].VariableCode:
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
            self.existing_result.VariableObj = self.list_ctrl.GetSelectedObject()
        self.parent.btnNext.Enable(True)

    def disable(self, event):
        self.parent.btnNext.Enable(False)

    def getSeriesData(self):
        if self.parent.database:
            read = self.parent.database.getReadSession()
            return read.getVariables()
        return []

    def onButtonAdd(self, event):
        dlg = NewSeriesDialog(self, 'Create New Variable')
        controller = AddNewVariablePanelController(dlg, self.parent.database)
        dlg.addPanel(controller)
        dlg.CenterOnScreen()

        if dlg.ShowModal() == wx.ID_OK:
            pass
            #self.list_ctrl.SetObjects(self.getSeriesData())
        else:
            pass
        dlg.Destroy()
        event.Skip()
    
    def __del__( self ):
        pass


        if dlg.ShowModal() == wx.ID_OK and controller.variable is not None:
            data = self.getSeriesData()
            self.list_ctrl.SetObjects(data)

            # Select the new variable
            self.list_ctrl.SelectObject(modelObject=controller.variable, ensureVisible=True)

        dlg.Destroy()
