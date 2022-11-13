#*********************************************************************
# content = PANTRY Asset Library Manager
#
# version = 0.0.0 
# date = 2022-11-13
#
# dependencies = Maya(currently)
#
# todos = Create UI (pyside2) and restructure the folders,
#         Maximize save or Export options (currently only .ma),
#		  Screenshot or PrintScreen must be bult in,
#		  Import or load options for Nuke (fbx and obj)
#
# license = MIT
# author = Padmacumar Prabhaharan <padmacumar@gmail.com>
#*********************************************************************

import os
from maya import cmds

#Currently the directory will be default maya project path
DIRECTORY = os.path.join( cmds.internalVar(userAppDir=True), 'PantryLM')


class AssetLibrary(dict):
"""
Created a class here for later reusing 
or inheriting the setup for other DCC packages.
Currently, only for Maya.
Also making it a dictionary.
"""
	# If our directory doesn't exist, create it.
	def createDir(self, directory=DIRECTORY):
		if not os.path.exists(directory):
			os.mkdir(directory)

	# Save
	def save(self, name, directory=DIRECTORY):
		self.createDir(directory)
		path = os.path.join(directory, '%s.ma' % name)
		cmds.file(rename=path)

        if cmds.ls(selection=True):
            cmds.file(force=True, exportSelected=True)
        else:
            cmds.file(save=True, force=True)

    # Find
    def find(self, directory=DIRECTORY):
        if not os.path.exists(directory):
            return

        files = os.listdir(directory)
        mayafiles = [thefile for thefile in files if thefile.endswith('.ma')]

        for ma in mayafiles:
            name, ext = os.path.splitext(ma)

            self[name] = path

    # Load
    def load(self, name):
        path = self[name]['path']
        cmds.file(path, i=True, usingNamespaces=False)