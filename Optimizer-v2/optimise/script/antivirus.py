# Updated Version of Data Tweaks (Antivirus),
#
# SERVICES
# ENABLE - 1
# DISABLE - 0 or 4
#

AntivirusReg = {
    r"HKLM\SYSTEM\SYSTEM\CurrentControlSet\Services\wdboot" : (
        ("Start", "Reg_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\SYSTEM\CurrentControlSet\Services\wdfilter" : (
        ("Start", "Reg_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\SYSTEM\CurrentControlSet\Services\WinDefend" : (
        ("Start", "Reg_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\SYSTEM\CurrentControlSet\Services\SecurityHealthService" : (
        ("Start", "Reg_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\SYSTEM\CurrentControlSet\Services\wdnisdrv" : (
        ("Start", "Reg_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\SYSTEM\CurrentControlSet\Services\mssecflt" : (
        ("Start", "Reg_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\SYSTEM\CurrentControlSet\Services\WdNisSvc" : (
        ("Start", "Reg_DWORD", "4"),
    ),
    r"HKLM\SYSTEM\SYSTEM\CurrentControlSet\Services\Sense" : (
        ("Start", "Reg_DWORD", "4"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" : (
        ("DisableAntiSpyware", "Reg_DWORD", "1"),
        ("DisableAntiVirus", "Reg_DWORD", "1"),
        ("DisableRoutinelyTakingAction", "Reg_DWORD", "1"),
        ("ServiceKeepAlive", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" : (
        ("DisableBehaviorMonitoring", "Reg_DWORD", "1"),
        ("DisableIOAVProtection", "Reg_DWORD", "1"),
        ("DisableOnAccessProtection", "Reg_DWORD", "1"),
        ("DisableRealtimeMonitoring", "Reg_DWORD", "1"),
        ("DisableRoutinelyTakingAction", "Reg_DWORD", "1"),
        ("DisableScanOnRealtimeEnable", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Reporting" : (
        ("DisableEnhancedNotifications", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications" : (
        ("DisableNotifications", "Reg_DWORD", "1"),
    ),
    r"HKCU\Software\Policies\Microsoft\Windows\CurrentVersion\PushNotifications" : (
        ("NoToastApplicationNotification", "Reg_DWORD", "4"),
        ("NoToastApplicationNotificationOnLockScreen", "Reg_DWORD", "4"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\System" : (
        ("EnableSmartScreen", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Attachments" : (
        ("SaveZoneInformation", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Virus and threat protection" : (
        ("UILockdown", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\App and Browser protection" : (
        ("UILockdown", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer" : (
    ("SmartScreenEnabled", "Reg_SZ", "Off"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Edge" : (
        ("SmartScreenEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\MicrosoftEdge\PhishingFilter" : (
        ("EnabledV9", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Attachments" : (
        ("SaveZoneInformation", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Associations" : (
    ("ModRiskFileTypes", "Reg_SZ", ".bat;.exe;.reg;.vbs;.chm;.msi;.js;.cmd"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Family options" : (
        ("UILockdown", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Device performance and health" : (
        ("UILockdown", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Account protection" : (
        ("UILockdown", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" : (
        ("SpyNetReporting", "Reg_DWORD", "0"),
        ("SubmitSamplesConsent", "Reg_DWORD", "2"),
        ("DisableBlockAtFirstSeen", "Reg_DWORD", "1")
    ),
    r"HKLM\Software\Policies\Microsoft\Windows Defender\MpEngine" : (
        ("MpEnablePus", "Reg_DWORD", "0"),
    ),
    # Disable Tamper Protection
    r"HKLM\Software\Microsoft\Windows Defender\Features" : (
        ("TamperProtection", "Reg_DWORD", "0"),
    ),
    # Disable Logging
    r"HKLM\System\CurrentControlSet\Control\WMI\Autologger\DefenderApiLogger" : (
        ("Start", "Reg_DWORD", "0"),
    ),
    r"HKLM\System\CurrentControlSet\Control\WMI\Autologger\DefenderAuditLogger" : (
        ("Start", "Reg_DWORD", "0"),
    ),
}

AntivirusCMD = [
    r'schtasks /Change /TN "Microsoft\Windows\ExploitGuard\ExploitGuard MDM policy Refresh" /Disable',
    r'schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Cache Maintenance" /Disable',
    r'schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Cleanup" /Disable',
    r'schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Scheduled Scan" /Disable',
    r'schtasks /Change /TN "Microsoft\Windows\Windows Defender\Windows Defender Verification" /Disable',
]
