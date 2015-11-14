
import wx

from collections import namedtuple
from src.controllers.Database import Database


from src.wizard.view.clsAddNewActionsPanel import AddNewActionsPanelView
from src.wizard.view.clsAddAffiliationPanel import NewAffiliationView
from src.wizard.view.clsCustomDialog import CustomDialog

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
        self.m_b.Bind(wx.EVT_BUTTON, self.onNewAffiliation)
        #self.affList.Bind(wx.EVT_LEFT_DOWN, self.onAffListClick)    
        #self.affList.Bind(wx.EVT_LIST_INSERT_ITEM, self.onAffInsert)    
        #self.affList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onAffSelect)    
        self.read = self.db.getReadSession()
        
        self.populateFields()

    def populateFields(self):
        #read = self.db.getReadSession()

        actionTypes = [i.Name for i in self.read.getCVActionTypes()]
        self.m_comboBox13.AppendItems(actionTypes)

        #self.affList.SetObjects(self.read.getDetailedAffiliationInfo())
        self.affList.AddObjects(self.read.getDetailedAffiliationInfo())

    def onActionTypeSelect(self, event):
        print "Filter by", event.GetString()
        methodTypes = [i.MethodName for i in self.read.getMethodsByType(event.GetString())]
        self.m_comboBox134.SetItems(methodTypes)
       
    def onNewAffiliation(self, event):
        dlg = CustomDialog(self, "New Affiliation")
        dlg.addPanel(NewAffiliationView(dlg))
        dlg.ShowModal()
        event.Skip()

if __name__ == '__main__':
    db = Database()
    Credentials = namedtuple('Credentials', 'engine, host, db_name, uid, pwd')
    db.createConnection(Credentials(\
        'mysql',
        'rambo.bluezone.usu.edu',
        'odm2',
        'odm',
        'odm'))
    app = wx.App()
    frame = wx.Frame(None)
    frame.SetSizer(wx.BoxSizer(wx.VERTICAL))
    pnl = AddNewActionsPanelController(frame, db)
    frame.CenterOnScreen()
    frame.Show()
    app.MainLoop()
 
