lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar*alt
tinta = area/2
print('Sua parede tem a dimensão {}x{} e sua área é de {}. \nPara pintar essa parede, você precisará de {}l.'.format(lar, alt, area, tinta))
