
import wx

from view.clsAddNewSourcePanel import AddNewSourcePanelView

class AddNewSourcePanelController(AddNewSourcePanelView):
    def __init__(self, daddy, **kwargs):
        super(AddNewSourcePanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        

