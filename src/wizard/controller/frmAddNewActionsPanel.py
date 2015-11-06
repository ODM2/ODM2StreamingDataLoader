
import wx

from src.wizard.view.clsAddNewActionsPanel import AddNewActionsPanelView

class Test:
    def __init__(self, name, org):
        self.name = name
        self.org = org

class AddNewActionsPanelController(AddNewActionsPanelView):
    def __init__(self, daddy, db, **kwargs):
        super(AddNewActionsPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        self.db = db

        self.m_comboBox13.Bind(wx.EVT_COMBOBOX, self.onActionTypeSelect)
        self.affList.Bind(wx.EVT_LEFT_DOWN, self.onAffListClick)    
        self.affList.Bind(wx.EVT_LIST_INSERT_ITEM, self.onAffInsert)    
        self.affList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onAffSelect)    
        self.read = self.db.getReadSession()
        
        self.populateFields()

    def populateFields(self):
        #read = self.db.getReadSession()

        actionTypes = [i.Name for i in self.read.getCVActionTypes()]
        self.m_comboBox13.AppendItems(actionTypes)

    def onActionTypeSelect(self, event):
        print "Filter by", event.GetString()
        methodTypes = [i.MethodName for i in self.read.getMethodsByType(event.GetString())]
        self.m_comboBox134.SetItems(methodTypes)
        
    def onAffListClick(self, event):
        print "clicked"
        self.affList.AddObject(Test("",""))
        event.Skip()
    
    def onAffInsert(self, event):
        print "new item added"
        #self.affList.AddObject(None)
        event.Skip()
    
    def onAffSelect(self, event):
        print "selected"
        event.Skip()
