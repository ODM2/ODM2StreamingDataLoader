from odm2api.ODM2.services.readService \
    import DetailedResult

class ResultMapping(DetailedResult):
    def __init__(self, result, samplingFeature,
        samplingFeatureName, method,
        methodName, variable, variableNameCV,
        processingLevel, processingLevelDef,
        unit, variableName=None):

        self.resultID=result
        self.samplingFeatureCode=samplingFeature
        self.samplingFeatureName=samplingFeatureName
        self.methodCode=method
        self.methodName=methodName
        self.variableCode=variable
        self.variableNameCV=variableNameCV
        self.processingLevelCode=processingLevel
        self.processingLevelDef=processingLevelDef
        self.unitsName=unit
        self.variableName = variableName

