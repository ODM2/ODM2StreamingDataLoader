import wx
import wx.wizard

class WizardPage(wx.wizard.PyWizardPage):
    def __init__(self, parent, **kwargs):
        super(WizardPage, self).__init__(parent, **kwargs)

        self.next = None
        self.prev = None

        self.panels = []

        self.sizer = wx.FlexGridSizer(0, 1, 0, 0)
        self.sizer.SetFlexibleDirection(wx.BOTH)
        self.sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.SetSizer(self.sizer)
        self.Layout()

    def addPanel(self, panel):
        self.sizer.Add(panel, 0, wx.ALL | wx.EXPAND, 5)
        self.panels.append(panel)

    def getPanels(self):
        return self.panels

    # For the record, I don't usually capitalize method names,
    # but I am in this case because of the inherited methods
    # from wxPython.
    
    def SetNext(self, next):
        self.next = next

    def SetPrev(self, prev):
        self.prev = prev

    def GetNext(self):
        return self.next

    def GetPrev(self):
        return self.prev
    
