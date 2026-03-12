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
montante_cdb = (capital_inicial* math.pow((1+taxa_cdb)),meses+(aporte*meses))
lucro_cdb = montante_cdb - total_investido 
montante_cdb_liquido =total_investido + (lucro_cdb*.85)
#LCI/LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = ( capital_inicial * math.pow((1+taxa_lci),meses)+ (aporte*meses))
#poupança 
taxa_poupança = 0.005
montante_poupança =(capital_inicial* math.pow(taxa_poupança),meses)
