# 引用必要套件
import time
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#時區設定

a = datetime.datetime.today()
o = datetime.timedelta(hours=8)


# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('serviceAccount.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

#首次上傳時初始化用
path_root = "Detector"
collection_ref = db.collection(path_root)
docs = collection_ref.get()
cc = 0
for doc in docs:
    #print("文件內容：{}".format(doc.to_dict()))
    cc += 1  # 取得最後一筆流水號
#print(cc)
#path = "Detector/gas"+str(cc) #現版本被禁用 暫時忽略
#doc_ref = db.document(path)
temp = ''
doc_ref = db.collection('Detector').document('gas')


def query_resetSearch():
    path_root = "Detector"
    collection_ref = db.collection(path_root)
    docs = collection_ref.get()
    cc = 0
    for docx in docs:
        #print("文件內容：{}".format(doc.to_dict()))
        cc += 1  # 取得最後一筆流水號
    #print(cc)
    #path = "Detector/gas"+str(cc)
    #doc_ref = db.document(path)
    path = "gas"+str(cc)
    return db.collection('Detector').document(path)



def queryInsert(insertStr):
    query_resetSearch()
    tempstr = 'gas'+str(cc)
    doc_ref = db.collection("Detector").document(tempstr)
    doc_ref.set(insertStr)


test = []
cc += 1  # 下一個流水號

test = {'id': cc, 'CO2': 1100, 'Ethanol': 0.4, 'CO': 200, 'PM2.5': 299,
        'temperture': 30, 'humidity': 50, 'timestamp': (a+o).strftime("%Y-%m-%d %H:%M:%S")}
#queryInsert(test)