# -*- mode: python ; coding: utf-8 -*-
added_files = [
         ( 'resources/icons/*.*', 'icons' ),
         ( 'resources/language/*.*', 'language' ),
         ( 'resources/images/*.png', 'images' ),
         ( 'resources/styles/*.qss', 'styles' )
         ]

a = Analysis(
    ['src/mainApp.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MarmaraConnector',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['resources/icons/icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MarmaraConnector',
)
