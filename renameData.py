import os

folderPath = 'data/images'
counter = 1

for filename in os.listdir(folderPath):
    os.rename(folderPath + '\\' + filename, folderPath + '\\' + str(counter) + '.jpg')
    counter += 1