from subprocess import run
from distutils.dir_util import copy_tree
import os, shutil, shlex
from sys import exit

output_folder = "[HE][KT]Umineko.Hane.PT-BR.(PC)"

def prepareFiles():

    try:
        os.mkdir(output_folder)
    except:
        pass

    dependencies = [
        'default.ttf',
        'GPL.txt', 
        'Leia-me.txt',
        'ons.cfg', 
        'SDL.dll', 
        'textbox1.zip', 
        'textbox2.zip', 
        'textbox3.zip', 
        'Umineko_Hane_PTBR.exe',
        'Personalizar_caixa_de_texto.bat'
    ]

    for files in dependencies:
        try:
            shutil.copy(files, output_folder)
        except:
            print(f"Couldn't copy {files}")
            pass
    
    try:
        copy_tree('web', f'{output_folder}/web')
    except FileNotFoundError:
        print("Couldn't find the web folder. Skipping.")
        pass

    try:
        shutil.rmtree('bmp/background')
    except FileNotFoundError:
        print("Couldn't find the backgrounds folder. Skipping.")
    
    try:
        copy_tree('legacy_extra/bmp', f'bmp')
    except FileNotFoundError:
        print("Couldn't find the legacy_extra folder. Skipping.")

def compile():
    try:
        os.remove('nscript.dat')
    except FileNotFoundError:
        pass

    nscript_args = '-o nscript.dat SCRIPTS/PC/hane_pc.txt'
    # shutil.copy('SCRIPTS/PC/hane_pc.txt', '0.txt')
    run(['dependencies/nscmake.exe'] + shlex.split(nscript_args))
    shutil.move('nscript.dat', output_folder)

    nsa_args = 'arc.nsa bmp'
    run(['dependencies/nsamake.exe'] + shlex.split(nsa_args))
    shutil.move('arc.nsa', output_folder)

    zip_args = f"HE.KT.Umineko.Hane.PT-BR.(Legacy.Art).7z {output_folder}"
    run([r'dependencies/7za.exe', 'a'] + shlex.split(zip_args))

def cleanup():
    shutil.rmtree(output_folder)

prepareFiles()
compile()
cleanup()