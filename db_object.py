from google.cloud import firestore
from google.cloud.firestore_v1 import ArrayRemove, ArrayUnion
import google.cloud.exceptions

#test = {'id': cc, 'CO2': 1100, 'Ethanol': 0.4, 'CO': 200, 'PM2.5': 299,
 #       'temperture': 30, 'humidity': 50, 'timestamp': (a+o).strftime("%Y-%m-%d %H:%M:%S")}

#氣體偵測模塊
class Gas_Sensing(object):
    def __init__(self, sid, CO2, Ethonal, CO, PM25,temperture,humidity,timestamp):
        self.sid = sid
        self.CO2 = CO2
        self.Ethonal = Ethonal
        self.CO = CO
        self.PM25 = PM25
        self.temperture = temperture
        self.humidity = humidity
        self.timestamp = timestamp

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        gas = Gas_Sensing(source[u'sid'], source[u'CO2'], source[u'Ethonal'],source[u'CO'],source[u'PM25'],
        source[u'temperture'],source[u'humidity'],source[u'timestamp'])

        if u'sid' in source:
            gas.sid = source[u'sid']

        if u'CO2' in source:
            gas.CO2 = source[u'CO2']
        
        if u'Ethonal' in source:
            gas.Ethonal = source[u'Ethonal']
        
        if u'CO' in source:
            gas.CO = source[u'CO']
        
        if u'PM25' in source:
            gas.PM25 = source[u'PM25']
        
        if u'temperture' in source:
            gas.temperture = source[u'temperture']
        
        if u'humidity' in source:
            gas.sid = source[u'humidity']
        
        if u'timestamp' in source:
            gas.sid = source[u'timestamp']

        return gas
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'sid': self.sid, 
            u'CO2': self.CO2,
            u'Ethonal': self.Ethonal,
            u'CO': self.CO,
            u'PM25':self.PM25,
            u'temperture':self.temperture,
            u'humidity':self.humidity,
            u'timestamp':self.timestamp
        }

        if self.sid:
            dest[u'sid'] = self.sid
            dest[u'CO2'] = self.CO2
            dest[u'Ethonal'] = self.Ethonal
            dest[u'PM25'] = self.PM25
            dest[u'temperture'] = self.temperture
            dest[u'humidity'] = self.humidity
            dest[u'timestamp'] = self.timestamp
              
        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            u'Gas_Sensing(sid={}, CO2={}, Ethonal={}, PM25={}, temperture={},humidity={},timestamp={})'
            .format(self.sid, self.CO2, self.Ethonal, self.PM25, self.temperture, self.hunidity
            , self.timestamp))
# [END 氣體偵測模塊_class_def]



