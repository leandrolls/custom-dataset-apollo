import os

folderPath = 'data/cubo amarelo'
counter = 1

for filename in os.listdir(folderPath):
    os.rename(folderPath + '\\' + filename, folderPath + '\\' + str(counter) + '.png')
    counter += 1