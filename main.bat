
set fileName=SpringExample01.py
set fromPath=D:\AbaqusPython\Spring\
set toPath=d:\simulia\temp

copy %fromPath%%fileName% %toPath% /y
abaqus cae noGUI=%fileName%

