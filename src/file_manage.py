import os
from os.path import isdir
import shutil



def filesCopy(source,dest):
    """ copies all files and folders of source folder to dest folder"""

    if os.path.exists(dest):
        shutil.rmtree(dest)

    if not (os.path.exists(source)):
        raise ValueError(f"no path named {source} found")

    def recursy(source,dest):
        if not os.path.exists(dest):
            os.mkdir(dest)
        elements = os.listdir(source)
        for element in elements:
            dest_path = os.path.join(dest,element)
            # source_path = os.path.join(source,element)
            if os.path.isdir(os.path.join(source,element)):
                recursy(os.path.join(source,element),dest_path)
            else:
                print(f"copying the {element} to {dest}")
                shutil.copy(os.path.join(source,element),dest)


    recursy(source,dest)
