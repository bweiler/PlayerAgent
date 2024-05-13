import zipfile
import xml.etree.ElementTree as ET

with zipfile.ZipFile("../../example.rosz","r") as zip_ref:
    zip_ref.extractall(".")

tree = ET.parse('New Roster.ros')

root = tree.getroot()
print("Root is",root)

for chards in root.iter('profile'):
    for charres in chards.iter('characteristic'):
         idi = charres.find('name').text
         name = charres.find('typeId').text
         print('Team (%s): %s' % (idi, name))    
#Battle Rounds

#Command Phase

#Movement Phase

#Shooting Phase

#Charge Phase

#Fight Phase