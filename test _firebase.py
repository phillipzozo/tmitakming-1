import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import datetime
import schedule

a = datetime.datetime.today()
o = datetime.timedelta(hours=8)
#print((a+o).strftime("%Y-%m-%d_%H:%M"))
cred = credentials.Certificate('serviceAccount.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
db = firestore.client()




#query_Get()



#首次上傳時初始化用
path_root = "Detector"
collection_ref = db.collection(path_root)
docs = collection_ref.get()
cc = 0
for doc in docs:
    #print("文件內容：{}".format(doc.to_dict()))
    cc+=1 #取得最後一筆流水號
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

def query_Get():
    # 初始化firestore
    doc_ref = query_resetSearch()
    #Get Collection
    global temp
    try:
        doc = doc_ref.get()
        # 透過 to_dict()將文件轉為dictionary
        temp += 'id => {}'.format(doc.to_dict()['id'])+ '\n' +'PM2.5 => {}'.format(doc.to_dict()['PM2.5']) + '\n' + '二氧化碳 => {}'.format(doc.to_dict()['CO2']) + '\n' + '酒精 => {}'.format(doc.to_dict()['Ethanol']) + '\n' + '一氧化碳 => {}'.format(doc.to_dict()['CO']) + '\n' + '溫度 => {}'.format(doc.to_dict()['temperture']) + '\n' + '濕度 => {}'.format(doc.to_dict()['humidity']) + '\n'  + '時間戳 => {}'.format(doc.to_dict()['timestamp']) + '\n'
        # print("文件內容為：{}".format(doc.to_dict()))
        #print(temp)
       # print(doc_ref)
      #  print(doc)
    except:
        temp += '意外錯誤'
       # print(temp)

def queryInsert(insertStr):
    query_resetSearch()
    tempstr = 'gas'+str(cc)
    doc_ref = db.collection("Detector").document(tempstr)
    doc_ref.set(insertStr)

#try:
 #   doc = doc_ref.get()
    # 透過 to_dict()將文件轉為dictionary
 #   print("文件內容為：{}".format(doc.to_dict()))
#except:
  #  print("指定文件的路徑{}不存在，請檢查路徑是否正確".format(path))

test = []
cc+=1 #下一個流水號

test = {'id': cc, 'CO2': 1100, 'Ethanol': 0.4, 'CO': 200, 'id': 1, 'PM2.5': 299,
        'temperture': 30, 'humidity': 50, 'timestamp': (a+o).strftime("%Y-%m-%d %H:%M:%S")}
queryInsert(test)
#query_Get()
