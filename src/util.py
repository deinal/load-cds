import os
from subprocess import call

def make_directory(location):
    """
       Creates directory, no error if existing, make parent directories as needed.
    """
    call(['mkdir', '-p', location])

def concat_files(files, outfile):
    """
       Concatenate files to one outfile.
    """
    command = ['cat'] + files + ['>', outfile]
    call(' '.join(command), shell=True)

def listdir_fullpath(d):
    """
       Return a list of all files with their full paths in directory d.
    """
    return [os.path.join(d, f) for f in os.listdir(d)]