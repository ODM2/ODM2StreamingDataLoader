
import wx

from view.clsAddNewActionsPanel import AddNewActionsPanelView

class AddNewActionsPanelController(AddNewActionsPanelView):
    def __init__(self, daddy, **kwargs):
        super(AddNewActionsPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        

