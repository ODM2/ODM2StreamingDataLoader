
import wx
import uuid
# TODO 
# Clean these up.
from api.ODM2.services.createService import *
from api.ODM2.services.readService import *
from api.ODMconnection import dbconnection

from src.wizard.view.clsAddNewSampFeatPanel import AddNewSampFeatPanelView
from src.wizard.view.clsAddSpatialReferences import NewSpatialReferenceView
from src.wizard.view.clsCustomDialog import CustomDialog

class AddNewSampFeatPanelController(AddNewSampFeatPanelView):
    def __init__(self, daddy, db, **kwargs):
        super(AddNewSampFeatPanelController, self).__init__(daddy,
            **kwargs)
        self.parent = daddy
        self.db = db
        
        self.m_button411.Bind(wx.EVT_BUTTON, self.onCreateSpatialReference)

        self.populateFields()
        

    def populateFields(self):
        read = self.db.getReadSession()
        
        self._uuid = uuid.uuid4()
        self.m_textCtrl30.SetValue(unicode(self._uuid))
        
        #cv_names = [i.Name for i in read.getCVSamplingFeatureTypes()]
        self.m_textCtrl30.SetValue('Site')
        
        self.sites = [i.Name for i in read.getCVSiteTypes()]
        self.m_comboBox8.AppendItems(self.sites)
        
        self.sp_ref = [{i.SRSName:i.SpatialReferenceID}\
            for i in read.getCVSpacialReferenceTypes()]
        self.m_comboBox822.AppendItems(\
            [y for x in [i.keys() for i in self.sp_ref] for y in x]
            )
        
        #geo = [i.Name for i in read.getCVSamplingFeatureGeoTypes()]
        self.m_geotypeTxt.SetValue('Point')
        
        self.datum = [i.Name for i in read.getCVElevationDatums()]
        self.m_comboBox8211.AppendItems(self.datum)

    def onCreateSpatialReference(self, event):
        dlg = CustomDialog(self, "New Spatial Reference")
        dlg.addPanel(NewSpatialReferenceView(dlg))
        dlg.ShowModal()
        event.Skip()
        
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
                    code=self.requiredValues['code'],
                    vType=self.requiredValues['vType'],
                    name=self.optionalValues['name'],
                    description=self.optionalValues['desc'],
                    geoType=self.optionalValues['geoType'],
                    elevation=self.optionalValues['elevation'],
                    elevationDatum=self.optionalValues['elevationDatum'],
                    featureGeo=self.optionalValues['featureGeo'])
                
                site = write.createSite(\
                    sfId=sf.SamplingFeatureID,
                    spatialRefId=self.requiredValues['spatialRef'],
                    vType=self.requiredValues['siteType'],
                    latitude=self.requiredValues['lat'],
                    longitude=self.requiredValues['long'])

                self.sf = sf
            except Exception as e:
                print e
        event.Skip()

    def getFieldValues(self):
        # Stores all of the required field values.
        # Default is None.
        self.requiredValues = {'uuid':'', # Required
                  'code':None, # Required
                  'vType':'Site',# Required
                  'spatialRef':None,# Required
                  'lat':None, # Required
                  'long':None,# Required
                  'siteType':None
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
        self.requiredValues['code'] = str(self.m_textCtrl301.GetValue())
        
        keys = [y for x in [i.keys() for i in self.sp_ref] for y in x]
        vals = [y for x in [i.values() for i in self.sp_ref] for y in x]
        d = dict(zip(keys, vals))

        self.requiredValues['spatialRef'] = \
            d[self.m_comboBox822.GetStringSelection()]
        self.requiredValues['lat'] = float(self.m_textCtrl35.GetValue())
        self.requiredValues['long'] = float(self.m_textCtrl36.GetValue())
        if self.m_comboBox8211.GetStringSelection() != '':
            self.optionalValues['elevationDatum'] = \
                str(self.datum[self.m_comboBox8211.GetSelection()])
        
        self.requiredValues['siteType'] = \
            str(self.m_comboBox8.GetStringSelection())
        
        if str(self.m_textCtrl302.GetValue()) != '':
            self.optionalValues['name'] = str(self.m_textCtrl302.GetValue())
        if str(self.m_textCtrl3022.GetValue()) != '':
            self.optionalValues['elevation'] = str(self.m_textCtrl3022.GetValue())
       
        if str(self.m_comboBox8211.GetStringSelection()) != '':
            self.optionalValues['elevationDatum'] = str(self.m_comboBox8211.GetStringSelection())
        if str(self.m_textCtrl303.GetValue()) != '':
            self.optionalValues['desc'] = str(self.m_textCtrl303.GetValue())
