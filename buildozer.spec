[app]

title = Bonjour Kone

package.name = bonjourkone
package.domain = org.kone

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0

# Android
android.api = 34
android.minapi = 21
android.ndk = 27b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

log_level = 2

warn_on_root = 1
