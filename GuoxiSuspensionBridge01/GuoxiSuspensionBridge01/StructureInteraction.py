import interaction
class StructureInteraction(object):
    """Create 'Interaction' of the structure"""

    def __init__(self,structureModel,structureGeometry,structureAssembly,structureRegionSet):

        self.structureModel=structureModel
        self.structureGeometry=structureGeometry
        self.structureAssembly=structureAssembly
        self.structureRegionSet=structureRegionSet

    def CreateInteraction(self):
        """Create interaction module of the structure"""
        self.__CreateRefPoints()
        self.__CreateRigidBodyConstraint()

    def __CreateRefPoints(self):
        """Create reference points of the structure"""
        rGR=self.structureGeometry.rGirderRigidarmCoordinate
        v = self.structureAssembly.instances['PartAll-1'].vertices

        lst=[]
        for i in range(0,len(rGR)):
            rf=self.structureAssembly.ReferencePoint(point=v.findAt(coordinates=rGR[i]))    #returns feature, not referencePoint
            lst.append(rf)
        self.refPoints=tuple(lst)

    def __CreateRigidBodyConstraint(self):
        """Create rigid body constraint of the structure"""
        import regionToolset

        gR=self.structureRegionSet.girderRigidarmRegionSet

        rGR=self.structureGeometry.rGirderRigidarmCoordinate

        #v= self.structureAssembly.instances['PartAll-1'].vertices
        
        for i in range(0,len(gR)):
            for j in range(0,len(gR[i])):     
                region1=regionToolset.Region(referencePoints=(self.structureAssembly.referencePoints.findAt(rGR[j],),))     #convert from ReferencesPoints to Region
                self.structureModel.RigidBody(name='Constraint-Rigidbody-'+str(i+1)+'-'+str(j+1),
                    refPointRegion=region1, bodyRegion=self.structureAssembly.instances['PartAll-1'].sets['girderRigidarm'+str(i+1)+'-'+str(j+1)])
        
        '''
        reference code:
        
        a = mdb.models['GuoxiSuspensionBridge'].rootAssembly
        e1 = a.instances['PartAll-1'].edges
        edges1 = e1.findAt(((15.0, 8.0675, 2.8125), ))
        region2=regionToolset.Region(edges=edges1)
        a = mdb.models['GuoxiSuspensionBridge'].rootAssembly
        r1 = a.referencePoints
        refPoints1=(r1[129], )
        region1=regionToolset.Region(referencePoints=refPoints1)
        mdb.models['GuoxiSuspensionBridge'].RigidBody(name='Constraint-37', 
            refPointRegion=region1, bodyRegion=region2)
        '''