import zipfile
import xml.etree.ElementTree as ET
import logging
from datetime import datetime
import re

class Modelk:
    def __init__(self,strname):
        self.strname = strname
    def set_M(self, value):
        tmp = re.findall(r'[^0–9]',value)
        self.Move = int(tmp[0]) 
    def set_T(self, value):
        tmp = re.findall(r'[^0–9]',value)
        self.Toughness = int(tmp[0])
    def set_Sv(self,value):
        tmp = re.findall(r'[^0–9]',value)
        self.SaveRoll = int(tmp[0])
    def set_W(self, value):
        tmp = re.findall(r'[^0–9]',value)
        self.Wounds = int(tmp[0])
    def set_LD(self, value):
        tmp = re.findall(r'[^0–9]',value)
        self.Leadership = int(tmp[0])
    def set_OC(self, value):
        tmp = re.findall(r'[^0–9]',value)
        if len(tmp) == 0:
            self.OccupyControl = 0
        else:
            self.OccupyControl = int(tmp[0])
    def print_contents(self):
        print(self.strname)
        print("   M : " + str(self.Move))
        print("   T : " + str(self.Toughness))
        print("   Sv: " + str(self.SaveRoll))
        print("   W : " + str(self.Wounds))
        print("   LD: " + str(self.Leadership))
        print("   OC: " + str(self.OccupyControl))
        
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

models = []
for selection in selections:
    for getname in names:
        tmp = Modelk(getname)
        if selection.get('name',default='blank') == getname:
            for profiles in selection:
                for profile in profiles:
                    if profile.get('name',default='blank') == getname:
                        for characteristics in profile:
                            for characteristic in characteristics:
                                match characteristic.get('name',default='blank'):
                                        case 'M':
                                            tmp.set_M(characteristic.text)
                                        case 'T':
                                            tmp.set_T(characteristic.text)
                                        case 'SV':
                                            tmp.set_Sv(characteristic.text)
                                        case 'W':
                                            tmp.set_W(characteristic.text)
                                        case 'LD':
                                            tmp.set_LD(characteristic.text)
                                        case 'OC':
                                            tmp.set_OC(characteristic.text)
                            models.append(tmp)
                            
for obj in models:
    obj.print_contents()
                                        
             
#Battle Rounds

#Command Phase

#Movement Phase

#Shooting Phase

#Charge Phase

#Fight Phase