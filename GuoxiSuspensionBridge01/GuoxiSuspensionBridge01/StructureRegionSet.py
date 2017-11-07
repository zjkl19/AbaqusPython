from abaqusConstants import *
class StructureRegionSet(object):
    """store abaqus region set of the structure"""

    def __init__(self,structureModel,structureGeometry):
        """init

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        self.structureModel=structureModel
        self.structureGeometry=structureGeometry
        

    def CreateRegionSet(self):
        """Create Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        self.__CreateTowerRegionSet()
        self.__CreateGirderRegionSet()
        self.__CreateCableRegionSet()
        self.__CreateSuspenderRegionSet()


    def __CreateTowerRegionSet(self):
        """Create tower region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        self.__CreateDownTowerRegionSet()
        self.__CreateUpTowerRegionSet()
        self.__CreateTowerBeamRegionSet()


    def __CreateDownTowerRegionSet(self):
        """Create down tower region set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        rUT=self.structureGeometry.rUpDownTowerCoordinate
        dTB=self.structureGeometry.downTowerBottomCoordinate

        p = self.structureModel.parts['PartAll']
        e = p.edges
        coff=0.5    #get middle point

        downTowerRegionSet=[]

        for i in range(len(rUT)):
            lst=[]
            for j in range(len(rUT[i])):  
                edges = e.findAt(((coff*(rUT[i][j][0]+dTB[i][j][0]), coff*(rUT[i][j][1]+dTB[i][j][1]), coff*(rUT[i][j][2]+dTB[i][j][2])),))
                pSet=p.Set(edges=edges, name='downTowerSet'+str(i+1)+'-'+str(j+1))
                lst.append(pSet)
            downTowerRegionSet.append(tuple(lst))
        self.downTowerRegionSet=downTowerRegionSet

    def __CreateUpTowerRegionSet(self):
        """Create up tower Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        uTT=self.structureGeometry.upTowerTopCoordinate
        rUT=self.structureGeometry.rUpDownTowerCoordinate

        p = self.structureModel.parts['PartAll']
        e = p.edges
        coff=0.5    #get middle point

        upTowerRegionSet=[]

        for i in range(len(uTT)):
            lst=[]
            for j in range(len(uTT[i])):  
                edges = e.findAt(((coff*(uTT[i][j][0]+rUT[i][j][0]), coff*(uTT[i][j][1]+rUT[i][j][1]), coff*(uTT[i][j][2]+rUT[i][j][2])),))
                pSet=p.Set(edges=edges, name='upTowerSet'+str(i+1)+'-'+str(j+1))
                lst.append(pSet)
            upTowerRegionSet.append(tuple(lst))
        self.upTowerRegionSet=upTowerRegionSet

    def __CreateTowerBeamRegionSet(self):
        """Create region set of the beam of the tower

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        upTowerTopCoordinate=(((25,20.44,-3.75),(25,20.44,3.75)),
                                    ((95,20.44,-3.75),(95,20.44,3.75)))

        uTT=self.structureGeometry.upTowerTopCoordinate

        p = self.structureModel.parts['PartAll']
        e = p.edges
        coff=0.5    #get middle point
        
        
        lst=[]
        for i in range(len(uTT)):
            edges = e.findAt(((coff*(uTT[i][0][0]+uTT[i][1][0]), coff*(uTT[i][0][1]+uTT[i][1][1]), coff*(uTT[i][0][2]+uTT[i][1][2])),))
            pSet=p.Set(edges=edges, name='towerBeamSet'+str(i+1))
            lst.append(pSet)
        self.towerBeamRegionSet=tuple(lst)

    def __CreateGirderRegionSet(self):
        """Create Girder Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        
        p = self.structureModel.parts['PartAll']
        e = p.edges
        edges = e.findAt(((11.25, 8.189375, 0.0), ))
        region=p.Set(edges=edges, name='Set-1')
        p = self.structureModel.parts['PartAll']
        p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
            -1.0))
        #: Beam orientations have been assigned to the selected regions.

        self.__CreateGirderA_ARegionSet()
        self.__CreateGirderB_BRegionSet()
        self.__CreateGirderC_CRegionSet()
        self.__CreateGirderD_DRegionSet()
        self.__CreateGirderE_ERegionSet()
        self.__CreateGirderF_FRegionSet()
        self.__CreateGirderRigidarmRegionSet()

    def __CreateGirderA_ARegionSet(self):
        """Create Girder A-A Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        sG=self.structureGeometry.stiffeningGirderCoordinate
        p = self.structureModel.parts['PartAll']
        e = p.edges
        coff=0.5    #get middle point

        lst=[]
        for i in range(len(sG)-1):
            edges = e.findAt(((coff*(sG[i][0]+sG[i+1][0]), coff*(sG[i][1]+sG[i+1][1]), coff*(sG[i][2]+sG[i+1][2])),))
            pSet=p.Set(edges=edges, name='girderSet'+str(i+1))
            lst.append(pSet)

        self.girderRegionSet=tuple(lst)

    def __CreateGirderB_BRegionSet(self):
        """Create Girder B-B Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __CreateGirderC_CRegionSet(self):
        """Create Girder C-C Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __CreateGirderD_DRegionSet(self):
        """Create Girder D-D Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __CreateGirderE_ERegionSet(self):
        """Create Girder E-E Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __CreateGirderF_FRegionSet(self):
        """Create Girder F-F Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        pass

    def __CreateGirderRigidarmRegionSet(self):
        """Create Girder Rigidarm Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """

        rRS=self.structureGeometry.rRigidarmSuspenderCoordinate
        rGR=self.structureGeometry.rGirderRigidarmCoordinate

        p = self.structureModel.parts['PartAll']
        e = p.edges
        coff=0.5    #get middle point

        self.girderRigidarmRegionSet=[]
        
        for i in range(len(rRS)):
            lst=[]
            for j in range(len(rRS[i])-1):
                edges = e.findAt(((coff*(rRS[i][j][0]+rGR[j][0]), coff*(rRS[i][j][1]+rGR[j][1]), coff*(rRS[i][j][2]+rGR[j][2])),))
                pSet=p.Set(edges=edges, name='girderRigidarm'+str(i+1)+'-'+str(j+1))
                lst.append(pSet)
            self.girderRigidarmRegionSet.append(tuple(lst))
        
        self.girderRigidarmRegionSet=tuple(self.girderRigidarmRegionSet)

    def __CreateCableRegionSet(self):
        """Create Cable Region Set
        create each section of a cable a set 

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        c=self.structureGeometry.cableCoordinate
        p = self.structureModel.parts['PartAll']
        e = p.edges
        coff=0.5    #get middle point

        self.cableRegionSet=[]
        
        for i in range(len(c)):
            lst=[]
            for j in range(len(c[i])-1):  
                edges = e.findAt(((coff*(c[i][j][0]+c[i][j+1][0]), coff*(c[i][j][1]+c[i][j+1][1]), coff*(c[i][j][2]+c[i][j+1][2])),))
                pSet=p.Set(edges=edges, name='cableSet'+str(i+1)+'-'+str(j+1))
                lst.append(pSet)
            self.cableRegionSet.append(tuple(lst))
        
        self.cableRegionSet=tuple(self.cableRegionSet)
            

    def __CreateSuspenderRegionSet(self):
        """Create Suspender Region Set

        Required argument:

        Optional arguments:

        None.

        Return value:

        Exceptions:

        None.
        """
        rRS=self.structureGeometry.rRigidarmSuspenderCoordinate
        hP=self.structureGeometry.hangingPointCoordinate

        p = self.structureModel.parts['PartAll']
        e = p.edges
        coff=0.5    #get middle point

        self.suspenderRegionSet=[]

        for i in range(len(rRS)):
            lst=[]
            for j in range(len(rRS[i])):     
                edges = e.findAt(((coff*(rRS[i][j][0]+hP[i][j][0]), coff*(rRS[i][j][1]+hP[i][j][1]), coff*(rRS[i][j][2]+hP[i][j][2])),))
                pSet=p.Set(edges=edges, name='suspenderSet'+str(i+1)+'-'+str(j+1))
                lst.append(pSet)    
            self.suspenderRegionSet.append(tuple(lst))
        
        self.suspenderRegionSet=tuple(self.suspenderRegionSet)
