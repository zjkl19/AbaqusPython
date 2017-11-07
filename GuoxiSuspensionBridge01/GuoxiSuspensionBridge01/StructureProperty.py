from abaqusConstants import *
class StructureProperty(object):
    """Properties of the structure, including material, profile, section"""

    def __init__(self,structureModel,structureRegionSet):
        self.structureModel=structureModel
        self.structureRegionSet=structureRegionSet

    def CreateProperty(self):
        """set the material, profile and section property

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        self.__CreateMaterial()
        self.__CreateProfile()
        self.__CreateSection()

        self.__SectionAssignment()
        self.__AssignBeamSectionOrientation()
    
    def __CreateMaterial(self):
        """create the material

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """


        #must operate manual at the time being

        #cable Material
        cableMaterial=self.structureModel.Material(name='cableMaterial')
        cableMaterial.Density(table=((8518.367347, ), ))    #density     
        cableMaterial.Elastic(table=((2.00E+11, 0.3), ))    #Young's module, possion ratio
        self.cableMaterial=cableMaterial

        #suspender Material
        suspenderMaterial=self.structureModel.Material(name='suspenderMaterial')
        suspenderMaterial.Density(table=((9050, ), ))    #density     
        suspenderMaterial.Elastic(table=((2.00E+11, 0.3), ))    #Young's module, possion ratio
        self.suspenderMaterial=suspenderMaterial

        #C50 Material
        C50Material=self.structureModel.Material(name='C50Material')
        C50Material.Density(table=((2549, ), ))    #density     
        C50Material.Elastic(table=((3.45E+10, 0.2), ))    #Young's module, possion ratio
        self.C50Material=C50Material


    def __CreateProfile(self):
        """create the profile

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        #Tower profile
        downTowerProfile=self.structureModel.RectangularProfile(name='downTowerProfile', a=1.3, b=1.6)  #bottom:a height:b

        upTowerProfile=self.structureModel.RectangularProfile(name='upTowerProfile', a=0.9, b=1.4)

        towerBeamProfile=self.structureModel.RectangularProfile(name='towerBeamProfile', a=0.8, b=0.76)



        #girder profile
        A_AProfile=self.structureModel.GeneralizedProfile(name='A-AProfile', area=3.24, i11=1.54E-01, i12=0, i22=2.17E+01, j=2.64E-01, gammaO=0.0, gammaW=0.0) 

        C_CProfile=self.structureModel.GeneralizedProfile(name='C-CProfile', area=5.74, i11=3.11E-01, i12=0, i22=2.55E+01, j=1.07834, gammaO=0.0, gammaW=0.0)

        E_EProfile=self.structureModel.GeneralizedProfile(name='E-EProfile', area=1.82E+01, i11=6.07E+00, i12=0, i22=1.26E+02, j=2.14E+01, gammaO=0.0, gammaW=0.0)


        F_FProfile=self.structureModel.GeneralizedProfile(name='F-FProfile', area=1.24E+01, i11=1.94E+00, i12=0, i22=8.58E+01, j=7.24E+00, gammaO=0.0, gammaW=0.0)


        
        #cable profile
        #The CircularProfile object is derived from the Profile object
        cableProfile=self.structureModel.CircularProfile(name='cableProfile', r=0.10695)

        #suspender profile
        suspenderProfile=self.structureModel.CircularProfile(name='suspenderProfile', r=0.031022)	

    def __CreateSection(self):
        """create the section

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """ 

        #tower section
        downTowerSection=self.structureModel.BeamSection(name='downTowerSection', 
              integration=BEFORE_ANALYSIS, profile='downTowerProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        upTowerSection=self.structureModel.BeamSection(name='upTowerSection', 
              integration=BEFORE_ANALYSIS, profile='upTowerProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        towerBeamSection=self.structureModel.BeamSection(name='towerBeamSection', 
              integration=BEFORE_ANALYSIS, profile='towerBeamProfile',
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        #girder section
        A_ASection=self.structureModel.BeamSection(name='A-ASection', 
              integration=BEFORE_ANALYSIS, profile='A-AProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        C_CSection=self.structureModel.BeamSection(name='C-CSection', 
              integration=BEFORE_ANALYSIS, profile='A-AProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        E_ESection=self.structureModel.BeamSection(name='E-ESection', 
              integration=BEFORE_ANALYSIS, profile='A-AProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False)

        F_FSection=self.structureModel.BeamSection(name='F-FSection', 
              integration=BEFORE_ANALYSIS, profile='A-AProfile', 
              material='C50Material', temperatureVar=LINEAR, consistentMassMatrix=False) 
 
        #cable section
        A=3.14159*self.structureModel.profiles['cableProfile'].r**2
        cableSection=self.structureModel.TrussSection(name='cableSection', material='cableMaterial', 
            area=A)

        #suspender section
        A=3.14159*self.structureModel.profiles['suspenderProfile'].r**2
        suspenderProfile=self.structureModel.CircularProfile(name='suspenderSection', r=0.031022)
        suspenderSection=self.structureModel.TrussSection(name='suspenderSection', material='suspenderMaterial', 
            area=A)	
       
    def __SectionAssignment(self):
        """assign the truss and beam section

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """     
        self.__AssignTowerSection()
        self.__AssignGirderSection()
        self.__AssignCableSection()
        self.__AssignSuspenderSection()

 
    def __AssignTowerSection(self):
        """Assign tower section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        self.__AssignDownTowerSection()
        self.__AssignUpTowerSection()
        self.__AssignTowerBeamSection()


    def __AssignDownTowerSection(self):
        """assign down tower section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        r=self.structureRegionSet.downTowerRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            for j in range(len(r[i])):
                myPart.SectionAssignment(region=r[i][j], sectionName='downTowerSection', offset=0.0, 
                    offsetType=MIDDLE_SURFACE, offsetField='', 
                    thicknessAssignment=FROM_SECTION)

    def __AssignUpTowerSection(self):
        """assign up tower section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        r=self.structureRegionSet.upTowerRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            for j in range(len(r[i])):
                myPart.SectionAssignment(region=r[i][j], sectionName='upTowerSection', offset=0.0, 
                    offsetType=MIDDLE_SURFACE, offsetField='', 
                    thicknessAssignment=FROM_SECTION)

    def __AssignTowerBeamSection(self):
        """assign section of the beam of the tower

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        r=self.structureRegionSet.towerBeamRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            myPart.SectionAssignment(region=r[i], sectionName='towerBeamSection', offset=0.0, 
                offsetType=MIDDLE_SURFACE, offsetField='', 
                thicknessAssignment=FROM_SECTION)

    def __AssignGirderSection(self):
        """Create Girder Section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        self.__AssignGirderA_ASection()
        self.__AssignGirderB_BSection()
        self.__AssignGirderC_CSection()
        self.__AssignGirderD_DSection()
        self.__AssignGirderE_ESection()
        self.__AssignGirderF_FSection()
        self.__AssignGirderRigidarmSection()

    def __AssignGirderA_ASection(self):
        """Create Girder A-A Section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        r=self.structureRegionSet.girderRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            myPart.SectionAssignment(region=r[i], sectionName='A-ASection', offset=0.0, 
                offsetType=MIDDLE_SURFACE, offsetField='', 
                thicknessAssignment=FROM_SECTION)

    def __AssignGirderB_BSection(self):
        """Create Girder B-B Section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __AssignGirderC_CSection(self):
        """Create Girder C-C Section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __AssignGirderD_DSection(self):
        """Create Girder D-D Section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __AssignGirderE_ESection(self):
        """Create Girder E-E Section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __AssignGirderF_FSection(self):
        """Create Girder F-F Section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __AssignGirderRigidarmSection(self):
        """Create Girder Rigidarm Section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __AssignCableSection(self):
        """assign cable section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        r=self.structureRegionSet.cableRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            for j in range(len(r[i])):
                myPart.SectionAssignment(region=r[i][j], sectionName='cableSection', offset=0.0, 
                    offsetType=MIDDLE_SURFACE, offsetField='', 
                    thicknessAssignment=FROM_SECTION)
            

    def __AssignSuspenderSection(self):
        """assign suspender section

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        r=self.structureRegionSet.suspenderRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            for j in range(len(r[i])):
                myPart.SectionAssignment(region=r[i][j], sectionName='suspenderSection', offset=0.0, 
                    offsetType=MIDDLE_SURFACE, offsetField='', 
                    thicknessAssignment=FROM_SECTION)

    def __AssignBeamSectionOrientation(self):
        """assign the beam section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """     
        self.__AssignTowerSectionOrientation()
        self.__AssignGirderBeamSectionOrientation()
        self.__AssignCableBeamSectionOrientation()
        self.__AssignSuspenderBeamSectionOrientation()

    def __AssignTowerSectionOrientation(self):
        """assign the tower section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """ 
        self.__AssignDownTowerBeamSectionOrientation()
        self.__AssignUpTowerBeamSectionOrientation()
        self.__AssignTowerBeamBeamSectionOrientation()

    def __AssignDownTowerBeamSectionOrientation(self):
        """assign the down tower section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        r=self.structureRegionSet.downTowerRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            for j in range(len(r[i])):
                myPart.assignBeamSectionOrientation(region=r[i][j], method=N1_COSINES, n1=(0.0, 0.0, -1.0))
 
    def __AssignUpTowerBeamSectionOrientation(self):
        """assign the up tower section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        r=self.structureRegionSet.upTowerRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            for j in range(len(r[i])):
                myPart.assignBeamSectionOrientation(region=r[i][j], method=N1_COSINES, n1=(0.0, 0.0, -1.0))

    def __AssignTowerBeamBeamSectionOrientation(self):
        """assign the tower beam section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        r=self.structureRegionSet.towerBeamRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            myPart.assignBeamSectionOrientation(region=r[i], method=N1_COSINES, n1=(-1.0, 0.0, 0.0))


    def __AssignGirderBeamSectionOrientation(self):
        """assign the girder beam section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        self.__AssignGirderA_ABeamSectionOrientation()
        self.__AssignGirderB_BBeamSectionOrientation()
        self.__AssignGirderC_CBeamSectionOrientation()
        self.__AssignGirderD_DBeamSectionOrientation()
        self.__AssignGirderE_EBeamSectionOrientation()
        self.__AssignGirderF_FBeamSectionOrientation()
        self.__AssignGirderRigidarmBeamSectionOrientation()

    def __AssignGirderA_ABeamSectionOrientation(self):
        """assign the girder A-A beam section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        r=self.structureRegionSet.girderRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            myPart.assignBeamSectionOrientation(region=r[i], method=N1_COSINES, n1=(0.0, 0.0, -1.0))

    
    def __AssignGirderB_BBeamSectionOrientation(self):
        pass

    def __AssignGirderC_CBeamSectionOrientation(self):
        pass

    def __AssignGirderD_DBeamSectionOrientation(self):
        pass

    def __AssignGirderE_EBeamSectionOrientation(self):
        pass

    def __AssignGirderF_FBeamSectionOrientation(self):
        pass

    def __AssignGirderRigidarmBeamSectionOrientation(self):
        pass

    def __AssignCableBeamSectionOrientation(self):
        """assign the cable beam section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        r=self.structureRegionSet.cableRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            for j in range(len(r[i])):
                myPart.assignBeamSectionOrientation(region=r[i][j], method=N1_COSINES, n1=(0.0, 0.0, -1.0))

    def __AssignSuspenderBeamSectionOrientation(self):
        """assign the suspender section orientation

        must operate manually

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        r=self.structureRegionSet.suspenderRegionSet

        myPart = self.structureModel.parts['PartAll']
 
        for i in range(len(r)):
            for j in range(len(r[i])):
                myPart.assignBeamSectionOrientation(region=r[i][j], method=N1_COSINES, n1=(0.0, 0.0, -1.0))    