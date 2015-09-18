
import wx

# TODO 
# Clean these up.
from api.ODM2.services.createService import *
from api.ODM2.services.readService import *
from api.ODMconnection import dbconnection

from src.wizard.view.clsAddNewSampFeatPanel import AddNewSampFeatPanelView

class AddNewSampFeatPanelController(AddNewSampFeatPanelView):
    def __init__(self, daddy, **kwargs):
        super(AddNewSampFeatPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy

        self.populateFields()
        

    def populateFields(self):
        # TODO use real time credentials.
        session_factory = dbconnection.createConnection('mysql', 'jws.uwrl.usu.edu', 'odm2', 'ODM', 'ODM123!!')
        session = session_factory.getSession()
        read = ReadODM2(session_factory)
        
        sampFeat = read.getSamplingFeatures()
        

    def onOK(self, event):
        # Event handler for when the user clicks OK.
        code = self.m_textCtrl301.GetValue()
        # TODO
        # Handle this combo box:
        vType = self.m_comboBox82.GetSelection()
        name = self.m_textCtrl302.GetValue()
        description = self.m_textCtrl303.GetValue()
        geoType = self.m_comboBox821.GetSelection()
        elevation = self.m_textCtrl3022.GetValue()
        elevationDatum = self.m_comboBox8211.GetSelection()
        featureGeo = self.m_textCtrl3021.GetValue()
        print str(code)
        event.Skip()


        

