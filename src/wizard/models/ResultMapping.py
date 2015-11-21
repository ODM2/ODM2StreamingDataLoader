from api.ODM2.services.readService \
    import DetailedResult

class ResultMapping(DetailedResult):
    def __init__(self, result, samplingFeature,
        method, variable, processingLevel,
        unit, variableName=None):

        self.resultID=result
        self.samplingFeatureCode=samplingFeature
        self.methodCode=method
        self.variableCode=variable
        self.processingLevelCode=processingLevel
        self.unitsName=unit
        self.variableName = variableName

