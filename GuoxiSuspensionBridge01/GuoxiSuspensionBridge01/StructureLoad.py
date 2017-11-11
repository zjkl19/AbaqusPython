from abaqusConstants import *
class StructureLoad(object):
    """define the load of the structure
       
    load convensions:

    position unsummetirc: one dimension tuple
    1st dimension: load

    for example:
  
    position symmetric: two dimension tuple
    1st dimension: north-south pointer, [0]: north, [1]: south
    2nd dimension: load
    
    for example:
    suspenderPredefinedLoad=((395.2283,	262.915, 395.6083,
                              397.2881, 264.5417, 264.7815, 264.7639, 264.9563, 264.9458, 264.9483, 264.941, 264.9465,	264.7482, 264.7559,	264.5617, 396.6539,
                              387.5433, 258.0443, 387.8515),
                             (395.2458,	262.9267, 395.6258,
                              397.3084,	264.5552, 264.7951,	264.7775, 264.9699,	264.9593, 264.9619, 264.9546, 264.9601,	264.7618, 264.7695,	264.5753, 396.6741,
                              387.5672, 258.0603, 387.8756))
   
    """

    def __init__(self,structureModel,structureAssembly,structureRegionSet):
        self.structureModel=structureModel
        self.structureAssembly=structureAssembly
        self.structureRegionSet=structureRegionSet

        self.__SetCablePredefinedLoad()
        self.__SetSuspenderPredefinedLoad()

    def __SetCablePredefinedLoad(self):
        """set the cable of predefined load"""

        cablePredefinedLoad=[[4047.9108, 4220.5794, 4352.7746, 4572.7058,
                             4201.9074, 4036.4827, 3944.8393, 3870.011, 3812.9638,	3774.473, 3755.0872, 3755.0909,	3774.4835, 3812.9793, 3870.0286, 3944.8536,	4036.5072, 4201.652, 
                             4488.9624,	4273.4517, 4143.64,	3974.1143],
                             [4048.0861, 4220.7623, 4352.9632, 4572.9039,
                             4202.1183,	4036.6853, 3945.0373, 3870.2052, 3813.1551,	3774.6625, 3755.2757, 3755.2794, 3774.6729,	3813.1707, 3870.2228, 3945.0516, 4036.7098,	4201.8629,
                             4489.2343,	4273.7106, 4143.8909, 3974.3549]]    #KN

        c=[]
        for i in range(0,len(cablePredefinedLoad)):
            k=[i*1000 for i in cablePredefinedLoad[i]]
            c.append(tuple(k))

        self.cablePredefinedLoad=tuple(c)

    def __SetSuspenderPredefinedLoad(self):
        """set the suspender of predefined load"""

        suspenderPredefinedLoad=[[395.2283,	262.915, 395.6083,
                                  397.2881, 264.5417, 264.7815, 264.7639, 264.9563, 264.9458, 264.9483, 264.941, 264.9465,	264.7482, 264.7559,	264.5617, 396.6539,
                                  387.5433, 258.0443, 387.8515],
                                 [395.2458,	262.9267, 395.6258,
                                  397.3084,	264.5552, 264.7951,	264.7775, 264.9699,	264.9593, 264.9619, 264.9546, 264.9601,	264.7618, 264.7695,	264.5753, 396.6741,
                                  387.5672, 258.0603, 387.8756]]    #KN

        c=[]
        for i in range(0,len(suspenderPredefinedLoad)):
            k=[i*1000 for i in suspenderPredefinedLoad[i]]
            c.append(tuple(k))

        self.suspenderPredefinedLoad=tuple(c)

    def CreateLoad(self):
        """create the load of structure"""
        self.__CreateDisplacementBC()
        self.__CreateGravityLoad()
        self.__CreatePredefinedField()
        

    def __CreateDisplacementBC(self):
        """create the displacement of the structure

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        import regionToolset

        structureGeometry=self.structureRegionSet.structureGeometry    #reference
        aP=structureGeometry.anchorPointCoordinate

        v1 = self.structureAssembly.instances['PartAll-1'].vertices

        for i in range(len(aP)):
            for j in range(len(aP[i])):
                verts1 = v1.findAt((aP[i][j], ))
                region = regionToolset.Region(vertices=verts1)
                self.structureModel.DisplacementBC(name='cableBC'+str(i+1)+str('-')+str(j+1), 
                    createStepName='beamStep', region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, 
                    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
                    fieldName='', localCsys=None)


        dTB=structureGeometry.downTowerBottomCoordinate

        for i in range(len(dTB)):
            for j in range(len(dTB[i])):
                verts1 = v1.findAt((dTB[i][j], ))
                region = regionToolset.Region(vertices=verts1)
                self.structureModel.DisplacementBC(name='downTowerBC'+str(i+1)+str('-')+str(j+1), 
                    createStepName='beamStep', region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, 
                    ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
                    fieldName='', localCsys=None)

        EP=structureGeometry.EndPointCoordinate
        for i in range(len(EP)):
            verts1 = v1.findAt((EP[i], ))
            region = regionToolset.Region(vertices=verts1)
            self.structureModel.DisplacementBC(name='girderBC'+str(i+1), 
                createStepName='beamStep', region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, 
                ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, 
                fieldName='', localCsys=None)

    def __CreatePredefinedField(self):
        """create the predefined field of the structure"""
        self.__CreateCablePredefinedField()
        self.__CreateSuspenderPredefinedField()


    def __CreateCablePredefinedField(self):
        """create the cable predefined field of the structure"""

        A=3.14159*self.structureModel.profiles['cableProfile'].r**2    #area
        
        cableRegionSet=self.structureRegionSet.cableRegionSet
        
        for i in range(0,len(cableRegionSet)):
            for j in range(0,len(cableRegionSet[i])):
                self.structureModel.Stress(name='cablePredefinedField'+str(i+1)+'-'+str(j+1), 
                    region=self.structureAssembly.instances['PartAll-1'].sets['cableSet'+str(i+1)+'-'+str(j+1)],
                    distributionType=UNIFORM, sigma11=self.cablePredefinedLoad[i][j]/A, sigma22=0.0, 
                    sigma12=0.0, sigma33=None, sigma13=None, sigma23=None)

    def __CreateSuspenderPredefinedField(self):
        """create the suspender predefined field of the structure"""

        A=3.14159*self.structureModel.profiles['suspenderProfile'].r**2    #area
        
        suspenderRegionSet=self.structureRegionSet.suspenderRegionSet
        
        for i in range(0,len(suspenderRegionSet)):
            for j in range(0,len(suspenderRegionSet[i])):
                self.structureModel.Stress(name='suspenderPredefinedField'+str(i+1)+'-'+str(j+1), 
                    region=self.structureAssembly.instances['PartAll-1'].sets['suspenderSet'+str(i+1)+'-'+str(j+1)],
                    distributionType=UNIFORM, sigma11=self.suspenderPredefinedLoad[i][j]/A, sigma22=0.0, 
                    sigma12=0.0, sigma33=None, sigma13=None, sigma23=None)

    def __CreateGravityLoad(self):
        """create the gravity load of the structure"""


        self.structureModel.Gravity(name='GravityLoad', 
            createStepName='beamStep', comp2=-9.8, distributionType=UNIFORM, field='')

   