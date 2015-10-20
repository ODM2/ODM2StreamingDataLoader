
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
        
        self._uuid = uuid.uuid4()
        self.m_textCtrl30.SetValue(unicode(self._uuid))
        
        #cv_names = [i.Name for i in read.getCVSamplingFeatureTypes()]
        self.m_textCtrl30.SetValue('Site')
        
        self.sites = [i.Name for i in read.getCVSiteTypes()]
        self.m_comboBox8.AppendItems(self.sites)
        
        self.sp_ref = [i.SRSName for i in read.getCVSpacialReferenceTypes()]
        self.m_comboBox822.AppendItems(self.sp_ref)
        
        #geo = [i.Name for i in read.getCVSamplingFeatureGeoTypes()]
        self.m_geotypeTxt.SetValue('Point')
        
        self.datum = [i.Name for i in read.getCVElevationDatums()]
        self.m_comboBox8211.AppendItems(self.datum)

        
    def onOK(self, event):
        # Event handler for when the user clicks OK.
        
        # Try to validate the form.
        if not self.Validate():
            self.Refresh()
            return
        else:
            # Move the data into the value dictionaries.
            # All data should be valid at this point.
            self.getFieldValues() 
            try:
                # Create the variable in the database.
                write = self.db.getWriteSession()
                sf = write.createSamplingFeature(\
                    uuid=str(self._uuid),
                    code=str(code),
                    vType=str(sampFeatType),
                    name=str(sampFeatName),
                    description=str(desc),
                    geoType=str(sampFeatGeo),
                    elevation=float(elevation_m),
                    elevationDatum=str(elevationDatum),
                    featureGeo=str(featGeo))
                
                site = write.createSite(\
                    sfId=sf.SamplingFeatureID,
                    spatialRefId=spatialRef,
                    vType=siteType,
                    latitude=float(lat),
                    longitude=float(lon))
            except Exception as e:
                print e
        event.Skip()

    def getFieldValues(self):
        # Stores all of the required field values.
        # Default is None.
        self.requiredValues = {'uuid':None, # Required
                  'code':None, # Required
                  'vType':'Site',# Required
                  'spatialRef':None,# Required
                  'lat':None, # Required
                  'long':None,# Required
                  }
        self.optionalValues = {
                  'name':None, 
                  'desc':None,
                  'geoType':'Point',
                  'elevation':None,
                  'elevationDatum':None,
                  'featureGeo':None,
                  }
        
        self.requiredValues['uuid'] = str(uuid.uuid4())
        self.requiredValues['code'] = self.m_textCtrl301.GetValue()
        self.sp_ref[self.m_comboBox822.GetCurrentSelection()]
