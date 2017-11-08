from abaqusConstants import *
class StructureStep(object):
    """define the step"""

    def __init__(self,structureModel):
        self.structureModel=structureModel

    def CreateStep(self):
        import step    #required
        """abaqus:
            Create a step. The time period of the static step is 1.0, 
            and the initial incrementation is 0.1; the step is created
            after the initial step. 
        """ 
        self.structureModel.StaticStep(name='beamStep', previous='Initial',
            nlgeom=OFF)
    
        self.structureModel.FieldOutputRequest(name='F-Output-2', 
            createStepName='beamStep', variables=('SF',))       
    