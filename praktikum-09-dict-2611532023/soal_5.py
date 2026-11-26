n = int(input())
kas = {}

for i in range(n):
    nama, nominal =input().split()
    kas[nama] = kas.get(nama,0)+ int(nominal)
for nama, total in kas.items():
    print(nama +":"+ str(total))
print("total cash:",str(sum(kas.values())))
top = max(kas, key=kas.get)
print("top contributor: "+ top +" ("+ str(kas[top])+")")