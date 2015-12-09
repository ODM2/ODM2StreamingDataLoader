import wx

from src.wizard.view.clsPersonPanel\
    import PersonPanelView

class PersonPanel(PersonPanelView):
    def __init__(self, parent):
        super(PersonPanel, self).__init__(parent)
        self.parent = parent
        self.Bind(wx.EVT_SHOW, self.onShow)
        
        self.parent.btnNext.Enable(True)
        
        read = self.parent.database.getReadSession()
    
        people = read.getPeople()
        self.people = {}
        [self.people.update({p.PersonFirstName + " " + p.PersonLastName:p.PersonID})\
            for p in people]
    
        if not self.people:
            self.m_comboBox13.Enable(False)
        else:
            self.m_comboBox13.AppendItems(self.people.keys()) 

    def onShow(self, event):
        print "Show"
        
        event.Skip()
  
    def enable(self, event):
        self.parent.btnNext.Enable(True)
        event.Skip()
    
    def disable(self, event):
        self.parent.btnNext.Enable(False)
        event.Skip()

