# SusFileCheck
Statically check any local file against a plethora of suspicious indicators to better detect malignant files.

Program aims to warn you about any and all suspicious indicators it manages to detect.
Upon completion presents you with all suspicious indicators found, with accompanying explanations to each indicator.

### This project is WIP

## Currently performs following checks: (+Mitre Attack references)
- [/] Masquerading - [Masquerading](https://attack.mitre.org/techniques/T1036/)
- [x] RTLO Filename Masquerading - [Masquerading: Right-to-Left Override](https://attack.mitre.org/techniques/T1036/002/)
- [] Alternative Executable Extensions - [User Execution: Malicious File](https://attack.mitre.org/techniques/T1204/002/)
- [x] MOTW Bypass (ISO) - [Subvert Trust Controls: Mark-of-the-Web Bypass](https://attack.mitre.org/techniques/T1553/005/)
- [x] MOTW Bypass (Misc Archives) - [Subvert Trust Controls: Mark-of-the-Web Bypass](https://attack.mitre.org/techniques/T1553/005/)
- [] OpenXML Archive - Masquerading, Subvert Trust Controls
- [x] Multiple File Extensions - [Masquerading: Double File Extension](https://attack.mitre.org/techniques/T1036/007/)
- [x] .lnk Extension - [User Execution: Malicious File](https://attack.mitre.org/techniques/T1204/002/)
- [] .lnk Launch Options - [Boot or Logon Autostart Execution: Shortcut Modification](https://attack.mitre.org/techniques/T1547/009/)
- [x] Contains Homoglyphs? - [D3-HD (Homoglyph Detection)](https://d3fend.mitre.org/technique/d3f:HomoglyphDetection/)
- [] File Magic
- [] Entropy
- [] Virustotal Hash
- [] is Signed?
- [] Filebloat

