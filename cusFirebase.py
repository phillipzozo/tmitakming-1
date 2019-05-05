import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('serviceAccount.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()
#Get Collection
doc_ref = db.collection('Detector').document('gas')
localtime = time.asctime(time.localtime(time.time()))
temp = '最後監測時間為 =>'+ localtime + '\n' 
try:
    doc = doc_ref.get()
# 透過 to_dict()將文件轉為dictionary
    temp +=  'PM2.5 => {}'.format(doc.to_dict()['PM2.5']) + '\n' + '二氧化碳 => {}'.format(doc.to_dict()['CO2']) + '\n' + '酒精 => {}'.format(doc.to_dict()['Ethanol']) + '\n' + '一氧化碳 => {}'.format(doc.to_dict()['CO']) + '\n'
# print("文件內容為：{}".format(doc.to_dict()))
# print(temp)
except:
# print("指定文件的路徑{}不存在，請檢查路徑是否正確".format(path))
#print(temp)

