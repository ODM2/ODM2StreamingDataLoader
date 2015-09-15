
import wx

from src.wizard.view.clsAddNewResultsPanel import AddNewResultsPanelView

class AddNewResultsPanelController(AddNewResultsPanelView):
    def __init__(self, daddy, **kwargs):
        super(AddNewResultsPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        

