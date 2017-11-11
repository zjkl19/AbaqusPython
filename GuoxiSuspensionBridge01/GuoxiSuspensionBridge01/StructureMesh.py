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
        
        Ediv=10   #the number of the Element division

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
                #self.structurePart.seedEdgeByNumber(edges=cRS[i][j], number=1, constraint=abaqusConstants.FINER)
        p = self.structureModel.parts['PartAll']
        e = p.edges
        pickedEdges = e.findAt(((112.8625, 10.071177, 3.75), ), ((106.25, 13.247756, 
            3.75), ), ((101.25, 16.154657, 3.75), ), ((96.25, 19.555984, 3.75), ), ((
            91.25, 18.55102, 3.75), ), ((86.25, 16.435626, 3.75), ), ((81.25, 
            14.725042, 3.75), ), ((76.25, 13.374846, 3.75), ), ((71.25, 12.38486, 
            3.75), ), ((66.25, 11.754939, 3.75), ), ((61.25, 11.48499, 3.75), ), ((
            56.25, 11.574971, 3.75), ), ((51.25, 12.024896, 3.75), ), ((46.25, 
            12.834833, 3.75), ), ((41.25, 14.004901, 3.75), ), ((36.25, 15.535269, 
            3.75), ), ((31.25, 17.426116, 3.75), ), ((26.25, 19.81034, 3.75), ), ((
            21.25, 17.787953, 3.75), ), ((16.25, 14.656099, 3.75), ), ((11.25, 
            11.929632, 3.75), ), ((3.5875, 7.672392, 3.75), ), ((96.25, 19.555984, 
            -3.75), ), ((91.25, 18.55102, -3.75), ), ((86.25, 16.435626, -3.75), ), ((
            81.25, 14.725042, -3.75), ), ((76.25, 13.374846, -3.75), ), ((71.25, 
            12.38486, -3.75), ), ((66.25, 11.754939, -3.75), ), ((61.25, 11.48499, 
            -3.75), ), ((56.25, 11.574971, -3.75), ), ((51.25, 12.024896, -3.75), ), ((
            46.25, 12.834833, -3.75), ), ((41.25, 14.004901, -3.75), ), ((36.25, 
            15.535269, -3.75), ), ((31.25, 17.426116, -3.75), ), ((26.25, 19.81034, 
            -3.75), ), ((21.25, 17.787953, -3.75), ), ((16.25, 14.656099, -3.75), ), ((
            11.25, 11.929632, -3.75), ), ((3.5875, 7.672392, -3.75), ), ((112.8625, 
            10.071177, -3.75), ), ((106.25, 13.247756, -3.75), ), ((101.25, 16.154657, 
            -3.75), ))
        p.seedEdgeByNumber(edges=pickedEdges, number=1, constraint=abaqusConstants.FINER)

    def __MeshSuspender(self):
        """mesh the suspender"""
        elemType=mesh.ElemType(elemCode=abaqusConstants.T3D2)

        sRS=self.structureRegionSet.suspenderRegionSet

        for i in range(len(sRS)):
            for j in range(len(sRS[i])):
                self.structurePart.setElementType(regions=sRS[i][j], elemTypes=(elemType,))
                #self.structurePart.seedEdgeByNumber(edges=sRS[i][j], number=1, constraint=abaqusConstants.FINER)

        
        p = self.structureModel.parts['PartAll']
        e = p.edges
        pickedEdges = e.findAt(((110.0, 10.385427, 3.75), ), ((105.0, 12.421989, 3.75), 
            ), ((100.0, 14.722953, 3.75), ), ((90.0, 15.57352, 3.75), ), ((85.0, 
            14.122162, 3.75), ), ((80.0, 12.934946, 3.75), ), ((75.0, 12.011739, 3.75), 
            ), ((70.0, 11.352406, 3.75), ), ((65.0, 10.956846, 3.75), ), ((60.0, 
            10.825, 3.75), ), ((55.0, 10.956846, 3.75), ), ((50.0, 11.352406, 3.75), ), 
            ((45.0, 12.011739, 3.75), ), ((40.0, 12.934946, 3.75), ), ((35.0, 
            14.122162, 3.75), ), ((30.0, 15.57352, 3.75), ), ((20.0, 14.722953, 3.75), 
            ), ((15.0, 12.421989, 3.75), ), ((10.0, 10.385427, 3.75), ), ((80.0, 9.08, 
            -0.9375), ), ((70.0, 9.23, -0.9375), ), ((110.0, 10.385427, -3.75), ), ((
            105.0, 12.421989, -3.75), ), ((100.0, 14.722953, -3.75), ), ((90.0, 
            15.57352, -3.75), ), ((85.0, 14.122162, -3.75), ), ((80.0, 12.934946, 
            -3.75), ), ((75.0, 12.011739, -3.75), ), ((70.0, 11.352406, -3.75), ), ((
            65.0, 10.956846, -3.75), ), ((60.0, 10.825, -3.75), ), ((55.0, 10.956846, 
            -3.75), ), ((50.0, 11.352406, -3.75), ), ((45.0, 12.011739, -3.75), ), ((
            40.0, 12.934946, -3.75), ), ((35.0, 14.122162, -3.75), ), ((30.0, 15.57352, 
            -3.75), ), ((20.0, 14.722953, -3.75), ), ((15.0, 12.421989, -3.75), ), ((
            10.0, 10.385427, -3.75), ))
        p.seedEdgeByNumber(edges=pickedEdges, number=1, constraint=abaqusConstants.FINER)