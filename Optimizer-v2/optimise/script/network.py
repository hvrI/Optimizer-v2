#
#
#   NETWORK
#
#

networkReg = {
    r"HKLM\SOFTWARE\Microsoft\MSMQ\Parameters" : (
        ("TCPNoDelay", "Reg_DWORD", "1"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces" : (
        ("TcpDelAckTicks", "Reg_DWORD", "0"),
        ("TcpAckFrequency", "Reg_DWORD", "1"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0x" : (
        ("*SpeedDuplex", "Reg_SZ", "0"),
        ("*FlowControl", "Reg_SZ", "3"),
        ("*RSS", "Reg_SZ", "1"),
        ("*TCPConnectionOffloadIPv4", "Reg_SZ", "1"),
        ("*TCPConnectionOffloadIPv6", "Reg_SZ", "1"),
        ("*IPChecksumOffloadIPv4", "Reg_SZ", "3"),
        ("*TCPChecksumOffloadIPv4", "Reg_SZ", "3"),
        ("*TCPChecksumOffloadIPv6", "Reg_SZ", "3"),
        ("*UDPChecksumOffloadIPv4", "Reg_SZ", "3"),
        ("*UDPChecksumOffloadIPv6", "Reg_SZ", "3"),
        ("*LsoV1IPv4", "Reg_SZ", "1"),
        ("*LsoV2IPv4", "Reg_SZ", "1"),
        ("*LsoV2IPv6", "Reg_SZ", "1"),
        ("*TCPUDPChecksumOffloadIPv4", "Reg_SZ", "3"),
        ("*TCPUDPChecksumOffloadIPv6", "Reg_SZ", "3"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters\Probe\{25aa16d5-73d9-4cd8-91ff-0683b3bcd05a}" : (
        ("LastProbeTime", "Reg_DWORD", "1500872657"),
        ("NetworkPerformsHijacking", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters\Probe\{e97ca175-e5e7-4580-895e-91be966166ba}" : (
        ("LastProbeTime", "Reg_DWORD", "1500872066"),
        ("NetworkPerformsHijacking", "Reg_DWORD", "0"),
    ),
    r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" : (
        ("EnableICMPRedirect", "Reg_DWORD", "0"),
        ("DisableMediaSenseEventLog", "Reg_DWORD", "1"),
        ("DisableTaskOffload", "Reg_DWORD", "1"),
        ("DisableRss", "Reg_DWORD", "0"),
        ("DisableTcpChimneyOffload", "Reg_DWORD", "0"),
        ("DefaultTTL", "Reg_DWORD", "64"),
        ("DisableLargeMtu", "Reg_DWORD", "0"),
        ("EnableConnectionRateLimiting", "Reg_DWORD", "0"),
        ("EnableDCA", "Reg_DWORD", "1"),
        ("EnablePMTUBHDetect", "Reg_DWORD", "0"),
        ("EnablePMTUDiscovery", "Reg_DWORD", "1"),
        ("EnableRSS", "Reg_DWORD", "1"),
        ("EnableTCPA", "Reg_DWORD", "0"),
        ("EnableWsd", "Reg_DWORD", "0"),
        ("GlobalMaxTcpWindowSize", "Reg_DWORD", "0"),
        ("MaxConnectionsPer1_0Server", "Reg_DWORD", "16"),
        ("MaxConnectionsPerServer", "Reg_DWORD", "16"),
        ("MaxFreeTcbs", "Reg_DWORD", "65535"),
        ("MaxHashTableSize", "Reg_DWORD", "65536"),
        ("MaxUserPort", "Reg_DWORD", "65534"),
        ("NumTcbTablePartitions", "Reg_DWORD", "8"),
        ("SackOpts", "Reg_DWORD", "1"),
        ("SynAttackProtect", "Reg_DWORD", "1"),
        ("Tcp1323Opts", "Reg_DWORD", "1"),
        ("TcpCreateAndConnectTcbRateLimitDepth", "Reg_DWORD", "0"),
        ("TcpMaxDataRetransmissions", "Reg_DWORD", "3"),
        ("TcpMaxDupAcks", "Reg_DWORD", "2"),
        ("TcpMaxSendFree", "Reg_DWORD", "65535"),
        ("TcpNumConnections", "Reg_DWORD", "16777214"),
        ("TcpTimedWaitDelay", "Reg_DWORD", "30"),
        ("TcpFinWait2Delay", "Reg_DWORD", "30"),
    ),
    # Quality of Service
    r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\QoS" : (
        ("Do not use NLA", "Reg_SZ", "1"),
    ),
    r"HKLM\SOFTWARE\Policies\Microsoft\Windows\Psched" : (
        ("NonBestEffortLimit", "Reg_DWORD", "0"),
    ),
    # Host Resolution Priority
    r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider" : (
        ("DnsPriority", "Reg_DWORD", "6"),
        ("LocalPriority", "Reg_DWORD", "4"),
        ("HostsPriority", "Reg_DWORD", "5"),
        ("NetbtPriority", "Reg_DWORD", "7"),
    ),
    # Disable Teredo
    r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip6\Parameters" : (
        ("DisabledComponents", "Reg_DWORD", "1"),
    ),
    # Disable Wifi Sense
    r"HKLM\Software\Microsoft\PolicyManager\default\WiFi\AllowWiFiHotSpotReporting" : (
        ("Value", "Reg_DWORD", "0"),
    ),
    r"HKLM\Software\Microsoft\PolicyManager\default\WiFi\AllowAutoConnectToWiFiSenseHotspots" : (
        ("value", "Reg_DWORD", "0"),
    ),
}
