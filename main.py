import os
os.system('pip3 install pandas')
os.system('pip3 install scipy')
import pandas as pd
from scipy import stats

KRfile = 'Plastic Survey - Final (Combined) - KR.csv'
MNfile = 'Plastic Survey - Final (Combined) - MN.csv'
PHfile = 'Plastic Survey - Final (Combined) - PH.csv'
dataKR = pd.read_csv(KRfile)
dataMN = pd.read_csv(MNfile)
dataPH = pd.read_csv(PHfile)
#data.columns = ['New_plastic_number',	'Plastic_necessity_opinion', 'Plastic_purpose',	'Reusable_number',	'Reuse_plastic_practice',	'Shopping_reusable_practice',	'Attention	Plastic_harm_opinion',	'Reusable_more_use',	'Less_plastic_research',	',Income_reusable_opinion',	'Importance_rank_1',	'Importance_rank_2',	'Importance_rank_3',	'Importance_rank_4',	'Importance_rank_5',	'Age',	'Gender',	'Education',	'Dependants',	'City',	'Income	Increase_choice_1',	'Increase_choice_2',	'Increase_choice_3',	'Increase_choice_4',	'Increase_choice_5']
print(dataKR.head())
print(dataMN.head())
print(dataPH.head())
print('fda')


def mean(p):
    price_total = 0
    for i in p:
        price_total = price_total + i
    return price_total / len(p)


def median(p):
    #p.sort()
    if len(p) % 2 != 0:
        mid_num = int((len(p) - 1) / 2)
        return p[mid_num]
    elif len(p) % 2 == 0:
        mid_num1 = int(len(p) / 2)
        mid_num2 = int(len(p) / 2) - 1
        return (p[mid_num1] + p[mid_num2]) / 2


def mode(p):
    max_count = (0, 0)
    for i in p:
        frequency = p.count(i)
        if frequency > max_count[0]:
            max_count = (frequency, i)
    return max_count[1]


def stand_devb(p):
    m = mean(p)
    total = 0
    for i in range(len(p)):
        total += (p[i] - m) ** 2
    sd = (total / (len(p) - 1)) ** 0.5  # Bessel's correction n-1
    return sd


def data_range(p):
    p.sort()
    r = p[-1] - p[0]
    return r


#mean1 = mean(house_price1)
#mean2 = mean(house_price2)

#sd1 = stand_devb(house_price1)
#sd2 = stand_devb(house_price2)

#n1 = len(house_price1)
#n2 = len(house_price2)

#SE = (sd1 ** 2 / len(house_price1) + sd2 ** 2 / len(house_price2)) ** 0.5

def t_score():
    t = (mean2 - mean1) / SE
    if t < 0:
        t = t * -1
    else:
        t = t

    if mean1 < mean2:
        df = mean1 - 1
    else:
        df = mean2 - 1
    # conservative degrees of freedom, use the smaller sample size and subtract by 1

def pvalue():
    p = stats.t.cdf(-t, df)

    Cohensd = (mean2 - mean1) / (((n1 - 1) * (sd1 ** 2) + (n2 - 1) * (sd2 ** 2)) / n1 + n2 - 2) ** 0.5
    HedgeG = Cohensd * (1 - (3 / (4 * (n1 + n2) - 9)))

print("KR New Plastic#:",mean(dataKR['New_plastic_number']))
print("KR Plastic Necessity:",mean(dataKR['Plastic_necessity_opinion']))
print("KR Reusable#:",mean(dataKR['Reusable_number']))
print("KR ReusablePlasticPractice:",mean(dataKR['Reuse_plastic_practice']))
print("KR ShoppingReusablePractice:",mean(dataKR['Shopping_reusable_practice']))
print("KR AttentionLV:",mean(dataKR['Attention']))
print("KR PlasticHarmOpinion:",mean(dataKR['Plastic_harm_opinion']))
print("KR ReusableMoreUse:",mean(dataKR['Reusable_more_use']))
print("KR LessPlasticResearch:",mean(dataKR['Less_plastic_research']))
print("KR IncomeOpinion:",mean(dataKR['Income_reusable_opinion']))
print("KR Dependants:",mean(dataKR['Dependants']))
print("KR AverageIncome in KRW:",mean(dataKR['Income']))
print("KR MedianIncome in KRW:",median(dataKR['Income']))
print("MN New Plastic#:",mean(dataMN['New_plastic_number']))
print("MN Plastic Necessity:",mean(dataMN['Plastic_necessity_opinion']))
print("MN Reusable#:",mean(dataMN['Reusable_number']))
print("MN ReusablePlasticPractice:",mean(dataMN['Reuse_plastic_practice']))
print("MN ShoppingReusablePractice:",mean(dataMN['Shopping_reusable_practice']))
print("MN AttentionLV:",mean(dataMN['Attention']))
print("MN PlasticHarmOpinion:",mean(dataMN['Plastic_harm_opinion']))
print("MN ReusableMoreUse:",mean(dataMN['Reusable_more_use']))
print("MN LessPlasticResearch:",mean(dataMN['Less_plastic_research']))
print("MN IncomeOpinion:",mean(dataMN['Income_reusable_opinion']))
print("MN Dependants:",mean(dataMN['Dependants']))
print("MN AverageIncome in MNT:",mean(dataMN['Income']))
print("MN MedianIncome in MNT:",median(dataMN['Income']))
print("PH New Plastic#:",mean(dataMN['New_plastic_number']))
print("PH Plastic Necessity:",mean(dataMN['Plastic_necessity_opinion']))
print("PH Reusable#:",mean(dataMN['Reusable_number']))
print("PH ReusablePlasticPractice:",mean(dataMN['Reuse_plastic_practice']))
print("PH ShoppingReusablePractice:",mean(dataMN['Shopping_reusable_practice']))
print("PH AttentionLV:",mean(dataMN['Attention']))
print("PH PlasticHarmOpinion:",mean(dataMN['Plastic_harm_opinion']))
print("PH ReusableMoreUse:",mean(dataMN['Reusable_more_use']))
print("PH LessPlasticResearch:",mean(dataMN['Less_plastic_research']))
print("PH IncomeOpinion:",mean(dataMN['Income_reusable_opinion']))
print("PH Dependants:",mean(dataMN['Dependants']))
print("PH AverageIncome in PHP:",mean(dataMN['Income']))
print("PH MedianIncome in PHP:",median(dataMN['Income']))



#currency convertor
KRAverageIncome = mean(dataKR['Income'])
KRMedianIncome = median(dataKR['Income'])
MNAverageIncome = mean(dataMN['Income'])
MNMedianIncome = median(dataMN['Income'])
PHAverageIncome = mean(dataPH['Income'])
PHMedianIncome = median(dataPH['Income'])

os.system('pip3 install py_currency_converter')
from py_currency_converter import convert

print("KRAverageIncome in USD as of now:",convert(base='KRW', amount=KRAverageIncome, to=['USD']))
print("KRMedianIncome in USD as of now:",convert(base='KRW', amount=KRMedianIncome, to=['USD']))
#As MNT and PHP are not supported by the API manual conversion goes here.
print("MNAverageIncome in USD as of April 9 2021:",MNAverageIncome/2853.34)
print("MNMedianIncome in USD as of April 9 2021:",MNMedianIncome/2853.34)
print("PHAverageIncome in USD as of April 9 2021",PHAverageIncome/48.60)
print("PHMedianIncome in USD as of April 9 2021:",PHMedianIncome/48.60)