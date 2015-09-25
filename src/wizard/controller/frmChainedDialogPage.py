

class ChainedDialogPage:
    '''
    This interface is designed to add functionality
    for passing data between panels within
    ChainedDialog.
    '''
    def __init__(self):
        self.inputDict = {}

    def getInput(self):
        '''
        Returns the data from the current panel.

        Return value: dict
        '''
        raise NotImplementedError

    def setInput(self, data):
        '''
        Populate the controls/widgets with the
        given data.

        Return value: None
        '''
        raise NotImplementedError
    
