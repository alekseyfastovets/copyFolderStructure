import os

def folderStructure(folderPath):
	os.chdir(folderPath)
	def createStructure():
		for i in os.walk(folderPath):
			try:
				os.mkdir(os.getcwd()+'\\template'+i[0].replace(os.getcwd(),''))
			except:
				continue

	try:
		os.mkdir('template')
		createStructure()
	except:
		createStructure()


if __name__ == '__main__':
	folderStructure(input('Путь к эталону: '))


