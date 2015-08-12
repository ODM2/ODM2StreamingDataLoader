
import wx

from view.clsAddNewUnitPanel import AddNewUnitPanelView

class AddNewUnitPanelController(AddNewUnitPanelView):
    def __init__(self, daddy, **kwargs):
        super(AddNewUnitPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        

