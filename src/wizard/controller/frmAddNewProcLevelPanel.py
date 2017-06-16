
import wx

from src.wizard.view.clsAddNewProcLevelPanel import AddNewProcLevelPanelView
from odm2api.ODM2.models import ProcessingLevels

class AddNewProcLevelPanelController(AddNewProcLevelPanelView):
    def __init__(self, daddy, db):
        super(AddNewProcLevelPanelController, self).__init__(daddy)
        self.parent = daddy
        self.db = db
        self.processing_level = None

        self.populateFields()

    def populateFields(self):
        pass

    def onOK(self, event):
        if not self.Validate():
            self.Refresh()
            return
        else:
            # Move the data into the value dictionaries.
            # All data should be valid at this point.
            self.getFieldValues() 
            try:
                write = self.db.getWriteSession()
                proc = ProcessingLevels(
                    ProcessingLevelCode=self.procLevelCode,
                    Definition=self.definition,
                    Explanation=self.explanation
                )

                write.createProcessingLevel(proc)
                
                self.parent.parent.list_ctrl.SetObjects(self.parent.parent.getSeriesData())
                length = self.parent.parent.list_ctrl.GetItemCount.im_self.ItemCount
                length = length - 1
                self.parent.parent.list_ctrl.Focus(length)
                self.parent.parent.list_ctrl.Select(length, 1)
            except Exception as e:
                print e

        event.Skip()

    def getFieldValues(self):
        self.procLevelCode = str(self.m_textCtrl30.GetValue())
        if str(self.m_textCtrl31.GetValue()) == '':
            self.definition = None
        else:
            self.definition = str(self.m_textCtrl31.GetValue())
        if str(self.m_textCtrl32.GetValue()) == '':
            self.explanation = None
        else:
            self.explanation = str(self.m_textCtrl32.GetValue())

