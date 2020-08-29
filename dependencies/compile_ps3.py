from subprocess import run
from distutils.dir_util import copy_tree
import os, shutil, shlex
from sys import exit

# Nome da pasta onde os arquivos do patch serão enviados
output_folder = "[HE][KT]Umineko.Hane.PT-BR.(PS3)"

def prepareFiles():

    try:
        os.mkdir(output_folder)
    except:
        pass

# Lista de ARQUIVOS (não pastas!) que são necessários para montar o patch 
# (atenção: não incluir o nscript.dat ou arc.nsa que são compilados por esse script posteriormente)
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
    
    # copia a pasta web. Para copiar outras pastas, reuse este bloco de código
    # tradução do que está sob o TRY: copy_tree('pasta que você quer copiar', f'{output_folder}/para onde ela vai' << pode ser para dentro dela mesmo, como no caso abaixo)
    try:
        copy_tree('web', f'{output_folder}/web')
    except FileNotFoundError:
        print("Couldn't find the web folder. Skipping.")
        pass

def compile():
    try:
        os.remove('nscript.dat')
    except FileNotFoundError:
        pass

    # caso precise modificar o caminho ou o nome do script, editar ele abaixo
    # IMPORTANTE: o nome do arquivo, caso modificado, precisa também ser modificado nos scripts do Github Actions, sob a pasta .github/workflows neste repositório
    nscript_args = '-o nscript.dat SCRIPTS/PS3/hane_ps3.txt'
    # shutil.copy('SCRIPTS/PS3/hane_ps3.txt', '0.txt')
    run(['dependencies/nscmake.exe'] + shlex.split(nscript_args))
    shutil.move('nscript.dat', output_folder)

    nsa_args = 'arc.nsa bmp bmp2'
    run(['dependencies/nsamake.exe'] + shlex.split(nsa_args))
    shutil.move('arc.nsa', output_folder)

    # nome do arquivo de destino
    # IMPORTANTE: o nome do arquivo, caso modificado, precisa também ser modificado nos scripts do Github Actions, sob a pasta .github/workflows neste repositório
    zip_args = f"HE.KT.Umineko.Hane.PT-BR.(PS3).7z {output_folder}"
    run([r'dependencies/7za.exe', 'a'] + shlex.split(zip_args))

def cleanup():
    shutil.rmtree(output_folder)

prepareFiles()
compile()
cleanup()