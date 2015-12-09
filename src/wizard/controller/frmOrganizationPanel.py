import wx

from src.wizard.view.clsOrganizationPanel\
    import OrganizationPanelView

class OrganizationPanel(OrganizationPanelView):
    def __init__(self, parent):
        super(OrganizationPanel, self).__init__(parent)
        self.parent = parent
        self.Bind(wx.EVT_SHOW, self.onShow)
    
        read = self.parent.database.getReadSession()

        orgs = read.getOrganizations()
        self.org = {}
        [self.org.update({o.OrganizationName:o.OrganizationID}) \
            for o in orgs]
    
        if not self.org:
            self.m_comboBox131.Enable(False)
        else:
            self.m_comboBox131.AppendItems(self.org.keys())
    
        orgTypes = [org.Name for org in read.getCVOrganizationTypes()]
        self.orgTypeCombo.AppendItems(orgTypes)

        self.comboParent.AppendItems(self.org.keys())
    

    def onShow(self, event):
        self.parent.btnNext.Enable(True)
        event.Skip()
  
    def enable(self, event):
        self.parent.btnNext.Enable(True)
        event.Skip()
    
    def disable(self, event):
        self.parent.btnNext.Enable(False)
        event.Skip()

