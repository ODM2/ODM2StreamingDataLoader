import wx

from src.wizard.view.clsSeriesSelectPanel \
    import SeriesSelectPanelView
from src.wizard.view.clsCustomDialog \
    import CustomDialog
from src.wizard.controller.frmSeriesWizard \
    import SeriesWizardController
class SeriesSelectDialog(CustomDialog):
    def __init__(self, parent, variable, database):
        super(SeriesSelectDialog, self).__init__(\
            parent=parent,
            title="Select Result for %s" % variable)
        self.database = database

        read = database.getReadSession()
        #read.getDetailedResultInfo("Time series coverage")
        seriesSelectPanel = SeriesSelectPanelView(self)
        self.addPanel(seriesSelectPanel)

        seriesSelectPanel.newBtn.Bind(wx.EVT_BUTTON, self.onNew)

        seriesSelectPanel.listCtrl.SetObjects(read.getDetailedResultInfo("Time series coverage"))

    # ================== #
    # > Event Handlers < #
    # ================== #

    def onNew(self, event):
        # Launch the SeriesWizardController
        resultWizard = SeriesWizardController(self,
            title="New Time Series Result Wizard",
            label="",
            db=self.database)
        resultWizard.run()
        event.Skip()

if __name__ == '__main__':

    import api 
    from api.ODMconnection import dbconnection
    from api.ODM2.services.readService import ReadODM2
    app = wx.App()
    frame = SeriesSelectDialog(parent=None,
                               variable="test",
                               database=dbconnection.createConnection("mysql", "rambo.bluezone.usu.edu", "odm2", "odm", "odm"))
    frame.ShowModal()
    app.MainLoop()
