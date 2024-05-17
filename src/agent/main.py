import zipfile
import xml.etree.ElementTree as ET
import logging
from datetime import datetime

class Modelk:
    def __init__(self,strname)
        self.strname = strname
    def set_M(self, value):
        self.Move = value
    def set_T(self, value):
        self.Toughness = value
    def set_Sv(self, value):
        self.SaveRoll = value
    def set_W(self, value):
        self.Wounds = value
    def set_LD(self, value):
        self.Leadership = value
    def set_OC(self, value):
        self.OccupyControl = value
        
compressed_rosterfile = '../../Necron Combat Patrol.rosz'
rosteerfile = 'Necron Combat Patrol.ros'

logf = logging.getLogger(__name__)
logfilename = datetime.now().strftime('playeragent_%H_%M_%d_%m_%Y.log')
logging.basicConfig(filename=logfilename, encoding='utf-8', level=logging.INFO)
logf.info("Log Started")

with zipfile.ZipFile(compressed_rosterfile,"r") as zip_ref:
    zip_ref.extractall(".")

tree = ET.parse(rosteerfile)

root = tree.getroot()
selections = root[1][0][0]

#print(selections)
ns = {'wh': 'http://www.battlescribe.net/schema/rosterSchema'}

names = { 'Overlord','Necron Warriors','Skorpekh Destroyers','Canoptek Scarab Swarms' }
indexer = 0
for selection in selections:
    for getname in names:
        print(getname)
        
        if selection.get('name',default='blank') == getname:
            for profiles in selection:
                for profile in profiles:
                    if profile.get('name',default='blank') == getname:
                        for characteristics in profile:
                            for characteristic in characteristics:
                                switch(characteristic.get('name',default='blank')
                                        'M':
                                            str(characteristic.text))
             
#Battle Rounds

#Command Phase

#Movement Phase

#Shooting Phase

#Charge Phase

#Fight Phase