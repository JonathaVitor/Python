dis = float(input('Uma distância em metros: '))
km = dis/1000
hm = dis/100
dam = dis/10
dm = dis*10
cm = dis*100
mm = dis*1000
print('A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(dis, km, hm, dam, dm, cm, mm))
