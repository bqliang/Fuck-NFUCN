start %~dp0ConfigureAccountPassword.exe

@echo off
::���ó�����ļ�������·������ѡ��
set Program=%~dp0�Զ���ѡ��.exe
 
::���ÿ�ݷ�ʽ���ƣ���ѡ��
set LnkName=Wifi Con
 
::���ó���Ĺ���·����һ��Ϊ������Ŀ¼�����������գ��ű������з���·��
set WorkDir=
 
::���ÿ�ݷ�ʽ��ʾ��˵������ѡ��
set Desc=

::���ÿ�ݷ�ʽͼ��
set icon=%~dp0/wifi.ico
 
if not defined WorkDir call:GetWorkDir "%Program%"
(echo Set WshShell=CreateObject("WScript.Shell"^)
echo strDesKtop=WshShell.SpecialFolders("DesKtop"^)
echo Set oShellLink=WshShell.CreateShortcut(strDesKtop^&"\%LnkName%.lnk"^)
echo oShellLink.TargetPath="%Program%"
echo oShellLink.WorkingDirectory="%WorkDir%"
echo oShellLink.WindowStyle=1
echo oShellLink.Description="%Desc%"
echo oShellLink.IconLocation="%icon%"
echo oShellLink.Save)>makelnk.vbs
echo �����ݷ�ʽ�����ɹ���
makelnk.vbs
del /f /q makelnk.vbs
exit
goto :eof
:GetWorkDir
set WorkDir=%~dp1
set WorkDir=%WorkDir:~,-1%
goto :eof