
import wx

from src.wizard.view.clsAddNewProcLevelPanel import AddNewProcLevelPanelView

class AddNewProcLevelPanelController(AddNewProcLevelPanelView):
    def __init__(self, daddy, db, **kwargs):
        super(AddNewProcLevelPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        self.db = db

        self.populateFields()

    def populateFields(self):
        pass

