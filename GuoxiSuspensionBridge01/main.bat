
set fileName=GuoxiSuspensionBridge.py
set fromPath=D:\AbaqusPython\GuoxiSuspensionBridge01\GuoxiSuspensionBridge01
set toPath=D:\simulia\temp\

xcopy %fromPath% %toPath%  /e /h /y
abaqus cae noGUI=%toPath%%fileName%

