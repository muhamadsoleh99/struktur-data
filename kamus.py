capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
    print(capitals[k]," is the capital of ", k)

phoneext={'saalimah':1410, 'hidayah':1137}
print(phoneext)
print(phoneext.keys())
listNama = list(phoneext.keys())
print(listNama)

phoneext.values()
print(list(phoneext.values()))
print(phoneext.items())
itemPhone = list(phoneext.items())
print(itemPhone)
print(itemPhone[-1][0])
