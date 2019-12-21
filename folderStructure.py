#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

def folderStructure(folderPath):
	os.chdir(folderPath)
	directionFolderName = 'template'
	def createStructure():
		for i in os.walk(folderPath):
			if directionFolderName in i[0]:
				continue
			else:
				try:
					os.mkdir(os.getcwd().replace('\\','/')+'\\'+directionFolderName+i[0].replace(os.getcwd().replace('\\','/'),''))
				except:
					continue

	try:
		os.mkdir(directionFolderName)
		createStructure()
	except:
		createStructure()


if __name__ == '__main__':
	folderStructure(input('Folder path: ').replace('\\','/'))


