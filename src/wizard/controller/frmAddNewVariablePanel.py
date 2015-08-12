
import wx

from view.clsAddNewVariablePanel import AddNewVariablePanelView

class AddNewVariablePanelController(AddNewVariablePanelView):
    def __init__(self, daddy, **kwargs):
        super(AddNewVariablePanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        

