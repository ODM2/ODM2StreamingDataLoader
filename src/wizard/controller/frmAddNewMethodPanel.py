
import wx

from view.clsAddNewMethodPanel import AddNewMethodPanelView

class AddNewMethodPanelController(AddNewMethodPanelView):
    def __init__(self, daddy, **kwargs):
        super(AddNewMethodPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        

