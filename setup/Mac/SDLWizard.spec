# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/denversmith/Documents/Programming/ODM2StreamingDataLoader/src/wizard/controller/frmMain.py'],
             pathex=['/Users/denversmith/Documents/Programming/ODM2StreamingDataLoader/setup/Mac'],
             hiddenimports=[],
             hookspath=['/Users/denversmith/Documents/Programming/ODM2StreamingDataLoader/setup/hooks'],
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='SDLWizard',
          debug=False,
          strip=None,
          upx=True,
          console=False , version='/Users/denversmith/Documents/Programming/ODM2StreamingDataLoader/setup/version.txt', icon='src/common/icons/SDL.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='SDLWizard')
app = BUNDLE(coll,
             name='SDLWizard.app',
             icon='src/common/icons/SDL.icns',
             bundle_identifier=None)
