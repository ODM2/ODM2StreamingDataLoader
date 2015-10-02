
import wx

from src.wizard.view.clsAddNewVariablePanel import AddNewVariablePanelView

class AddNewVariablePanelController(AddNewVariablePanelView):
    def __init__(self, daddy, db, **kwargs):
        super(AddNewVariablePanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        self.db = db

        self.populateFields()

    def populateFields(self):
        '''
        '''
        read = self.db.getReadSession()

        names = [i.Name for i in read.getCVVariableNames()]
        self.m_comboBox4.AppendItems(names)
        
        types = [i.Name for i in read.getCVVariableTypes()]
        self.m_comboBox12.AppendItems(types)
        
        speciations = [i.Name for i in read.getCVSpeciations()]
        self.m_comboBox2.AppendItems(speciations)
