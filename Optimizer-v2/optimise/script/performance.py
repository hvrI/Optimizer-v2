#
#
# Performance - GameBar, Power, Paging, SVCHostSplit
# Fsutil Commands
# Additional Commands
#
#

performanceReg = {
    # Disable Paging Settings
    r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" : (
        ("DisablePagingExecutive", "Reg_DWORD", "1"),
        ("DisablePageCombining", "Reg_DWORD", "1"),
        ("LargeSystemCache", "Reg_DWORD", "1"),
    ),
    # Prioritize Foreground Applications
    r"HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" : (
        ("Win32PrioritySeparation", "Reg_DWORD", "38"),
        ("IRQ8Priority", "Reg_DWORD", "1"),
        ("IRQ16Priority", "Reg_DWORD", "2"),
    ),
    # Configure Automatic Maintenance
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Task Scheduler\Maintenance" : (
        ("WakeUp", "Reg_DWORD", "0"),
    ),
    # Configure the Multimedia Class Scheduler Service
    r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" : (
        ("SystemResponsiveness", "Reg_DWORD", "0"),
        ("NetworkThrottlingIndex", "Reg_DWORD", "4294967295"),
    ),
    # Disable Automatic Folder Discovery
    r"HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\Bags\AllFolders\Shell" : (
        ("FolderType", "Reg_SZ", "NotSpecified"),
    ),
    # Disable Background Apps
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" : (
        ("GlobalUserDisabled", "Reg_DWORD", "1"),
        ("LetAppsRunInBackground", "Reg_DWORD", "2"),
    ),
    r"HKLM\Software\Policies\Microsoft\Windows\AppPrivacy" : (
        ("LetAppsRunInBackground", "Reg_DWORD", "2"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" : (
        ("BackgroundAppGlobalToggle", "Reg_DWORD", "0"),
        # Set Display For Performance
        ("SearchboxTaskbarMode", "Reg_DWORD", "0"),
    ),
    # Disable Fault Tolerant Heap (FTH)
    r"HKLM\SOFTWARE\Microsoft\FTH" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    # Disable Game Bar & Full Screen Optimization Globally
    r"HKCU\System\GameConfigStore" : (
        ("GameDVR_Enabled", "Reg_DWORD", "0"),
        ("GameDVR_FSEBehavior", "Reg_DWORD", "2"),
        ("GameDVR_FSEBehaviorMode", "Reg_DWORD", "2"),
        ("GameDVR_HonorUserFSEBehaviorMode", "Reg_DWORD", "1"),
        ("GameDVR_DXGIHonorFSEWindowsCompatible", "Reg_DWORD", "1"),
        ("GameDVR_EFSEFeatureFlags", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR" : (
        ("AppCaptureEnabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\GameBar" : (
        ("GamePanelStartupTipIndex", "Reg_DWORD", "3"),
        ("ShowStartupPanel", "Reg_DWORD", "0"),
        ("UseNexusForGameBarEnabled", "Reg_DWORD", "0"),
        ("AllowAutoGameMode", "Reg_DWORD", "1"),
        ("AutoGameModeEnabled", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\WindowsRuntime\ActivatableClassId\Windows.Gaming.GameBar.PresenceServer.Internal.PresenceWriter" : (
        ("ActivationType", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\GameDVR" : (
        ("AllowGameDVR", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR" : (
        ("value", "Reg_DWORD", "0"),
    ),
    # Respect Power Modes Windows Search Indexing
    r"HKLM\Software\Microsoft\Windows Search\Gather\Windows\SystemIndex" : (
        ("RespectPowerModes", "Reg_DWORD", "1"),
        # Disable Variable Refresh Rate
        ("DirectXUserGlobalSettings", "Reg_SZ", "VRROptimizeEnable=0"),
    ),
    # Enable Hardware Accelerated GPU Scheduling (Windows 10 2004 + NVIDIA 10 Series Above + AMD 5000 and Above)
    r"HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" : (
        ("HwSchMode", "Reg_DWORD", "2"),
    ),
    # Disable Power Throttling
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling" : (
        ("PowerThrottlingOff", "Reg_DWORD", "1"),
    ),
    # MMCSS Tweaks (Games)
    r"HKCU\SOFTWARE\Microsoft\Games" : (
        ("FpsAll", "Reg_DWORD", "1"),
        ("GameFluidity", "Reg_DWORD", "1"),
        ("FpsStatusGames", "Reg_DWORD", "16"),
        ("FpsStatusGamesAll", "Reg_DWORD", "4")
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" : (
        ("Affinity", "Reg_DWORD", "0"),
        ("Background Only", "Reg_SZ", "False"),
        ("Clock Rate", "Reg_DWORD", "10000"),
        ("GPU Priority", "Reg_DWORD", "8"),
        ("Priority", "Reg_DWORD", "6"),
        ("Scheduling Category", "Reg_SZ", "High"),
        ("SFIO Priority", "Reg_SZ", "High"),
        ("Latency Sensitive", "Reg_SZ", "True"),
    ),
    # Disable Hibernation
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power" : (
        ("HibernateEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Power" : (
        ("HibernateEnabled", "Reg_DWORD", "0"),
        ("HiberbootEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FlyoutMenuSettings" : (
        ("ShowHibernateOption", "Reg_DWORD", "0"),
    ),
    # Set Display For Performance
    r"HKCU\Control Panel\Desktop" : (
        ("DragFullWindows", "Reg_SZ", "0"),
    ),
    r"HKCU\Control Panel\Keyboard" : (
        ("KeyboardDelay", "Reg_SZ", "0"),
    ),
    # Lower Latency
    r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Low Latency" : (
        ("Affinity", "Reg_DWORD", "0"),
        ("Background Only", "Reg_SZ", "False"),
        ("Clock Rate", "Reg_DWORD", "10000"),
        ("GPU Priority", "Reg_DWORD", "8"),
        ("Priority", "Reg_DWORD", "2"),
        ("Scheduling Category", "Reg_SZ", "High"),
        ("SFIO Priority", "Reg_SZ", "High"),
        ("Latency Sensitive", "Reg_SZ", "True"),
    ),
    # Disk Optimizations
    r"HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" : (
        ("DontVerifyRandomDrivers", "Reg_DWORD", "1"),
        ("NtfsMftZoneReservation", "Reg_DWORD", "1"),
        ("NtfsDisable8dot3NameCreation", "Reg_DWORD", "1"),
        ("NtfsDisableLastAccessUpdate", "Reg_DWORD", "1"),
        ("ContigFileAllocSize", "Reg_DWORD", "40")
    ),
    # Power Option Max Performance
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" : (
        ("ValueMax", "Reg_DWORD", "100"),
        ("ValueMin", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\ControlSet001\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" : (
        ("ValueMax", "Reg_DWORD", "100"),
        ("ValueMin", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\ControlSet002\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\0cc5b647-c1df-4637-891a-dec35c318583" : (
        ("ValueMax", "Reg_DWORD", "100"),
        ("ValueMin", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\893dee8e-2bef-41e0-89c6-b55d0929964c" : (
        ("ValueMax", "Reg_DWORD", "100"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\893dee8e-2bef-41e0-89c6-b55d0929964c\DefaultPowerSchemeValues\8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c" : (
        ("ValueMax", "Reg_DWORD", "100"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler" : (
        ("VsyncIdleTimeout", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Intel\GMM" : (
        ("DedicatedSegmentSize", "Reg_DWORD", "1024"),
    ),
    r"HKLM\SYSTEM\ControlSet001\Control\PriorityControl" : (
        ("Win32PrioritySeparation", "Reg_DWORD", "38"),
        ("IRQ8Priority", "Reg_DWORD", "1"),
        ("IRQ16Priority", "Reg_DWORD", "2"),
    ),
    r"HKLM\System\CurrentControlSet\Services\VxD\BIOS" : (
        ("CPUPriority", "Reg_DWORD", "1"),
        ("FastDRAM", "Reg_DWORD", "1"),
        ("PCIConcur", "Reg_DWORD", "1"),
        ("AGPConcur", "Reg_DWORD", "1"),
    ),
}

fsutilCMD = [
    # Disable last access information on directories, performance/privacy
    "fsutil behavior set disablelastaccess 1",
    # Disable the creation of 8.3 character-length file names on FAT- and NTFS-formatted volumes
    "fsutil behavior set disable8dot3 1",
    # Raised the limit of paged pool memory
    "fsutil behavior set memoryusage 2",
    # Disabled Virtual Memory Pagefile Encryption
    "fsutil behavior set encryptpagingfile 0",
    # Disabled NTFS compression
    "fsutil behavior set disablecompression 1",
    # Enabled Trim
    "fsutil behavior set disabledeletenotify 0",
]

ExtCommands = [
    # Disable Modern Standby SleepStudy
    r'wevtutil.exe set-log "Microsoft-Windows-SleepStudy/Diagnostic" /e:false',
    r'wevtutil.exe set-log "Microsoft-Windows-Kernel-Processor-Power/Diagnostic" /e:false',
    r'wevtutil.exe set-log "Microsoft-Windows-UserModePowerService/Diagnostic" /e:false',
    # Disable PowerShell Core telemetry
    r'setx POWERSHELL_TELEMETRY_OPTOUT 1',
    # Disable .NET CLI Telemetry
    r'setx DOTNET_CLI_TELEMETRY_OPTOUT 1',
    # Disable Dynamic Tick
    r'bcdedit /set disabledynamictick yes',
    # Disable High Precision Event Timer (HPET)
    r'bcdedit /deletevalue useplatformclock',
    # Disable Synthetic Timers
    r'bcdedit /set useplatformtick yes',
    # Lowering dual boot choice time
    r'bcdedit /timeout 10',
    # Use legacy boot menu
    r'bcdedit /set bootmenupolicy legacy',
    # Disable Hibernation
    r'powercfg.exe /hibernate off',
]
