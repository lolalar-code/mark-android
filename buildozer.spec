[app]
title = Markirovka Tizimi
package.name = markirovkatizimi
package.domain = uz.markirovka

source.dir = .
source.include_exts = py,json,wav

version = 1.0.0

requirements = python3,kivy==2.3.0,openpyxl,pillow

orientation = portrait

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.arch = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
