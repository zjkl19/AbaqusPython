
set fileName=SimpleSupportBeam(IProfile).py
set fromPath=D:\AbaqusPython\CompareGeneralProfileIProfile(BEAM)\
set toPath=d:\simulia\temp

copy %fromPath%%fileName% %toPath% /y
abaqus cae noGUI=%fileName%

