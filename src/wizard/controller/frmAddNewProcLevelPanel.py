
import wx

from src.wizard.view.clsAddNewProcLevelPanel import AddNewProcLevelPanelView

class AddNewProcLevelPanelController(AddNewProcLevelPanelView):
    def __init__(self, daddy, **kwargs):
        super(AddNewProcLevelPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        

