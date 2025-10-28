[app]
title = WireTun VPN
package.name = wiretunvpn
package.domain = org.vpn

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0
requirements = python3,kivy

[buildozer]
log_level = 2

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.api = 30
android.minapi = 21
