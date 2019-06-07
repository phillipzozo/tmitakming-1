from google.cloud import firestore
from google.cloud.firestore_v1 import ArrayRemove, ArrayUnion
import google.cloud.exceptions
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from db_object import Gas_Sensing
# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('serviceAccount.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
db = firestore.client()

#test = {'id': cc, 'CO2': 1100, 'Ethanol': 0.4, 'CO': 200, 'PM2.5': 299,
#       'temperture': 30, 'humidity': 50, 'timestamp': (a+o).strftime("%Y-%m-%d %H:%M:%S")}


gas = Gas_Sensing(sid=u'gas999', CO2=u'999', Ethonal=u'999',CO=u'999',PM25=u'999',temperture=u'999',humidity=u'999',timestamp=u'999')

def db_insert(gas):
    db.collection(u'Detector').document(u'999').set(gas.to_dict())


