
import wx
import uuid
# TODO 
# Clean these up.
from api.ODM2.services.createService import *
from api.ODM2.services.readService import *
from api.ODMconnection import dbconnection

from src.wizard.view.clsAddNewSampFeatPanel import AddNewSampFeatPanelView

class AddNewSampFeatPanelController(AddNewSampFeatPanelView):
    def __init__(self, daddy, db, **kwargs):
        super(AddNewSampFeatPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        self.db = db

        self.populateFields()
        

    def populateFields(self):
        read = self.db.getReadSession()
        
        _uuid = uuid.uuid4()
        self.m_textCtrl30.SetValue(unicode(_uuid))
        
        cv_names = [i.Name for i in read.getCVSamplingFeatureTypes()]
        self.m_comboBox82.AppendItems(cv_names)
        
        sites = [i.Name for i in read.getCVSiteTypes()]
        self.m_comboBox8.AppendItems(sites)
        
        sp_ref = [i.SRSName for i in read.getCVSpacialReferenceTypes()]
        self.m_comboBox822.AppendItems(sp_ref)
        
        geo = [i.Name for i in read.getCVSamplingFeatureGeoTypes()]
        self.m_comboBox821.AppendItems(geo)
        
        datum = [i.Name for i in read.getCVElevationDatums()]
        self.m_comboBox8211.AppendItems(datum)
        
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


        

