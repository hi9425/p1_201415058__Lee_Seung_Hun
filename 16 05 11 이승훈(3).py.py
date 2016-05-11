allData=list()
allData=[['Coffee','Water','Milk','Icecream'],['Espresso','No','No','No'],['Long Black','Yes','No','No'],["Flat White","No","Yes","No"],["Cappuccino","No","Yes","No"],["Affogato","No","No","Yes"]]
Data=allData[1:]
def CF():
 for i in Data:
  print i[0]

def MK():
 none=0
 for i in Data:
  if i[2]=='No':
   none=none+1
 print none

def MCF():
 for i in Data:
  if i[2]!='No':
   print i[0]


CF()
MK()
MCF()

raw_input("201415058 LEE SEUNG HUN")