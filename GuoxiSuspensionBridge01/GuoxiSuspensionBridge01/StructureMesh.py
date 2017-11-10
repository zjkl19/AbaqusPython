import abaqusConstants
import mesh
class StructureMesh(object):
    """mesh the structrue"""

    def __init__(self,structureModel,structureRegionSet,structureAssembly):
        self.structureModel=structureModel
        self.structurePart=structureModel.parts['PartAll']
        self.structureRegionSet=structureRegionSet
        self.structureAssembly=structureAssembly

    def CreateMesh(self):
        """create the mesh of the structrue"""
        
        Ediv=100   #the number of the Element division

        # Seed the part instance.
        self.structurePart.seedPart(size=1/Ediv,
            deviationFactor=0.01, minSizeFactor=0.01)

        self.__MeshTower()
        self.__MeshGirder()
        self.__MeshCable()
        self.__MeshSuspender()

        self.structureModel.parts['PartAll'].generateMesh()
        self.structureAssembly.regenerate()

    def __MeshTower(self):
        """mesh the tower"""
        self.__MeshDownTower()
        self.__MeshUpTower()
        self.__MeshTowerBeam()

    def __MeshDownTower(self):
        """mesh the down tower"""
        elemType=mesh.ElemType(elemCode=abaqusConstants.B32)

        dTR=self.structureRegionSet.downTowerRegionSet

        for i in range(len(dTR)):      
            for j in range(len(dTR[i])):
                self.structurePart.setElementType(regions=dTR[i][j], elemTypes=(elemType,))  

    def __MeshUpTower(self):
        """mesh the up tower"""
        elemType=mesh.ElemType(elemCode=abaqusConstants.B32)

        uTR=self.structureRegionSet.upTowerRegionSet

        for i in range(len(uTR)):      
            for j in range(len(uTR[i])):
                self.structurePart.setElementType(regions=uTR[i][j], elemTypes=(elemType,))

    def __MeshTowerBeam(self):
        """mesh the tower beam"""
        elemType=mesh.ElemType(elemCode=abaqusConstants.B32)

        tBRS=self.structureRegionSet.towerBeamRegionSet

        for i in range(len(tBRS)):      
            self.structurePart.setElementType(regions=tBRS[i], elemTypes=(elemType,))


    def __MeshGirder(self):
        """mesh the girder"""
        #girder
        elemType=mesh.ElemType(elemCode=abaqusConstants.B32)

        gRS=self.structureRegionSet.girderRegionSet

        for i in range(len(gRS)):
            self.structurePart.setElementType(regions=gRS[i], elemTypes=(elemType,))

        #girder rigidArm
        elemType=mesh.ElemType(elemCode=abaqusConstants.B32)

        gRRS=self.structureRegionSet.girderRigidarmRegionSet

        for i in range(len(gRRS)):
            for j in range(len(gRRS[i])):
                self.structurePart.setElementType(regions=gRRS[i][j], elemTypes=(elemType,))   

    def __MeshCable(self):
        """mesh the cable"""
        elemType=mesh.ElemType(elemCode=abaqusConstants.T3D2)

        cRS=self.structureRegionSet.cableRegionSet

        for i in range(len(cRS)):
            for j in range(len(cRS[i])):
                self.structurePart.setElementType(regions=cRS[i][j], elemTypes=(elemType,))

    def __MeshSuspender(self):
        """mesh the suspender"""
        elemType=mesh.ElemType(elemCode=abaqusConstants.T3D2)

        sRS=self.structureRegionSet.suspenderRegionSet

        for i in range(len(sRS)):
            for j in range(len(sRS[i])):
                self.structurePart.setElementType(regions=sRS[i][j], elemTypes=(elemType,))