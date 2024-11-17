#
#
#
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
    r"" : (
        ("", "Reg_DWORD", "0"),
    ),
    r"" : (
        ("", "Reg_DWORD", "0"),
    ),
    r"" : (
        ("", "Reg_DWORD", "0"),
    ),
    r"" : (
        ("", "Reg_DWORD", "0"),
    ),
    r"" : (
        ("", "Reg_DWORD", "0"),
    ),
}