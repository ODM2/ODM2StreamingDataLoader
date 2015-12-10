# -*- mode: python -*-
a = Analysis(['/Users/stephanie/DEV/StreamingDataLoader/src/StreamingDataLoader.py'],
             pathex=['/Users/stephanie/DEV/StreamingDataLoader/setup/Mac'],
             hiddenimports=[],
             hookspath=['/Users/stephanie/DEV/StreamingDataLoader/setup/hooks'],
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='SDLLoader',
          debug=False,
          strip=None,
          upx=True,
          console=False , version='/Users/stephanie/DEV/StreamingDataLoader/setup/version.txt', icon='src/common/icons/SDL.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='SDLLoader')
app = BUNDLE(coll,
             name='SDLLoader.app',
             icon='src/common/icons/SDL.icns')
