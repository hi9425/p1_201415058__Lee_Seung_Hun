Alldata=list()
Alldata=[["English",100,"Math",200],["English",200,"Math",200],["English",100,"Math",300]]
ens=0
mas=0
for i in Alldata:
    ens=i[1]+ens
    print ens

for c in Alldata:
    mas=c[3]+mas
    print mas
ea=ens/len(Alldata)
ma=mas/len(Alldata)
print ea
print ma

raw_input("201415058 LEE SEUNG HUN")