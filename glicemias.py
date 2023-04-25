print('Hello, World!')

glicemia = float(input('Glicemia:\n'))
refeicao = int(input('Será realizada alguma refeição? \n[1] Sim [2] Não\n'))

if refeicao == 1:
    cho = float(input('Qual a quantidade de carboidrato existente na refeição?\n'))
    
elif refeicao == 2:
    print('')


if glicemia <= 20 and refeicao == 1 or refeicao == 2:
    print('🚨🚨🚨\nHipoglicemia grave!!!\nCorrija com carboidrato líquido e vá até o Pronto Socorro mais próximo!\n')
elif 20 < glicemia <= 70 and refeicao == 1:
    print('⚠️⚠️⚠️\nHipoglicemia!!!\nCorrija com 15g de carboidrato e não aplique insulina para essa refeição.')
elif 20 < glicemia <= 70 and refeicao == 2:
    print('⚠️⚠️⚠️\nHipoglicemia!!!\nCorrija com 15g de carboidrato.')
elif 70 < glicemia <= 140 and refeicao ==1:
    print('🎉🎉🎉\nParabéns!\nGlicemia dentro do alvo!\nAplique {:.2f}u de insulina para essa refeição'.format(cho/15))
elif 70 < glicemia <= 140 and refeicao ==2:
    print('🎉🎉🎉\nParabéns!\nGlicemia dentro do alvo!')    
elif 140 < glicemia <= 180 and refeicao ==1:
    print('❗❗❗\nCuidado!\nRisco de hiperglicemia!\nAplique {:.2f}u de insulina para essa refeição'.format(cho/15))
elif 140 < glicemia <= 180 and refeicao==2:
    print('❗❗❗\nCuidado!\nRisco de hiperglicemia!')
elif 180 < glicemia <= 400 and refeicao == 1:
    print('⚠️⚠️⚠️\nHiperglicemia!!!\n Aplique {:.2f}u de insulina de ação rápida para correção e para essa refeição.'.format((glicemia - 100) / 40 + cho /15))
elif 180 < glicemia <= 400 and refeicao == 2:
    print('⚠️⚠️⚠️\nHiperglicemia!!!\nCorrija com {:.2f}u de insulina de ação rápida!'.format((glicemia - 100)/40))
elif glicemia >= 500 and refeicao ==1 or refeicao ==2:
    print('🚨🚨🚨\nHiperglicemia grave!!!\n Corrija com {:.2f}u de insulina e vá até o Pronto Socorro mais próximo!'.format((glicemia - 100)/40))
else:
    print('Digite a glicemia novamente.')
