import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import datetime
import schedule


cred = credentials.Certificate('serviceAccount.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
db = firestore.client()


def query_Get():
    # 初始化firestore

    
    #Get Collection
    doc_ref = db.collection('Detector')
    localtime = time.asctime(time.localtime(time.time()))
    temp = '監測時間 => ' + localtime + '\n'
    try:
        doc = doc_ref.get()
        # 透過 to_dict()將文件轉為dictionary
        #temp += 'PM2.5 => {}'.format(doc.to_dict()['PM2.5']) + '\n' + '二氧化碳 => {}'.format(doc.to_dict()[
        #    'CO2']) + '\n' + '酒精 => {}'.format(doc.to_dict()['Ethanol']) + '\n' + '一氧化碳 => {}'.format(doc.to_dict()['CO']) + '\n'
        # print("文件內容為：{}".format(doc.to_dict()))
        
        print(doc_ref)
        print(doc)
    except:
        print("指定文件的路徑{}不存在，請檢查路徑是否正確".format(path))
        # print(temp)

#query_Get()


path = "Detector/gas"
path_root = "Detector"
doc_ref = db.document(path)
collection_ref = db.collection(path_root)
docs = collection_ref.get()
for doc in docs:
    print("文件內容：{}".format(doc.to_dict()))
try:
    doc = doc_ref.get()
    # 透過 to_dict()將文件轉為dictionary
    print("文件內容為：{}".format(doc.to_dict()))
except:
    print("指定文件的路徑{}不存在，請檢查路徑是否正確".format(path))
