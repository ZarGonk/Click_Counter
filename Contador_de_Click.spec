# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Contador_de_Click.py'],   # seu script principal
    pathex=[],
    binaries=[],
    datas=[('counter.py', '.'), ('assets/mouse_icon.png', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Contador de Click',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,   # não abre terminal
    icon='assets/icon_click.ico'  # ícone personalizado
)
