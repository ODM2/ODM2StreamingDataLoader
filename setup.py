
# -*- coding: utf-8 -*-
from __future__ import with_statement
__author__ = 'stephanie'
import os, sys, shutil, zipfile, platform
from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED

#need Windows installer
#windows installer with console
#windows no install( include console)
#mac installer
#mac no installer




## Update odmtools.meta.data whenever creating a release
from src.meta import data
# sys.path.insert(0, '/Users/stephanie/DEV/ODM2PythonAPI')

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SETUP_DIR= os.path.join(BASE_DIR, "setup")

WIN_DIR = os.path.join(SETUP_DIR, "Windows")
MAC_DIR = os.path.join(SETUP_DIR, "Mac")

MAC_DIST_DIR = os.path.join(MAC_DIR, "Dist")
DIST_DIR = os.path.join(WIN_DIR, 'Dist')


MAC_WORK_DIR = os.path.join(MAC_DIR, "Temp")
WORK_DIR = os.path.join(WIN_DIR, "Temp")

ICON_DIR = os.path.join('src', 'common', "icons")
WIN_ICON_FILE = os.path.join(ICON_DIR, "SDL.ico")
MAC_ICON_FILE = os.path.join(ICON_DIR, "SDL.icns")

APP_LOADER_DIR = os.path.join(MAC_DIR, 'Dist', "SDLLoader.app")
# Location of Windows files
APP_LOADER_FILE = os.path.join(BASE_DIR, 'src', "StreamingDataLoader.py")


MAKE_FILE = os.path.realpath(__file__)
VERSION_FILE = os.path.join(SETUP_DIR, "version.txt")

HOOK_DIR = os.path.join(SETUP_DIR, "hooks")
print "@@@@@@Hook dir", HOOK_DIR
# Location of Innosetup Installer
INNO_SCRIPT = os.path.join(WIN_DIR, "sdl_setup.iss")
INNO_EXECUTABLE = '"C:\\Program Files (x86)\\Inno Setup 5\\ISCC.exe"'
ICE_SCRIPT = os.path.join(MAC_DIR, "sdl_setup.packproj")
ICE_EXECUTABLE ='freeze'

def check_if_dirs_exist():
    try:
        if sys.platform == 'win32':
            print "Trying to open WIN_DIR: ",
            if not os.path.exists(WIN_DIR):
                os.mkdir(WIN_DIR)
                print "Created: ", WIN_DIR
            print "Success"

            print "Trying to confirm that INNO_SCRIPT exists: ",
            assert os.path.exists(INNO_SCRIPT)
            print "Success: ", INNO_SCRIPT
        elif sys.platform =="darwin":
            print "Trying to open MAC_DIR: "
            assert os.path.exists(MAC_DIR)
            print "Success"

        print "Trying to open WORK_DIR: ",
        if not os.path.exists(WORK_DIR):
            print "Failed... Trying to create the folder...",
            os.mkdir(WORK_DIR)
            print "Created: ", WORK_DIR
        print "Success"


        print "Trying to open DIST_DIR: ",
        if not os.path.exists(DIST_DIR):
            print "Failed... Trying to create the folder...",
            os.mkdir(DIST_DIR)
            print "Created: ", DIST_DIR
        print "Success"

        print "Trying to open ICON_DIR: ",
        assert os.path.exists(ICON_DIR)
        print "Success"

    except Exception as e:
        print e

def zipdir(basedir, archivename):
    assert os.path.isdir(basedir)
    with closing(ZipFile(archivename, "w", ZIP_DEFLATED)) as z:
        for root, dirs, files in os.walk(basedir):
            #NOTE: ignore empty directories
            for fn in files:
                absfn = os.path.join(root, fn)
                zfn = absfn[len(basedir)+len(os.sep):]
                z.write(absfn, zfn)
def printInfo():
    print "============================================================="
    print "=             SDL Installer                             "
    print "= Be sure to update src/meta/data with every release    "
    print "= Building release: {version}".format(version=data.version),
    print "\n= Platform: {platform}, {architecture}".format(platform=sys.platform, architecture=platform.architecture()), "\n="
    print "============================================================="
    print "Environment Variables: "
    print ("APP_FILE: ", APP_LOADER_FILE)
    print ("MAKE_FILE: ", MAKE_FILE)
    print ("BASE_DIR: ", BASE_DIR)
    print ("SETUP_DIR: ", SETUP_DIR)
    print ("DIST_DIR: ", DIST_DIR)

    ## Windows Specific Files/Directories
    print ("WIN_DIR: ", WIN_DIR)
    print ("WIN_ICON_FILE: ", WIN_ICON_FILE)
    print ("WORK_DIR: ", WORK_DIR)
    print ("INNO_SCRIPT: ", INNO_SCRIPT)
    print ("INNO_EXECUTABLE: ", INNO_EXECUTABLE)

    # OSX Specific Files/Directories
    print ("MAC_DIR: ", MAC_DIR)
    # print ("MAC_ICON_FILE: ", MAC_ICON_FILE)
    print ("MAC_WORK_DIR: ", MAC_WORK_DIR)

    print "============================================================="
    print "Checking if the required directories exist"

    check_if_dirs_exist()

def obtain_exe_filename(console=False):
    if console:
        return "{app}_{version}_{os}_{arch}_{type}".format(app=data.app_name,
        version=data.version, os=sys.platform, arch='x86_64', type= "console")
    else:
        return "{app}_{version}_{os}_{arch}".format(app=data.app_name,
        version=data.version, os=sys.platform, arch='x86_64')

def delete_old_out_dir():
    loc_exists = os.path.exists(DIST_DIR)
    isFile = os.path.isfile(DIST_DIR)
    isDir = os.path.isdir(DIST_DIR)
    if loc_exists and isFile:
        print "Removing file DIST_DIR"
        os.remove(DIST_DIR)
    elif loc_exists and isDir:
        print "Removing directory DIST_DIR"
        shutil.rmtree(DIST_DIR)
    else:
        print "Nothing to remove"


def run_pyinstaller( Name= None, File = None, console=False):
    try:
        if Name is None:
            Name = 'SDLLoader'
        if File is None:
            File = APP_LOADER_FILE
        if console:
            ## Console Version
            os.system('pyinstaller '
                '--clean '
                '--additional-hooks-dir=%s'% HOOK_DIR +
                '--distpath=%s ' % WIN_DIR +
                '--workpath=%s ' % WORK_DIR +
                '--name=%s ' % Name +
                '--specpath=%s ' % WIN_DIR +
                '--upx-dir=%s ' % BASE_DIR +
                '--icon=%s ' % WIN_ICON_FILE +
                '--version-file=%s ' % VERSION_FILE +
                '--noconfirm ' + File)
        else:
            ## Non Console Version
            val = os.system('pyinstaller '
                '--clean '
                '--distpath=%s ' % WIN_DIR +
                '--name=%s ' % Name +
                '--workpath=%s ' % WORK_DIR +
                '--additional-hooks-dir=%s'% HOOK_DIR +
                '--specpath=%s ' % WIN_DIR +
                '--upx-dir=%s ' % BASE_DIR +
                '--icon=%s ' % WIN_ICON_FILE +
                '--version-file=%s ' % VERSION_FILE +
                '--noconsole '
                '--noconfirm ' + File)

        return True
    except Exception as e:
        print (e)
        return False

def mac_pyinstaller(Name = None, File = None):
    try:
        if Name is None:
            Name = 'SDLLoader'
        if File is None:
            File = APP_LOADER_FILE
        os.system('pyinstaller '
            '--clean '
            '--distpath=%s ' % MAC_DIST_DIR +
            '--additional-hooks-dir=%s '% HOOK_DIR +
            '--workpath=%s ' % MAC_WORK_DIR +
            '--specpath=%s ' % MAC_DIR +
            '--upx-dir=%s ' % BASE_DIR +
            '--icon=%s ' % MAC_ICON_FILE +
            '--version-file=%s ' % VERSION_FILE +
            '--name=%s ' % Name +
            '--windowed '
            '--noconfirm ' + File)

        APP_DIR = os.path.join(MAC_DIR, 'Dist', Name+".app")


        #/Users/denversmith/miniconda/envs/SDL-env/lib/libwx_osx_cocoau-3.0.0.0.0.dylib
        path = os.path.dirname(os.path.dirname(sys.executable))

        python = os.path.join(path, 'lib', 'libwx_osx_cocoau-3.0.0.0.0.dylib')
        os.system("cp  %s %s" %(python, os.path.join(APP_DIR, "Contents", "MacOS")))

        return True
    except Exception as e:
        print (e)
        return False

def move_to_dist(filename):
    assert filename

    if not os.path.isdir(DIST_DIR):
        os.mkdir(DIST_DIR)

    print "Moving {filename} to {dist}".format(filename=os.path.abspath(filename), dist=DIST_DIR),
    try:
        shutil.move(os.path.abspath(filename), DIST_DIR)
        print "Success"
    except shutil.Error as e:
        print (e)


def run_inno():
    os.system(INNO_EXECUTABLE + " " + INNO_SCRIPT)

def run_no_installer():
    # Need to finish, Not functional
    raise ("Not functional yet")
    filename = obtain_exe_filename()

    zipdir(BASE_DIR, filename)
    move_to_dist(filename)


def run_iceberg():
    os.system(ICE_EXECUTABLE + " "+ ICE_SCRIPT)

def main():
    delete_old_out_dir()
    printInfo()

    if sys.platform == 'win32':

        print "Creating Windows Executable..."
        if run_pyinstaller('SDLLoader', os.path.join(BASE_DIR, 'src', "StreamingDataLoader.py")):
            if run_pyinstaller('SDLWizard', os.path.join(BASE_DIR, 'src', 'wizard', 'controller', "frmMain.py")):
                run_inno()
        '''
        print "Creating Windows Executable Console..."
        if run_pyinstaller(console=True):
            run_inno()

        print "Create No Installer "
        run_no_installer()
        '''
        ## Create Shortcut
        ## Create File
        ## Zip Executable

    elif sys.platform =='darwin':
        print "Creating Mac Executable"
        if mac_pyinstaller('SDLLoader', os.path.join(BASE_DIR, 'src', "StreamingDataLoader.py")):
            if mac_pyinstaller('SDLWizard', os.path.join(BASE_DIR, 'src', 'wizard', 'controller', "frmMain.py")):
                run_iceberg()

    # elif sys.platform == 'linux2':
    #     ## Testing, not officially supported
    #     run_no_installer()


if __name__ == '__main__':
    main()
