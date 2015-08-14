
import wx

from view.clsAddNewSampFeatPanel import AddNewSampFeatPanelView

class AddNewSampFeatPanelController(AddNewSampFeatPanelView):
    def __init__(self, daddy, **kwargs):
        super(AddNewSampFeatPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        

