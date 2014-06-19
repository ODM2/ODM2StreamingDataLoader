__author__ = 'Jacob'

"""
    System Controller starts the controllers
"""
from streamdata.wizard.views.databaseChangerView import DatabaseChangerView

class SystemController:
    def __init__(self):
        pass

    def startSystem(self):
        """Initializes the system"""
        self.startSDLModel()
        self.startLoader()

    def startSDLModel(self):
        """Starts the SDLModel application"""

        ## Create Views
        self._createViews()
        ## Create Models
        self._createModels()
        ## Pass View and Model into each respective controllers
        self._createControllers()

    def _createViews(self):
        dbView = DatabaseChangerView()


        pass

    def startLoader(self):
        """Starts the Loader application"""
        pass



