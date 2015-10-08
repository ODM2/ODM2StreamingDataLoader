
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
        
        code = self.m_textCtrl301.GetValue()
        sampFeatType = 'Site'
        siteType = self.sites[self.m_comboBox8.GetCurrentSelection()]
        lat = self.m_textCtrl35.GetValue()
        lon = self.m_textCtrl36.GetValue()
        spatialRef = self.sp_ref[self.m_comboBox822.GetCurrentSelection()]
        sampFeatName = self.m_textCtrl302.GetValue()
        sampFeatGeo = 'Point'
        featGeo = 'POINT(%s %s)' % (lon, lat)
        elevation_m = self.m_textCtrl3022.GetValue()
        elevationDatum = self.datum[self.m_comboBox8211.GetSelection()]
        desc = self.m_textCtrl303.GetValue()
        
        
        print "code",str(code)
        print "Type",str(sampFeatType)
        print "siteType",str(siteType)
        print "spatialRef",str(spatialRef)
        print "sampFeatgeotype",str(sampFeatGeo)
        print "elevation",str(elevation_m)
        print "datum",str(elevationDatum)
        print "feat geom",str(featGeo)
        print "desc",str(desc)

        '''
        write = self.db.getWriteSession()
        sf = write.createSamplingFeature(\
            code=str(code),
            vType=str(sampFeatType),
            name=str(sampFeatName),
            description=str(desc),
            geoType=str(sampFeatGeo),
            elevation=float(elevation_m),
            elevationDatum=str(elevationDatum),
            featureGeo=str(featGeo))
        
        site = write.createSamplingFeature(\
            sfId=sf.id,
            spatialRefId=spatialRef,
            vType=sampFeatType,
            latitude=float(lat),
            longitude=float(lon))
        '''
        #self.Validate()
        event.Skip()

