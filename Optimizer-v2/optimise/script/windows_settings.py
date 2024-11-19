#
#
#   Privacy - Advertising, Windows Privacy Settings, Cloud, Telementry
#   Qol - Appearance, Accessibility Settings, Ease of Access, Explorer, Shell, Startup Shutdown, Crash Control, Taskbar, Windows Update, 
#       - Mouse & Keyboard, 
#
#



privacyQolReg = {
    # Disable Advertising ID
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\Software\Policies\Microsoft\Windows\AdvertisingInfo" : (
        ("DisabledByGroupPolicy", "Reg_DWORD", "1"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" : (
        ("SubscribedContent-338393Enabled", "Reg_DWORD", "0"),
        ("SubscribedContent-353694Enabled", "Reg_DWORD", "0"),
        ("SubscribedContent-353696Enabled", "Reg_DWORD", "0"),
        ("SubscribedContent-310093Enabled", "Reg_DWORD", "0"),
        ("SubscribedContent-314559Enabled", "Reg_DWORD", "0"),
        ("SubscribedContent-338387Enabled", "Reg_DWORD", "0"),
        ("SubscribedContent-338388Enabled", "Reg_DWORD", "0"),
        ("SubscribedContent-338389Enabled", "Reg_DWORD", "0"),
        ("SubscribedContent-353698Enabled", "Reg_DWORD", "0"),
        ("SubscribedContent-88000326Enabled", "Reg_DWORD", "0"),
        # Telementry
        ("ContentDeliveryAllowed", "Reg_DWORD", "0"),
        ("OemPreInstalledAppsEnabled", "Reg_DWORD", "0"),
        ("PreInstalledAppsEnabled", "Reg_DWORD", "0"),
        ("PreInstalledAppsEverEnabled", "Reg_DWORD", "0"),
        ("SoftLandingEnabled", "Reg_DWORD", "0"),
        ("SilentInstalledAppsEnabled", "Reg_DWORD", "0"),
        ("SystemPaneSuggestionsEnabled", "Reg_DWORD", "0"),
        ("RotatingLockScreenOverlayEnabled", "Reg_DWORD", "0"),
    ),
    # Disable Show me suggestions for using my mobile device with Windows (Phone Link suggestions)
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Mobility" : (
        ("OptedIn", "Reg_DWORD", "0"),
    ),
    # Disable Sync Provider Notifications
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" : (
        ("ShowSyncProviderNotifications", "Reg_DWORD", "0"),
        # Disable App Launch Tracking
        ("Start_TrackProgs", "Reg_DWORD", "0"),
        # Disable Use Check Boxes to Select Items
        ("AutoCheckSelect", "Reg_DWORD", "0"),
        # Hide Recent Items
        ("Start_TrackDocs", "Reg_DWORD", "0"),
        # Disable Ballon Tips
        ("EnableBalloonTips", "Reg_DWORD", "0"),
        # Open File Explorer to This PC 
        ("LaunchTo", "Reg_DWORD", "1"),
        # Configure Explorer to Show All Files with File Extensions
        ("Hidden", "Reg_DWORD", "1"),
        ("HideFileExt", "Reg_DWORD", "0"),
        # Use Compact Mode
        ("UseCompactMode", "Reg_DWORD", "1"),
        # Do Not Show Edge Tabs in Alt-Tab
        ("MultiTaskingAltTabFilter", "Reg_DWORD", "3"),
        # Disable Aero Shake
        ("DisallowShaking", "Reg_DWORD", "1"),
        # Disable Recommendations in the Start Menu
        ("Start_IrisRecommendations", "Reg_DWORD", "0"),
        ("Start_AccountNotifications", "Reg_DWORD", "0"),
        # Disable Microsoft Copilot
        ("ShowCopilotButton", "Reg_DWORD", "0"),
        # Disable Show Desktop Peek on Taskbar
        ("DisablePreviewDesktop", "Reg_DWORD", "1"),
        # Disable Windows Chat
        ("TaskbarMn", "Reg_DWORD", "0"),
        ("TaskbarDa", "Reg_DWORD", "0"),
        # Disable Cortona Button
        ("ShowCortanaButton", "Reg_DWORD", "0"),
        # Disable Task View on Taskbar
        ("ShowTaskViewButton", "Reg_DWORD", "0"),
        # Set Taskbar to Align Left
        ("TaskbarAl", "Reg_DWORD", "0"),
        # Joint Resize 
        ("JointResize", "Reg_DWORD", "0"),
        # Snap
        ("SnapFill", "Reg_DWORD", "0"),
        ("SnapAssist", "Reg_DWORD", "0"),
        # Configure Visual Effects
        ("ListviewAlphaSelect", "Reg_DWORD", "0"),
        ("IconsOnly", "Reg_DWORD", "0"),
        ("TaskbarAnimations", "Reg_DWORD", "0"),
        ("ListviewShadow", "Reg_DWORD", "0"),
        ("TaskbarGlomLevel", "Reg_DWORD", "0"),
    ),
    # Disable Settings Sync
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\SettingSync" : (
        ("DisableSettingSync", "Reg_DWORD", "2"),
        ("DisableSettingSyncUserOverride", "Reg_DWORD", "1"),
        ("DisableSyncOnPaidNetwork", "Reg_DWORD", "1"),
        ("DisableWindowsSettingSync", "Reg_DWORD", "2"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Personalization" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\BrowserSettings" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Credentials" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Language" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Accessibility" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync\Groups\Windows" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SettingSync" : (
        ("SyncPolicy", "Reg_DWORD", "5"),
    ),
    # Personalization Tab ( Disable Transparency )
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" : (
        ("EnableTransparency", "Reg_DWORD", "0"),
    ),
    # Disable Suggested Ways to Finish Setting Up Your Device
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\UserProfileEngagement" : (
        ("ScoobeSystemSettingEnabled", "Reg_DWORD", "0"),
    ),
    # Disallow Message Service Cloud Sync
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Messaging" : (
        ("AllowMessageSync", "Reg_DWORD", "0"),
    ),
    # Disable Biometric
    r"HKLM\SOFTWARE\Policies\Microsoft\Biometrics" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    # Configure App Permissions
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appDiagnostics" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    # Location
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\location" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userAccountInformation" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    # Notification
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userNotificationListener" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings" : (
        ("NOC_GLOBAL_SETTING_ALLOW_NOTIFICATION_SOUND", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PushNotifications" : (
        ("ToastEnabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\PushNotifications" : (
        ("ToastEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\PushNotifications" : (
        ("NoCloudApplicationNotification", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Explorer" : (
        ("DisableNotificationCenter", "Reg_DWORD", "1"),
        # Configure Start Menu
        ("ShowOrHideMostUsedApps", "Reg_DWORD", "2"),
        ("HideRecentlyAddedApps", "Reg_DWORD", "1"),
        ("HideRecommendedPersonalizedSites", "Reg_DWORD", "1"),
        # Disable Cortana in Search
        ("AllowCortana", "Reg_DWORD", "0"),
        ("CortanaConsent", "Reg_DWORD", "0"),
    ),
    r"HKCU\Software\Policies\Microsoft\Windows\Explorer" : (
        ("DisableNotificationCenter", "Reg_DWORD", "1"),
        # Blocks Anonymous Enumeration of SAM Accounts
        ("DisableSearchBoxSuggestions", "Reg_DWORD", "1"),
        # Hide Recent Items
        ("NoRemoteDestinations", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\activity" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\appointments" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\bluetoothSync" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\cellularData" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\chat" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\contacts" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\email" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\gazeInput" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\musicLibrary" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCall" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\phoneCallHistory" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\radios" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\userDataTasks" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeviceAccess\Global\LooselyCoupled" : (
        ("Value", "Reg_SZ", "Deny"),
    ),
    # Disable AppPrivacy
    #r"HKLM\SOFTWARE\Policies\Microsoft\Windows\AppPrivacy" : (
    #    ("LetAppsAccessAccountInfo", "Reg_DWORD", "2"),
    #    ("LetAppsAccessBackgroundSpatialPerception", "Reg_DWORD", "2"),
    #    ("LetAppsAccessCalendar", "Reg_DWORD", "2"),
    #    ("LetAppsAccessCallHistory", "Reg_DWORD", "2"),
    #    ("LetAppsAccessContacts", "Reg_DWORD", "2"),
    #    ("LetAppsAccessEmail", "Reg_DWORD", "2"),
    #    ("LetAppsAccessGazeInput", "Reg_DWORD", "2"),
    #    ("LetAppsAccessLocation", "Reg_DWORD", "2"),
    #    ("LetAppsAccessMessaging", "Reg_DWORD", "2"),
    #    ("LetAppsAccessMotion", "Reg_DWORD", "2"),
    #    ("LetAppsAccessNotifications", "Reg_DWORD", "2"),
    #    ("LetAppsAccessPhone", "Reg_DWORD", "2"),
    #    ("LetAppsAccessRadios", "Reg_DWORD", "2"),
    #    ("LetAppsAccessTasks", "Reg_DWORD", "2"),
    #    ("LetAppsAccessTrustedDevices", "Reg_DWORD", "2"),
    #    ("LetAppsActivateWithVoice", "Reg_DWORD", "2"),
    #    ("LetAppsActivateWithVoiceAboveLock", "Reg_DWORD", "2"),
    #    ("LetAppsGetDiagnosticInfo", "Reg_DWORD", "2"),
    #    ("LetAppsSyncWithDevices", "Reg_DWORD", "2"),
    #),
    # Configure Windows Media Player
    r"HKLM\SOFTWARE\Policies\Microsoft\WMDRM" : (
        ("DisableOnline", "Reg_DWORD", "1"),
    ),
    r"HKCU\SOFTWARE\Microsoft\MediaPlayer\Preferences" : (
        ("AcceptedPrivacyStatement", "Reg_DWORD", "1"),
        ("UsageTracking", "Reg_DWORD", "0"),
    ),
    # Disable Activity Feed
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\System" : (
        ("EnableActivityFeed", "Reg_DWORD", "0"),
        # Disable Resultant Set of Policy (RSoP) Logging
        ("RSoPLogging", "Reg_DWORD", "0"),
        # Disallow Upload and Publish of User Activities
        ("UploadUserActivities", "Reg_DWORD", "0"),
        ("PublishUserActivities", "Reg_DWORD", "0"),
    ),
    # Disable Device Health Attestation Monitoring and Reporting
    r"HKLM\SOFTWARE\Policies\Microsoft\DeviceHealthAttestationService" : (
        ("EnableDeviceHealthAttestationService", "Reg_DWORD", "0"),
    ),
    # Disable Experimentation
    r"HKLM\SOFTWARE\Microsoft\PolicyManager\default\System\AllowExperimentation" : (
        ("value", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\PolicyManager\current\device\System" : (
        ("AllowExperimentation", "Reg_DWORD", "0"),
    ),
    # Disable People
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\People" : (
        ("PeopleBand", "Reg_DWORD", "0"),
    ),
    # Disable UserAssist
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\settings" : (
        ("NoLog", "Reg_DWORD", "1"),
    ),
    # Disable Prefetch
    r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters" : (
        ("EnablePrefetcher", "Reg_DWORD", "0"),
        ("EnableSuperfetch", "Reg_DWORD", "0"),
        ("EnableBoottrace", "Reg_DWORD", "0")
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32" : (
        ("NoFileMru", "Reg_DWORD", "1"),
    ),
    # Disable Lockscreen Camera
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Personalization" : (
        ("NoLockScreenCamera", "Reg_DWORD", "1"),
    ),
    # Disable Online Speech Recognition
    r"HKCU\SOFTWARE\Microsoft\Speech_OneCore\Settings\OnlineSpeechPrivacy" : (
        ("HasAccepted", "Reg_DWORD", "0"),
    ),
    # Disable ConsumerFeatures
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\CloudContent" : (
        ("DisableWindowsConsumerFeatures", "Reg_DWORD", "1"),
        # Disable Cloud Optimized Content on Taskbar
        ("DisableCloudOptimizedContent", "Reg_DWORD", "1"),
        # Disable Tips
        ("DisableSoftLanding", "Reg_DWORD", "1"),
    ),
    # Disable Program Compatibility Assistant (PCA)
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\AppCompat" : (
        ("AITEnable", "Reg_DWORD", "0"),
        ("AllowTelemetry", "Reg_DWORD", "0"),
        ("DisableEngine", "Reg_DWORD", "1"),
        ("DisableInventory", "Reg_DWORD", "1"),
        ("DisablePCA", "Reg_DWORD", "1"),
        ("DisableUAR", "Reg_DWORD", "1"),
    ),
    # Disable Performance Track
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WDI\{9c5a40da-b965-4fc3-8781-88dd50a6299d}" : (
        ("ScenarioExecutionEnabled", "Reg_DWORD", "0"),
    ),
    # Disable OOBE Privacy Experience
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\OOBE" : (
        ("DisablePrivacyExperience", "Reg_DWORD", "1"),
    ),
    # Disable Automatic Updates Of Speech Data
    r"HKLM\SOFTWARE\Policies\Microsoft\Speech" : (
        ("AllowSpeechModelUpdate", "Reg_DWORD", "0"),
    ),
    # Do Not Use Diagnostic Data For Tailored Experiences
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Privacy" : (
        ("TailoredExperiencesWithDiagnosticDataEnabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Policies\Microsoft\Windows\CloudContent" : (
        ("DisableTailoredExperiencesWithDiagnosticData", "Reg_DWORD", "1"),
        # Disable Windows Spotlight
        ("DisableWindowsSpotlightFeatures", "Reg_DWORD", "1"),
        ("DisableWindowsSpotlightWindowsWelcomeExperience", "Reg_DWORD", "1"),
        ("DisableWindowsSpotlightOnActionCenter", "Reg_DWORD", "1"),
        ("DisableWindowsSpotlightOnSettings", "Reg_DWORD", "1"),
        ("DisableThirdPartySuggestions", "Reg_DWORD", "1"),
    ),
    # Disable Most Frequently Used Applications
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" : (
        ("NoInstrumentation", "Reg_DWORD", "1"),
        # Disable Searching for Invalid Shortcuts
        ("NoResolveSearch", "Reg_DWORD", "1"),
        ("NoResolveTrack", "Reg_DWORD", "1"),
        # Hide Recent Items
        ("ClearRecentDocsOnExit", "Reg_DWORD", "1"),
        ("NoRecentDocsHistory", "Reg_DWORD", "1"),
        # Better Explorer
        ("NoRun", "Reg_DWORD", "0"),
        ("NoControlPanel", "Reg_DWORD", "0"),
        ("NoFolderOptions", "Reg_DWORD", "0"),
        ("NoViewContextMenu", "Reg_DWORD", "0"),
        ("NoInternetOpenWith", "Reg_DWORD", "1"),
        ("LinkResolveIgnoreLinkInfo", "Reg_DWORD", "1"),
        # Diasble Low Disk Space Checks
        ("NoLowDiskSpaceChecks", "Reg_DWORD", "1"),
    ),
    # Disable Website Access to Language List
    r"HKCU\Control Panel\International\User Profile" : (
        ("HttpAcceptLanguageOptOut", "Reg_DWORD", "1"),
    ),
    # Disable Windows Error Reporting
    r"HKCU\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting" : (
        ("Disabled", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\PCHealth\ErrorReporting" : (
        ("DoReport", "Reg_DWORD", "0"),
        ("ShowUI", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\Windows Error Reporting" : (
        ("Disabled", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Error Reporting" : (
        ("Disabled", "Reg_DWORD", "1"),
        ("DontShowUI", "Reg_DWORD", "1"),
        ("LoggingDisabled", "Reg_DWORD", "1"),
        ("DontSendAdditionalData", "Reg_DWORD", "1"),
    ),
    r"HKLM\Software\Microsoft\Windows\CurrentVersion\Component Based Servicing" : (
        ("DisableWerReporting", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\DeviceInstall\Settings" : (
        ("DisableSendGenericDriverNotFoundToWER", "Reg_DWORD", "1"),
        ("DisableSendRequestAdditionalSoftwareToWER", "Reg_DWORD", "1"),
    ),
    # Disallow Users to Be Non-local
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" : (
        ("NoConnectedUser", "Reg_DWORD", "1"),
        # Disable UAC Secure Desktop
        ("PromptOnSecureDesktop", "Reg_DWORD", "0"),
    ),
    # Configure Search on the Taskbar
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" : (
        ("SearchboxTaskbarMode", "Reg_DWORD", "0"),
        ("BingSearchEnabled", "Reg_DWORD", "0"),
        ("AllowSearchToUseLocation", "Reg_DWORD", "0"),
        ("CortanaConsent", "Reg_DWORD", "0"),
        ("DeviceHistoryEnabled", "Reg_DWORD", "0"),
        ("HistoryViewEnabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\SearchSettings" : (
        ("IsAADCloudSearchEnabled", "Reg_DWORD", "0"),
        ("IsDeviceSearchHistoryEnabled", "Reg_DWORD", "0"),
        ("IsMSACloudSearchEnabled", "Reg_DWORD", "0"),
        ("SafeSearchMode", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" : (
        ("ConnectedSearchUseWeb", "Reg_DWORD", "0"),
        ("DisableWebSearch", "Reg_DWORD", "1"),
        ("AllowCloudSearch", "Reg_DWORD", "0"),
        ("AllowCortana", "Reg_DWORD", "0"),
        ("AllowSearchToUseLocation", "Reg_DWORD", "0"),
        ("EnableDynamicContentInWSB", "Reg_DWORD", "0"),
    ),
    # Disable Remote Assistance
    r"HKLM\SYSTEM\CurrentControlSet\Control\Lsa" : (
        ("restrictanonymoussam", "Reg_DWORD", "1"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Remote Assistance" : (
        ("fAllowFullControl", "Reg_DWORD", "0"),
        ("fAllowToGetHelp", "Reg_DWORD", "0"),
    ),
    # Disable Recall
    r"HKCU\SOFTWARE\Policies\Microsoft\Windows\WindowsAI" : (
        ("DisableAIDataAnalysis", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsAI" : (
        ("DisableAIDataAnalysis", "Reg_DWORD", "1"),
    ),

    # Telementry

    # Disable NVIDIA Control Panel Telemetry
    r"HKCU\Software\NVIDIA Corporation\NVControlPanel2\Client" : (
        ("OptInOrOutPreference", "Reg_DWORD", "0"),
    ),
    # Disable Office Telemetry
    r"HKCU\Software\Policies\Microsoft\office\16.0\common" : (
        ("sendcustomerdata", "Reg_DWORD", "0"),
        ("QMEnable", "Reg_DWORD", "0"),
    ),
    r"HKCU\Software\Policies\Microsoft\office\common\clienttelemetry" : (
        ("SendTelemetry", "Reg_DWORD", "3"),
    ),
    # Disable Key Management System Telemetry
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows NT\CurrentVersion\Software Protection Platform" : (
        ("NoGenTicket", "Reg_DWORD", "1"),
    ),
    # Disable Customer Experience Improvement Program
    r"HKLM\SOFTWARE\Policies\Microsoft\AppV\CEIP" : (
        ("CEIPEnable", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\SQMClient\Windows" : (
        ("CEIPEnable", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\SQMClient\Windows" : (
        ("CEIPEnable", "Reg_DWORD", "0"),
    ),
    # Disable Diagnostic Tracing
    r"HKLM\SYSTEM\CurrentControlSet\Control\Diagnostics\Performance" : (
        ("DisableDiagnosticTracing", "Reg_DWORD", "1"),
    ),
    # Disable Location Tracking
    r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Sensor\Overrides\{BFA794E4-F964-4FDB-90F6-51056BFE4B44}" : (
        ("SensorPermissionState", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\lfsvc\Service\Configuration" : (
        ("Status", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\Maps" : (
        ("AutoUpdateEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors" : (
        ("DisableWindowsLocationProvider", "Reg_DWORD", "1"),
        ("DisableLocationScripting", "Reg_DWORD", "1")
    ),
    # Disable Input Telemetry
    r"HKLM\SOFTWARE\Microsoft\Speech_OneCore\Preferences" : (
        ("ModelDownloadAllowed", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\InputPersonalization" : (
        ("RestrictImplicitInkCollection", "Reg_DWORD", "1"),
        ("RestrictImplicitTextCollection", "Reg_DWORD", "1"),
    ),
    r"HKCU\SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore" : (
        ("HarvestContacts", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Personalization\Settings" : (
        ("AcceptedPrivacyPolicy", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\TabletPC" : (
        ("PreventHandwritingDataSharing", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\HandwritingErrorReports" : (
        ("PreventHandwritingErrorReports", "Reg_DWORD", "1"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Input\Settings" : (
        ("InsightsEnabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Input\TIPC" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Input\TIPC" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Device Metadata" : (
        ("PreventDeviceMetadataFromNetwork", "Reg_DWORD", "1"),
    ),
    # Disallow Telemetry and Data Collection
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack" : (
        ("ShowedToastAtLevel", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection" : (
        ("AllowTelemetry", "Reg_DWORD", "0"),
        ("MaxTelemetryAllowed", "Reg_DWORD", "0"),
        # Disable Windows Feedback
        ("DoNotShowFeedbackNotifications", "Reg_DWORD", "1"),
    ),
    r"HKLM\Software\Policies\Microsoft\Windows\DataCollection" : (
        ("AllowTelemetry", "Reg_DWORD", "0"),
        ("AllowDeviceNameInTelemetry", "Reg_DWORD", "0"),
        ("DisableOneSettingsDownloads", "Reg_DWORD", "1"),
        ("LimitDiagnosticLogCollection", "Reg_DWORD", "1"),
        ("DisableTelemetryOptInChangeNotification", "Reg_DWORD", "1"),
        ("AllowWUfBCloudProcessing", "Reg_DWORD", "0"),
        ("AllowDesktopAnalyticsProcessing", "Reg_DWORD", "0"),
        # Disable Windows Feedback
        ("DoNotShowFeedbackNotifications", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\DataCollection" : (
        ("AllowTelemetry", "Reg_DWORD", "0"),
    ),
    r"HKLM\Software\Microsoft\Windows\CurrentVersion\Diagnostics\DiagTrack\EventTranscriptKey" : (
        ("EnableEventTranscript", "Reg_DWORD", "0"),
        ("MiniTraceSlotEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\Diagtrack-Listener" : (
        ("Start", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\WMI\AutoLogger\AutoLogger-Diagtrack-Listener" : (
        ("Start", "Reg_DWORD", "0"),
    ),
    # Disable MSRT telemetry
    r"HKLM\SOFTWARE\Policies\Microsoft\MRT" : (
        ("DontReportInfectionInformation", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\RemovalTools\MpGears" : (
        ("HeartbeatTrackingIndex", "Reg_DWORD", "0"),
        ("SpyNetReportingLocation", "Reg_MULTI_SZ", " "),
    ),
    # Disable Office Telementry
    r"HKCU\Software\Policies\microsoft\office\16.0\osm\preventedapplications" : (
        ("accesssolution", "Reg_DWORD", "1"),
        ("olksolution", "Reg_DWORD", "1"),
        ("onenotesolution", "Reg_DWORD", "1"),
        ("pptsolution", "Reg_DWORD", "1"),
        ("projectsolution", "Reg_DWORD", "1"),
        ("publishersolution", "Reg_DWORD", "1"),
        ("visiosolution", "Reg_DWORD", "1"),
        ("wdsolution", "Reg_DWORD", "1"),
        ("xlsolution", "Reg_DWORD", "1"),
    ),
    r"HKCU\Software\Policies\microsoft\office\16.0\osm\preventedsolutiontypes" : (
        ("agave", "Reg_DWORD", "1"),
        ("appaddins", "Reg_DWORD", "1"),
        ("comaddins", "Reg_DWORD", "1"),
        ("documentfiles", "Reg_DWORD", "1"),
        ("templatefiles", "Reg_DWORD", "1"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\15.0\Outlook\Options\Mail" : (
        ("EnableLogging", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\16.0\Outlook\Options\Mail" : (
        ("EnableLogging", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\15.0\Outlook\Options\Calendar" : (
        ("EnableCalendarLogging", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\16.0\Outlook\Options\Calendar" : (
        ("EnableCalendarLogging", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\15.0\Word\Options" : (
        ("EnableLogging", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\16.0\Word\Options" : (
        ("EnableLogging", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Policies\Microsoft\Office\15.0\OSM" : (
        ("EnableLogging", "Reg_DWORD", "0"),
        ("EnableUpload", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Policies\Microsoft\Office\16.0\OSM" : (
        ("EnableLogging", "Reg_DWORD", "0"),
        ("EnableUpload", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\Common\ClientTelemetry" : (
        ("DisableTelemetry", "Reg_DWORD", "1"),
        ("VerboseLogging", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\16.0\Common\ClientTelemetry" : (
        ("DisableTelemetry", "Reg_DWORD", "1"),
        ("VerboseLogging", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\15.0\Common" : (
        ("QMEnable", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\16.0\Common" : (
        ("QMEnable", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\15.0\Common\Feedback" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Office\16.0\Common\Feedback" : (
        ("Enabled", "Reg_DWORD", "0"),
    ),
    # Disable 'Always Read and Scan This Section'
    r"HKCU\SOFTWARE\Microsoft\Ease of Access" : (
        ("selfscan", "Reg_DWORD", "0"),
        ("selfvoice", "Reg_DWORD", "0"),
    ),
    # Disable Commonly Annoying Features and Shortcuts
    r"HKCU\Control Panel\Accessibility\HighContrast" : (
        ("Flags", "Reg_DWORD", "0"),
    ),
    r"HKCU\Control Panel\Accessibility\Keyboard Response" : (
        ("Flags", "Reg_DWORD", "0"),
    ),
    r"HKCU\Control Panel\Accessibility\MouseKeys" : (
        ("Flags", "Reg_DWORD", "0"),
    ),
    r"HKCU\Control Panel\Accessibility\StickyKeys" : (
        ("Flags", "Reg_DWORD", "0"),
    ),
    r"HKCU\Control Panel\Accessibility\ToggleKeys" : (
        ("Flags", "Reg_DWORD", "0"),
    ),
    # Disable Narrator shortcut
    r"HKCU\Software\Microsoft\Narrator\NoRoam" : (
        ("WinEnterLaunchEnabled", "Reg_DWORD", "0"),
    ),
    # Disable Accessibility Tool Shortcut
    r"HKCU\Control Panel\Accessibility\SlateLaunch" : (
        ("LaunchAT", "Reg_DWORD", "0"),
    ),
    # Disable Ease of Access Sounds & Dynamic Scrollbars
    r"HKCU\Control Panel\Accessibility" : (
        ("Warning Sounds", "Reg_DWORD", "0"),
        ("Sound on Activation", "Reg_DWORD", "0"),
        ("DynamicScrollbars", "Reg_DWORD", "0"),
    ),
    r"HKCU\Control Panel\Accessibility\SoundSentry" : (
        ("WindowsEffect", "Reg_SZ", "0"),
    ),
    # Remove 'Cast to device' from Context Menu
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Shell Extensions\Blocked" : (
        ("{7AD84985-87B4-4a16-BE58-8B72A5B390F7}", "Reg_SZ", " "),
        # Remove 'Troubleshooting Compatibility' from Context Menu
        ("{1d27f844-3a1f-4410-85ac-14651078412d}", "Reg_SZ", " "),
    ),
    r"HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Shell Extensions\Blocked" : (
        ("{1d27f844-3a1f-4410-85ac-14651078412d}", "Reg_SZ", " "),
    ),
    # Show More Details by Default on Transfers
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\OperationStatusManager" : (
        ("EnthusiastMode", "Reg_DWORD", "1"),
    ),
    # Revert to Classic Search
    r"HKLM\SOFTWARE\Classes\CLSID\{1d64637d-31e9-4b06-9124-e83fb178ac6e}\TreatAs" : (
        (" ", "Reg_SZ", "{64bc32b5-4eec-4de7-972d-bd8bd0324537}"),
    ),
    r"HKLM\SOFTWARE\Classes\WOW6432Node\CLSID\{1d64637d-31e9-4b06-9124-e83fb178ac6e}\TreatAs" : (
        (" ", "Reg_SZ", "{64bc32b5-4eec-4de7-972d-bd8bd0324537}"),
    ),
    r"HKLM\SOFTWARE\WOW6432Node\Classes\CLSID\{1d64637d-31e9-4b06-9124-e83fb178ac6e}\TreatAs" : (
        (" ", "Reg_SZ", "{64bc32b5-4eec-4de7-972d-bd8bd0324537}"),
    ),
    # Hide Folders from This PC
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{31C0DD25-9439-4F12-BF41-7FF4EDA38722}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{31C0DD25-9439-4F12-BF41-7FF4EDA38722}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{a0c69a99-21c8-4671-8703-7934162fcf1d}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{a0c69a99-21c8-4671-8703-7934162fcf1d}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{7d83ee9b-2244-4e70-b1f5-5393042af1e4}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{7d83ee9b-2244-4e70-b1f5-5393042af1e4}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{0ddd015d-b06c-45d5-8c4c-f59713854639}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{0ddd015d-b06c-45d5-8c4c-f59713854639}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{35286a68-3c57-41a1-bbb1-0eae73d76c95}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{35286a68-3c57-41a1-bbb1-0eae73d76c95}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{f42ee2d3-909f-4907-8871-4c22fc0bf756}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{f42ee2d3-909f-4907-8871-4c22fc0bf756}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}\PropertyBag" : (
        ("ThisPCPolicy", "Reg_SZ", "Hide"),
    ),
    # Don't Show Office Files
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer" : (
        ("ShowCloudFilesInQuickAccess", "Reg_DWORD", "0"),
        # Always Show the Full Context Menu On Items
        ("MultipleInvokePromptMinimum", "Reg_DWORD", "100"),
        # Hide Recent Items
        ("ShowFrequent", "Reg_DWORD", "0"),
        ("ShowRecent", "Reg_DWORD", "0"),
        # Disable Search Box Suggestion
        ("DisableSearchBoxSuggestions", "Reg_DWORD", "1"),
    ),
    # Enable Long Paths
    r"HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" : (
        ("LongPathsEnabled", "Reg_DWORD", "1"),
    ),
    # Extend Icon Cache & Unload .dll
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer" : (
        ("Max Cached Icons", "Reg_SZ", "4096"),
        ("AlwaysUnloadDLL", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\AlwaysUnloadDLL" : (
        ("Default", "Reg_DWORD", "1"),
    ),
    # Minimize Mouse Hover Time for Item Info
    r"HKCU\Control Panel\Desktop" : (
        ("MouseHoverTime", "Reg_SZ", "20"),
        # Disable Menu Hover Delay
        ("MenuShowDelay", "Reg_SZ", "0"),
        # Decrease Shutdown Time
        ("HungAppTimeout", "Reg_SZ", "1000"),
        ("WaitToKillAppTimeout", "Reg_SZ", "2000"),
        ("LowLevelHooksTimeout", "Reg_SZ", "1000"),
        ("WaitToKillServiceTimeout", "Reg_SZ", "1000"),
        ("ForegroundLockTimeout", "Reg_SZ", "150000"),
        # Force Close Applications On Session End
        ("AutoEndTasks", "Reg_SZ", "1"),
        # Disable Wallpaper Compression
        ("JPEGImportQuality", "Reg_DWORD", "100"),
    ),
    # Disable Internet File Assocation Service
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" : (
        ("NoInternetOpenWith", "Reg_DWORD", "1"),
        # Hide 'Meet Now' on Taskbar
        ("HideSCAMeetNow", "Reg_DWORD", "1"),
        # Configure Start Menu
        ("NoStartMenuMFUprogramsList", "Reg_DWORD", "1"),
        # Disable Settings Tips
        ("AllowOnlineTips", "Reg_DWORD", "0"),
        # Hides Settings pages that are either broken or unused
        ("SettingsPageVisibility", "Reg_SZ", "hide:recovery;maps;maps-downloadmaps;privacy;privacy-feedback;privacy-activityhistory;search-permissions;privacy-general;sync;mobile-devices;mobile-devices-addphone;workplace;family-group;deviceusage;home"),
    ),
    # Driver Searching
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching" : (
        ("SearchOrderConfig", "Reg_DWORD", "1"),
    ),
    # Remove Shortcut Text
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\NamingTemplates" : (
        ("ShortcutNameTemplate", "Reg_SZ", r'"%s.lnk"'),
    ),
    # Disable AutoRun
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers" : (
        ("DisableAutoplay", "Reg_DWORD", "1"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers\EventHandlersDefaultSelection\CameraAlternate" : (
        ("MSTakeNoAction", "Reg_NONE", None),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers\EventHandlersDefaultSelection\StorageOnArrival" : (
        ("MSTakeNoAction", "Reg_NONE", None),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers\UserChosenExecuteHandlers\CameraAlternate\ShowPicturesOnArrival" : (
        ("MSTakeNoAction", "Reg_NONE", None),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers\UserChosenExecuteHandlers\StorageOnArrival" : (
        ("MSTakeNoAction", "Reg_NONE", None),
    ),
    # Disable Shared Experiences
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\CDP\SettingsPage" : (
        ("BluetoothLastDisabledNearShare", "Reg_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\CDP" : (
        ("NearShareChannelUserAuthzPolicy", "Reg_DWORD", "0"),
        ("CdpSessionUserAuthzPolicy", "Reg_DWORD", "1"),
    ),
    # Set Unpinned Control Center Items
    r"HKCU\Control Panel\Quick Actions\Control Center\Unpinned" : (
        ("Microsoft.QuickAction.Cast", "Reg_NONE", None),
        ("Microsoft.QuickAction.NearShare", "Reg_NONE", None),
        ("Microsoft.QuickAction.ColorProfile", "Reg_NONE", None),
        ("Microsoft.QuickAction.ProjectL2", "Reg_NONE", None),
        
    ),
    r"HKCU\Control Panel\Quick Actions\Control Center\QuickActionsStateCapture" : (
        ("Toggles", "Reg_SZ", "Toggles,Microsoft.QuickAction.BlueLightReduction:false,Microsoft.QuickAction.Accessibility:false,Microsoft.QuickAction.ProjectL2:false"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control" : (
        ("WaitToKillServiceTimeout", "Reg_SZ", "1000"),
    ),
    # Disable Startup Delay
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Serialize" : (
        ("StartupDelayInMSec", "Reg_DWORD", "0"),
    ),
    # Clear Page File at Shutdown
    r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" : (
        ("ClearPageFileAtShutdown", "Reg_DWORD", "0"),
    ),
    # Configure Crash Control
    r"HKLM\SYSTEM\CurrentControlSet\Control\CrashControl" : (
        ("AutoReboot", "Reg_DWORD", "0"),
        ("CrashDumpEnabled", "Reg_DWORD", "0"),
        ("LogEvent", "Reg_DWORD", "0"),
        ("DisplayParameters", "Reg_DWORD", "1"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\CrashControl\StorageTelemetry" : (
        ("DeviceDumpEnabled", "Reg_DWORD", "0"),
    ),
    # Disable Windows Platform Binary Table Execution (WPBT)
    r"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager" : (
        ("DisableWpbtExecution", "Reg_DWORD", "1"),
    ),
    # Disable Microsoft Copilot
    r"HKLM\Software\Policies\Microsoft\Windows\WindowsCopilot" : (
        ("TurnOffWindowsCopilot", "Reg_DWORD", "1"),
    ),
    r"HKCU\Software\Policies\Microsoft\Windows\WindowsCopilot" : (
        ("TurnOffWindowsCopilot", "Reg_DWORD", "1"),
    ),
    # Disable News and Interests
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Feeds" : (
        ("EnableFeeds", "Reg_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Feeds" : (
        ("ShellFeedsTaskbarViewMode", "Reg_DWORD", "2"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Dsh" : (
        ("AllowNewsAndInterests", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\PolicyManager\default\NewsAndInterests\AllowNewsAndInterests" : (
        ("value", "Reg_DWORD", "0"),
    ),
    
    # Never Use Tablet Mode
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ImmersiveShell" : (
        ("SignInMode", "Reg_DWORD", "1"),
        ("TabletMode", "Reg_DWORD", "0"),
    ),
    # Disable Windows Chat
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Chat" : (
        ("ChatIcon", "Reg_DWORD", "3"),
    ),
    # Add 'End task' to the taskbar
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\TaskbarDeveloperSettings" : (
        ("TaskbarEndTask", "Reg_DWORD", "1"),
    ),
    # Disable Delivery Optimization
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization" : (
        ("DODownloadMode", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config" : (
        ("DODownloadMode", "Reg_DWORD", "0"),
    ),
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\DeliveryOptimization" : (
        ("SystemSettingsDownloadMode", "Reg_DWORD", "0"),
    ),
    # Disable Feature Updates
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" : (
        ("TargetReleaseVersion", "Reg_DWORD", "1"),
        # Restrict Windows Insider
        ("ManagePreviewBuilds", "Reg_DWORD", "1"),
        ("ManagePreviewBuildsPolicyValue", "Reg_DWORD", "0"),
        # Windows Update
        ("DeferUpgrade", "Reg_DWORD", "1"),
        ("DeferUpgradePeriod", "Reg_DWORD", "1"),
        ("DeferUpdatePeriod", "Reg_DWORD", "0")
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\PreviewBuilds" : (
        ("AllowBuildPreview", "Reg_DWORD", "0"),
        ("EnableConfigFlighting", "Reg_DWORD", "0"),
        ("EnableExperimentation", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Microsoft\WindowsSelfHost\UI\Visibility" : (
        ("HideInsiderPage", "Reg_DWORD", "1"),
    ),
    # Disable WU Nagging
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" : (
        ("NoAUAsDefaultShutdownOption", "Reg_DWORD", "1"),
        ("NoAutoUpdate", "Reg_DWORD", "1"),
    ),
    r"HKLM\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings" : (
        ("HideMCTLink", "Reg_DWORD", "1"),
    ),
    # Configure PowerShell
    r"HKLM\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell" : (
        ("ExecutionPolicy", "Reg_SZ", "Unrestricted"),
    ),
    # Disable Dynamic Lighting
    r"HKCU\Software\Microsoft\Lighting" : (
        ("AmbientLightingEnabled", "Reg_DWORD", "0"),
    ),
    # Disable Mouse Acceleration
    r"HKCU\Control Panel\Mouse" : (
        ("MouseSensitivity", "Reg_SZ", "10"),
        ("MouseSpeed", "Reg_SZ", "0"),
        ("MouseThreshold1", "Reg_SZ", "0"),
        ("MouseThreshold2", "Reg_SZ", "0"),
    ),
    r"HKU\.DEFAULT\Control Panel\Mouse" : (
        ("MouseSensitivity", "Reg_SZ", "10"),
        ("MouseSpeed", "Reg_SZ", "0"),
        ("MouseThreshold1", "Reg_SZ", "0"),
        ("MouseThreshold2", "Reg_SZ", "0"),
    ),
    # Disable Settings Tips
    r"HKLM\SOFTWARE\Microsoft\PolicyManager\default\Settings\AllowOnlineTips" : (
        ("value", "Reg_DWORD", "0"),
    ),
    # Disable Spell Checking
    r"HKCU\SOFTWARE\Microsoft\TabletTip\1.7" : (
        ("EnableAutocorrection", "Reg_DWORD", "0"),
        ("EnableDoubleTapSpace", "Reg_DWORD", "0"),
        ("EnablePredictionSpaceInsertion", "Reg_DWORD", "0"),
        ("EnableSpellchecking", "Reg_DWORD", "0"),
        ("EnableTextPrediction", "Reg_DWORD", "0"),
        # Disable Unnecessary Touch Keyboard Settings
        ("EnableAutoShiftEngage", "Reg_DWORD", "0"),
        ("EnableKeyAudioFeedback", "Reg_DWORD", "0"),
    ),
    # Disable Automatic Updates for Apps in Store
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsStore\WindowsUpdate" : (
        ("AutoDownload", "Reg_DWORD", "2"),
    ),
    # Disable Auto Maintenance
    r"HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\Maintenance" : (
        ("MaintenanceDisabled", "Reg_DWORD", "1"),
    ),
    # Disable Touch Visual Feedback
    r"HKCU\Control Panel\Cursors" : (
        ("GestureVisualization", "Reg_DWORD", "0"),
        ("ContactVisualization", "Reg_DWORD", "0"),
    ),
    # Disable Windows 11 Settings Banner
    r"HKLM\SOFTWARE\Microsoft\WindowsRuntime\ActivatableClassId\ValueBanner.IdealStateFeatureControlProvider" : (
        ("ActivationType", "Reg_DWORD", "0"),
    ),
    # Disable Windows Feedback
    r"HKCU\SOFTWARE\Microsoft\Siuf\Rules" : (
        ("NumberOfSIUFInPeriod", "Reg_DWORD", "0"),
        #("PeriodInNanoSeconds", "Reg_DWORD", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanelt" : (
        ("{2cc5ca98-6485-489a-920e-b3e88a6ccce3}", "Reg_DWORD", "1"),
    ),
    # Do Not Reduce Sounds While in a Call
    r"HKCU\SOFTWARE\Microsoft\Multimedia\Audio" : (
        ("UserDuckingPreference", "Reg_DWORD", "3"),
    ),
    # Hide Disabled and Disconnected Devices in Sounds Panel
    r"HKCU\SOFTWARE\Microsoft\Multimedia\Audio\DeviceCpl" : (
        ("ShowDisconnectedDevices", "Reg_DWORD", "0"),
        ("ShowHiddenDevices", "Reg_DWORD", "0"),
    ),
    r"HKCU\Control Panel\Desktop\WindowMetrics" : (
        ("MinAnimate", "Reg_SZ", "0"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects" : (
        ("VisualFXSetting", "Reg_DWORD", "3"),
    ),
    r"HKCU\SOFTWARE\Microsoft\Windows\DWM" : (
        ("EnableAeroPeek", "Reg_DWORD", "0"),
        ("AlwaysHibernateThumbnails", "Reg_DWORD", "0"),
    ),
    # IRP Stack Size
    r"HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" : (
        ("IRPStackSize", "Reg_DWORD", "30"),
    ),
}

TelementryCMD = [
    r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\Consolidator"',
    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\Consolidator" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\BthSQM"',
    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\BthSQM" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask"',
    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip"',
    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Customer Experience Improvement Program\Uploader"',
    r'schtasks /change /tn "\Microsoft\Windows\Customer Experience Improvement Program\Uploader" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser"',
    r'schtasks /change /tn "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Application Experience\ProgramDataUpdater"',
    r'schtasks /change /tn "\Microsoft\Windows\Application Experience\ProgramDataUpdater" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Application Experience\StartupAppTask"',
    r'schtasks /change /tn "\Microsoft\Windows\Application Experience\StartupAppTask" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector"',
    r'schtasks /change /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver"',
    r'schtasks /change /tn "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem"',
    r'schtasks /change /tn "\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Shell\FamilySafetyMonitor"',
    r'schtasks /change /tn "\Microsoft\Windows\Shell\FamilySafetyMonitor" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Shell\FamilySafetyRefresh"',
    r'schtasks /change /tn "\Microsoft\Windows\Shell\FamilySafetyRefresh" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Shell\FamilySafetyUpload"',
    r'schtasks /change /tn "\Microsoft\Windows\Shell\FamilySafetyUpload" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Autochk\Proxy"',
    r'schtasks /change /tn "\Microsoft\Windows\Autochk\Proxy" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Maintenance\WinSAT"',
    r'schtasks /change /tn "\Microsoft\Windows\Maintenance\WinSAT" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Application Experience\AitAgent"',
    r'schtasks /change /tn "\Microsoft\Windows\Application Experience\AitAgent" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Windows Error Reporting\QueueReporting"',
    r'schtasks /change /tn "\Microsoft\Windows\Windows Error Reporting\QueueReporting" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\CloudExperienceHost\CreateObjectTask"',
    r'schtasks /change /tn "\Microsoft\Windows\CloudExperienceHost\CreateObjectTask" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\DiskFootprint\Diagnostics"',
    r'schtasks /change /tn "\Microsoft\Windows\DiskFootprint\Diagnostics" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\FileHistory\File History (maintenance mode)"',
    r'schtasks /change /tn "\Microsoft\Windows\FileHistory\File History (maintenance mode)" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\PI\Sqm-Tasks"',
    r'schtasks /change /tn "\Microsoft\Windows\PI\Sqm-Tasks" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\NetTrace\GatherNetworkInfo"',
    r'schtasks /change /tn "\Microsoft\Windows\NetTrace\GatherNetworkInfo" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\AppID\SmartScreenSpecific"',
    r'schtasks /change /tn "\Microsoft\Windows\AppID\SmartScreenSpecific" /disable',
    r'schtasks /Change /TN "\Microsoft\Windows\WindowsUpdate\Automatic App Update" /Disable',
    r'schtasks /Change /TN "\Microsoft\Windows\Time Synchronization\ForceSynchronizeTime" /Disable',
    r'schtasks /Change /TN "\Microsoft\Windows\Time Synchronization\SynchronizeTime" /Disable',
    r'schtasks /end /tn "\Microsoft\Windows\HelloFace\FODCleanupTask"',
    r'schtasks /change /tn "\Microsoft\Windows\HelloFace\FODCleanupTask" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Feedback\Siuf\DmClient"',
    r'schtasks /change /tn "\Microsoft\Windows\Feedback\Siuf\DmClient" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload"',
    r'schtasks /change /tn "\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Application Experience\PcaPatchDbTask"',
    r'schtasks /change /tn "\Microsoft\Windows\Application Experience\PcaPatchDbTask" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Device Information\Device"',
    r'schtasks /change /tn "\Microsoft\Windows\Device Information\Device" /disable',
    r'schtasks /end /tn "\Microsoft\Windows\Device Information\Device User"',
    r'schtasks /change /tn "\Microsoft\Windows\Device Information\Device User" /disable',
]
