# Windows Forensics

## Семинар 14.09.2024

1. MFT : 47:00
1. XWay : 1:11:06

## Семинар 14.09.2024

1. Autopsy : 5:44
1. XWay : 13:12
1. Zimmerman : 23:52
1. Журнал событий : 26:45
    1. Удаленные входы (TerminalServices-RemoteConnectionManager-Operationals) : 27:58
    1. TerminalServices-LocalConnectionManager-Operationals : 29:10
    1. Security : 35:20
    1. Powershell : 36:06
        - evtx_dump.py : 37:58
    1. Timescatch : 42:43
    1. Chainsaw : 49:56
    1. Исходящие RDP : 54:16
1. Пользовательские файлы:
    1. User Terminal Cache (Снимки экрана сессий) : 57:49
        - bmc-tools : 59:00
    1. Powershell History : 01:02:40
1. AMCACHE : 01:09:39
1. User Assist : 01:15:45

## 4/9   Извлечение артефактов из файловой системы

### $MFT

1. about : 1:50
1. From disk image (FTKImager) : 2:18
1. Live System (DiskExplorer) : 6:50
    - MFT record : 8:12
1. Zimmerman
    - MFTExplorer : 14:54
    - MftECmd : 17:20
    - Timeline Explorer : 18:27

### Usn journal ($EXTEND\\$J)

1. Zimmerman (MFTECmd) : 22:10


## 5/9   Анализ артефактов исполнения

### AMCACHE

> sha1 от первых 31457280 байт

1. zimmerman parse : 2:14
1. Registry explorer parse : 7:06
    - InventoryApplicationFile : 8:32
1. regripper parse : 18:20

### SHIMCACHE

1. about : 24:20
1. ms registry : 25:32
    - AppCampatCashe : 25:53
1. Artefact: 26:46
    1. Zimmerman (AppCompatCacheParser) : 27:10
    1. Registry explorer : 32:00

### UserAssist (NTUSER.DAT)

1. about : 33:50
1. From disk image (FTKImager) : 34:21
1. Live machine : 35:16
1. Artefact:
    1. Location : 37:01
    1. Registry explorer : 37:16

### System Resource Utilization Monitore (SRU)

1. about : 40:50
1. Artefact:
    1. Location : 41:29
    1. Zimmerman (SrumECmd) : 42:47
        - AppResourceUsrInfo_Output.csv : 45:00

### Prefetch

1. About : 48:46
1. Artefact
    1. Location : 50:10
    1. Zimmerman (PECmd) : 52:08 
        - output : 56:05

## 6/9   Анализ активности пользователя

### AppData

1. intro : 1:00
1. PowerShell log : 2:00
1. Recent Files : 2:46
    1. Automatic Destiontion & Custom Destinations (Jump lists) : 4:25
        - Zimmerman (JLECmd) : 5:37
        - Timeline Explorer : 7:40
    1. LinkFiles : 14:42
         - Zimmerman (LECmd) : 15:24
    
### Реестр пользователя

1. Registry Explorer : 20:54

#### NTUser.DAT

1. Registry Explorer : 21:13
    - Available Bookmarks:
        1. Run : 21:35
        1. RunOnce : 22:21
        1. RunMRU : 22:56
        1. Recent Docs : 23:55
        1. Shell Bags : 26:39
        1. ComDlg32 : 28:03

#### RDP conections

1. 32:25

#### Исторя браузера

1. NirSoft - NirLauncher : 33:45
    - Web Browser Tools
        - BroswingHistoryView : 34:46

# Linux Forensics

## Семинар 21.09.2024

### GSocket

1. intro : 3:38
1. cron : 5:58
1. закреп в /usr/bin : 11:20
1. bashrc & bashprofile : 14:25
1. сервис : 15:20
1. logs : 17:30
1. to check : 19:45
1. hidden files : 20:40
1. ld so preload : 24:06

### RAM dump

1. intro : 37:25
1. lime : 37:46

### Временные метки

1. 45:50

### Velociraptor

1. intro : 54:12
