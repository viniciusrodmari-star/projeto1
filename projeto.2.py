import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
#entrada
capital_inicial =float (input('capital inicial:'))
aporte = float(input('aporte mensal:'))
meses = float (input('Prazo (meses) : '))
cdi_anual = float(input('CDI anual % :'))/100
perc_cdb = float(input('percentual do CDI - LCI (%):'))/100
perc_lci = float(input('Percentual do CDI - LCI (%):'))/100
taxa_fii = float(input("Rentabilidade do FII(%)"))/100
meta = float(input("Meta financeira (R$):"))/100
#conversao CDI
cdi_mensal = math.pow((1+cdi_anual),1/12)-1
#total investido 
total_investido = capital_inicial + (aporte * meses)
#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital_inicial* math.pow((1+taxa_cdb),meses)+(aporte*meses))
lucro_cdb = montante_cdb - total_investido 
montante_cdb_liquido = total_investido + (lucro_cdb*.85)
#LCI/LCA1
taxa_lci = cdi_mensal * perc_lci
montante_cdi = ( capital_inicial * math.pow((1+taxa_lci),meses)+ (aporte*meses))
#poupança 
taxa_poupança = 0.005
montante_poupança =(capital_inicial* math.pow((taxa_poupança),meses))+(aporte*meses)
#FII com Simulação Estatístic
#gerar variação aleatória 5
fii_base = (capital_inicial * math.pow((1 + taxa_fii), meses)) + (aporte * meses)
fii1 = fii_base * (1 + random.uniform(-0.03,0.03))
fii2 = fii_base * (1 + random.uniform(-0.03,0.03))
fii3 = fii_base * (1 + random.uniform(-0.03,0.03))
fii4 = fii_base * (1 + random.uniform(-0.03,0.03))
fii5 = fii_base * (1 + random.uniform(-0.03,0.03))
simulacoes = [fii1, fii2, fii3, fii4, fii5]
media_fii = statistics.mean(simulacoes)
mediana_fii = statistics.median(simulacoes)
desvio_fii = statistics.stdev(simulacoes)
print("Simulações:", fii_base)
print("Média:", media_fii)
print("Mediana:", mediana_fii)
print("Desvio padrão:", desvio_fii)
print(f"Média: {media_fii:.3f}")
print(f"Mediana: {mediana_fii:.3f}")
print(f"Desvio padrão: {desvio_fii:.3f}")
#formataçao monetaria
#juntar tudo em um so valor brasileiro 
print("Total investido:", locale.currency(total_investido, grouping=True))
print("Média FII:", locale.currency(media_fii, grouping=True))
#Data de resgate
hoje = datetime.datetime.now()
dias = meses * 30
data_resgate = hoje + datetime.timedelta(days=dias)
print("Data atual:", hoje)
print("Data de resgate:", data_resgate)


