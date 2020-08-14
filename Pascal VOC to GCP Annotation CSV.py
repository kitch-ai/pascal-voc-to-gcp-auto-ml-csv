import os
import csv
import xml.etree.ElementTree as ET

googlePath = "gs://kitch-training-data/"
fileUploadDate = "-2020-08-13T17:14:49.864Z.png"

imageWidth = 3840
imageHeight = 2160

with open('google_annotations.csv', mode='w') as google_file:
    google_writer = csv.writer(google_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    

    path = './'
    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)

        fileNameStart = filename[:len(filename) - 4]

        tree = ET.parse(fullname)
        root = tree.getroot()

        for myObject in root.iter('object'):
            category = myObject.find('name').text
            boundBox = myObject.find('bndbox')
            xMin = float(boundBox.find('xmin').text) / imageWidth
            yMin = float(boundBox.find('ymin').text) / imageHeight
            xMax = float(boundBox.find('xmax').text) / imageWidth
            yMax = float(boundBox.find('ymax').text) / imageHeight

            imageName = googlePath + fileNameStart + fileUploadDate
            google_writer.writerow(["",imageName,category,xMin,yMin,"","",xMax,yMax,"",""])



