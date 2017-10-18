
set fileName=UniformLoad_main.py
set fromPath=D:\AbaqusPython\UniformLoad\
set toPath=d:\simulia\temp

copy %fromPath%%fileName% %toPath% /y
abaqus cae noGUI=%fileName%

