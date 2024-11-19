#
#
#   DEBLOAT
#
#
#

debloatReg = {
    # Debloat Edge
    r"HKLM\SOFTWARE\Policies\Microsoft\Edge" : (
        ("PersonalizationReportingEnabled", "Reg_DWORD", "0"),
        ("ShowRecommendationsEnabled", "Reg_DWORD", "0"),
        ("HideFirstRunExperience", "Reg_DWORD", "1"),
        ("UserFeedbackAllowed", "Reg_DWORD", "0"),
        ("ConfigureDoNotTrack", "Reg_DWORD", "1"),
        ("AlternateErrorPagesEnabled", "Reg_DWORD", "0"),
        ("EdgeCollectionsEnabled", "Reg_DWORD", "0"),
        ("EdgeShoppingAssistantEnabled", "Reg_DWORD", "0"),
        ("MicrosoftEdgeInsiderPromotionEnabled", "Reg_DWORD", "0"),
        ("PersonalizationReportingEnabled", "Reg_DWORD", "0"),
        ("ShowMicrosoftRewards", "Reg_DWORD", "0"),
        ("WebWidgetAllowed", "Reg_DWORD", "0"),
        ("DiagnosticData", "Reg_DWORD", "0"),
        ("EdgeAssetDeliveryServiceEnabled", "Reg_DWORD", "0"),
        ("EdgeCollectionsEnabled", "Reg_DWORD", "0"),
        ("CryptoWalletEnabled", "Reg_DWORD", "0"),
        ("WalletDonationEnabled", "Reg_DWORD", "0"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\EdgeUpdate" : (
        ("CreateDesktopShortcutDefault", "Reg_DWORD", "0"),
    ),
}

debloatRegDelete = [
    # Remove Background Tasks
    r"HKCR\Extensions\ContractId\Windows.BackgroundTasks\PackageId\46928bounde.EclipseManager_2.2.4.51_neutral__a5h4egax66k6y",
    r"HKCR\Extensions\ContractId\Windows.BackgroundTasks\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0",
    r"HKCR\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.MicrosoftOfficeHub_17.7909.7600.0_x64__8wekyb3d8bbwe",
    r"HKCR\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.PPIProjection_10.0.15063.0_neutral_neutral_cw5n1h2txyewy",
    r"HKCR\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.XboxGameCallableUI_1000.15063.0.0_neutral_neutral_cw5n1h2txyewy",
    r"HKCR\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.XboxGameCallableUI_1000.16299.15.0_neutral_neutral_cw5n1h2txyewy",
    # Windows File
    r"HKCR\Extensions\ContractId\Windows.File\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0",
    # Registry keys to delete if they aren't uninstalled by RemoveAppXPackage/RemoveAppXProvisionedPackage
    r"HKCR\Extensions\ContractId\Windows.Launch\PackageId\46928bounde.EclipseManager_2.2.4.51_neutral__a5h4egax66k6y",
    r"HKCR\Extensions\ContractId\Windows.Launch\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0",
    r"HKCR\Extensions\ContractId\Windows.Launch\PackageId\Microsoft.PPIProjection_10.0.15063.0_neutral_neutral_cw5n1h2txyewy",
    r"HKCR\Extensions\ContractId\Windows.Launch\PackageId\Microsoft.XboxGameCallableUI_1000.15063.0.0_neutral_neutral_cw5n1h2txyewy",
    r"HKCR\Extensions\ContractId\Windows.Launch\PackageId\Microsoft.XboxGameCallableUI_1000.16299.15.0_neutral_neutral_cw5n1h2txyewy",
    # Scheduled Tasks to delete
    r"HKCR\Extensions\ContractId\Windows.PreInstalledConfigTask\PackageId\Microsoft.MicrosoftOfficeHub_17.7909.7600.0_x64__8wekyb3d8bbwe",
    # Windows Protocol Keys
    r"HKCR\Extensions\ContractId\Windows.Protocol\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0",
    r"HKCR\Extensions\ContractId\Windows.Protocol\PackageId\Microsoft.PPIProjection_10.0.15063.0_neutral_neutral_cw5n1h2txyewy",
    r"HKCR\Extensions\ContractId\Windows.Protocol\PackageId\Microsoft.XboxGameCallableUI_1000.15063.0.0_neutral_neutral_cw5n1h2txyewy",
    r"HKCR\Extensions\ContractId\Windows.Protocol\PackageId\Microsoft.XboxGameCallableUI_1000.16299.15.0_neutral_neutral_cw5n1h2txyewy",
    # Windows Share Target
    r"HKCR\Extensions\ContractId\Windows.ShareTarget\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0",
    # Disable Give access to context menu
    r"HKCR\*\shellex\ContextMenuHandlers\Sharing",
    r"HKCR\Directory\Background\shellex\ContextMenuHandlers\Sharing",
    r"HKCR\Directory\shellex\ContextMenuHandlers\Sharing",
    r"HKCR\Directory\shellex\CopyHookHandlers\Sharing",
    r"HKCR\Directory\shellex\PropertySheetHandlers\Sharing",
    r"HKCR\Drive\shellex\ContextMenuHandlers\Sharing",
    r"HKCR\Drive\shellex\PropertySheetHandlers\Sharing",
    r"HKCR\LibraryFolder\background\shellex\ContextMenuHandlers\Sharing",
    r"HKCR\UserLibraryFolder\shellex\ContextMenuHandlers\Sharing",
    # Disable Include in library from context menu
    r"HKCR\Folder\ShellEx\ContextMenuHandlers\Library Location",
    r"HKLM\SOFTWARE\Classes\Folder\ShellEx\ContextMenuHandlers\Library Location",
    # Disable Share from context_menu
    r"HKCR\*\shellex\ContextMenuHandlers\ModernSharing",
    # Hide 3D Object Folder
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}",
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}",
    # Hide Music Folder
    r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}",
    r"HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}",
]
