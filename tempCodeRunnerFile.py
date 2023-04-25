o = glicemia - 100 / 40

if glicemia <= 70:
    print('⚠️⚠️⚠️\nHipoglicemia!!!\nCorrigir com 15g de carboidrato!')
elif 70 > glicemia <= 140:
    print('Glicemia dentro do alvo!')
