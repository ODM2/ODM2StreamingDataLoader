__author__ = 'Jacob'

import wx
from sqlalchemy.exc import DBAPIError


class DatabaseChangerController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self._bindEvents()

    def _bindEvents(self):
        self.view.btnSave.Bind(wx.EVT_BUTTON, self.onSave, id=self.view.btnSave.Id)
        self.view.btnCancel.Bind(wx.EVT_BUTTON, self.onCancel, id=self.view.btnCancel.Id)
        self.view.btnTest.Bind(wx.EVT_BUTTON, self.onTest, id=self.view.btnTest.Id)

    def onTest(self, event):
        conn_dict = self._getFieldValues()
        self.validateInput(conn_dict)

    def onSave(self, event):
        conn_dict = self._getFieldValues()
        result = self.validateInput(conn_dict, False)

    def onCancel(self, event):
        self.view.SetReturnCode(wx.ID_CANCEL)
        self.view.Destroy()

    def validateInput(self, conn_dict, test=True):
        message = ""
        if conn_dict['user'] and conn_dict['password'] and conn_dict['address'] \
                and conn_dict['db'] and conn_dict['engine']:
            if test:
                if self.model.service_manager.test_connection(conn_dict):
                    try:
                        if self.model.service_manager.get_db_version(conn_dict) == '1.1.1':
                            message = "This connection is valid"
                            wx.MessageBox(message, 'Test Connection', wx.OK)
                            return True
                    except DBAPIError:
                        message = "Please check the credentials and " \
                                  "ensure that the database is accessible"
                        wx.MessageBox(message, 'Login Unsuccessful', wx.OK | wx.ICON_ERROR)
                else:
                    message = "This connection is invalid"
                    wx.MessageBox(message, 'Test Connection', wx.OK | wx.ICON_ERROR)
            else:
                self.view.SetReturnCode(wx.ID_OK)
                self.model.service_manager.add_connection(conn_dict)
                self.view.Destroy()
        else:
            message = "Please enter valid connection information"
            wx.MessageBox(message, 'ODMTool Python', wx.OK | wx.ICON_EXCLAMATION)
        return False


    # Returns a dictionary of the database values entered in the form
    def _getFieldValues(self):
        conn_dict = {}

        if self.view.dbComboBox.GetValue() == u'Microsoft SQL Server':
            conn_dict['engine'] = 'mssql'
        elif self.view.dbComboBox.GetValue() == u'MySQL':
            conn_dict['engine'] = 'mysql'
        else:
            conn_dict['engine'] = self.view.dbComboBox.GetValue()

        conn_dict['user'] = self.view.txtUser.GetValue()
        conn_dict['password'] = self.view.txtPass.GetValue()
        conn_dict['address'] = self.view.txtServer.GetValue()
        conn_dict['db'] = self.view.txtDBName.GetValue()
        return conn_dict