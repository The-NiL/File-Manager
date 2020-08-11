#!/usr/bin/env python3

'''
                        | made by " --name-- = '--Niloo--' " :) |
    this module finds/copies/removes files with desired extensions
'''

import os
import shutil


def home_check(directory):

    ''' part of program, not for importing '''
    
    if '~' in directory:
        directory = directory.replace('~',os.path.expanduser('~'))
    return directory

def splitter(dest, my_files):

    ''' utility function '''

    my_input_files = {}
    splitted = dest.split()
    file = splitted[1].split(',')
    for name in file:
        my_input_files = { name:root for file_name,root in my_files.items() if file_name == name }
    if len(splitted) == 2 :
        return my_input_files,splitted[1]
    else:
        return my_input_files,splitted[2]
                     
def remove(my_files):

    ''' not complete yet to be used when it is imported, don't use it '''

    if isinstance(my_files,str):
        os.remove(my_files)
    else:
        for file_name,root in my_files.items():
            if os.path.isdir(root):
                os.remove(root + '/' + file_name)
    print('Done =)')

def menu():
    
    '''  Main Menu '''

    print("\n\n*For copying all of the files : cp -a destination_path")
    print("*For copying specific file/files : cp filenames(seperated by ',') destination_path")
    print("*For removing all files from where it exist : rm -a")
    print("*For removing specific file/files from where it exist : rm filenames(seperated by ',') destination_path")
    print("*Enter 'q' to exit")
    dest = input(':')
    return dest

def find(directory, extension):

    '''
        --> Parameters = string,string
        ** finds all of the files with desired extension in all 
        of subdirectories of given directory **
        --> output = a dictionary of found file names as keys and their paths as values
    '''

    my_files = {}
    directory = home_check(directory)
    for root,Dirs,files in os.walk(directory):
        for file_name in files:
            # ._  are for some kind of system files in MacOS
            if file_name.endswith(extension) and '._' not in file_name:
                my_files[file_name] = root       
    if __name__ == '__main__':
        print(len(my_files),'files found,do you want to print them?(y/n)')
        res = input(':')
        if res == 'y':
            for file_name,root in my_files.items():
                    print(root, file_name)
        elif res == 'n':
            pass
        while True:
            dest = menu()
            if dest == 'q':
                exit()
            elif 'cp -a' in dest:
                splitted = dest.split()
                copy(splitted[2],my_files)
            elif 'cp' in dest and '-a' not in dest:
                my_input_files,dest = splitter(dest,my_files)
                copy(dest,my_input_files)           
            elif 'rm -a' in dest:
                for file_name,root in my_files.items():
                    os.remove(root + '/' + file_name)
            elif 'rm' in dest and '-a' not in dest:
                my_input_files,dest = splitter(dest,my_files)
                remove(my_input_files)
    else:
        return my_files

def copy(dest,my_files):

    '''
    --> Parameters = string,dictionary(includes file names as keys and the path
        to them as value)
        ** copies files into the given directory **
    '''

    if not os.path.isdir(dest):
            os.mkdir(dest)
    dest = home_check(dest)
    for file_name,root in my_files.items(): 
        new_dest = dest + '/' + file_name
        shutil.copyfile(os.path.join(root,file_name), new_dest)
    print('Done =)')


if __name__ == '__main__':
    directory = input("Enter the directory you wanna search through: ")
    extension = input("Enter the file extension you wanna search for: ")
    find(directory,extension)
    
