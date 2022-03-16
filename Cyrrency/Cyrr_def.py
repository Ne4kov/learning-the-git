import re

usd = 'USD'
eur = 'EUR'
chf = 'CHF'
gpb = 'GPB'
cny = 'CNY'

def usd_f(k_usd):
    while True:
        a = input('Введите сумму')
        comp = re.compile('-')
        m = comp.match(a)
        if m:
            print('вы ввели отрицательное число')
            continue
        elif len(a) == 0:
            print('Вы ничего не ввели')
            continue
        elif not a.isnumeric():
            print('это не число, можно число, плеаз?')
            continue
        elif int(a) >= 0:
            print('Вы ввели сумму ', a, 'и валюту ', usd)
            for k, v in k_usd.items():
                r = int(a) * v
                print('конвертированная сумма в ', k, ' = ', round(r, 2))
        break


def eur_f(k_eur):
    while True:
        a = input('Введите сумму')
        comp = re.compile('-')
        m = comp.match(a)
        if m:
            print('вы ввели отрицательное число')
            continue
        elif len(a) == 0:
            print('Вы ничего не ввели')
            continue
        elif not a.isnumeric():
            print('это не число, можно число, плеаз?')
            continue
        elif int(a) >= 0:
            print('Вы ввели сумму ', a, 'и валюту ', eur)
            for k, v in k_eur.items():
                r = int(a) * v
                print('конвертированная сумма в ', k, ' = ', round(r, 2))
        break

def chf_f(k_chf):
    while True:
        a = input('Введите сумму')
        comp = re.compile('-')
        m = comp.match(a)
        if m:
            print('вы ввели отрицательное число')
            continue
        elif len(a) == 0:
            print('Вы ничего не ввели')
            continue
        elif not a.isnumeric():
            print('это не число, можно число, плеаз?')
            continue
        elif int(a) >= 0:
            print('Вы ввели сумму ', a, 'и валюту ', chf)
            for k, v in k_chf.items():
                r = int(a) * v
                print('конвертированная сумма в ', k, ' = ', round(r, 2))
        break


def gpb_f(k_gpb):
    while True:
        a = input('Введите сумму')
        comp = re.compile('-')
        m = comp.match(a)
        if m:
            print('вы ввели отрицательное число')
            continue
        elif len(a) == 0:
            print('Вы ничего не ввели')
            continue
        elif not a.isnumeric():
            print('это не число, можно число, плеаз?')
            continue
        elif int(a) >= 0:
            print('Вы ввели сумму ', a, 'и валюту ', gpb)
            for k, v in k_gpb.items():
                r = int(a) * v
                print('конвертированная сумма в ', k, ' = ', round(r, 2))
        break


def cny_f(k_cny):
    while True:
        a = input('Введите сумму')
        comp = re.compile('-')
        m = comp.match(a)
        if m:
            print('вы ввели отрицательное число')
            continue
        elif len(a) == 0:
            print('Вы ничего не ввели')
            continue
        elif not a.isnumeric():
            print('это не число, можно число, плеаз?')
            continue
        elif int(a) >= 0:
            print('Вы ввели сумму ', a, 'и валюту ', cny)
            for k, v in k_cny.items():
                r = int(a) * v
                print('конвертированная сумма в ', k, ' = ', round(r, 2))
        break


while True:
    currency = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']")
    if currency == usd:
        usd_f({'USD': 1, 'EUR': 0.87, 'CHF': 0.92, 'GBP': 0.73, 'CNY': 6.35})
    elif currency == eur:
        eur_f({'USD': 1.14, 'EUR': 1, 'CHF': 1.05, 'GBP': 0.84, 'CNY': 7.21})
    elif currency == chf:
        chf_f({'USD': 1.08, 'EUR': 0.95, 'CHF': 1, 'GBP': 0.80, 'CNY': 6.86})
    elif currency == gpb:
        gpb_f({'USD': 1.36, 'EUR': 1.20, 'CHF': 1.26, 'GBP': 1, 'CNY': 6.62})
    elif currency == cny:
        cny_f({'USD': 0.16, 'EUR': 0.14, 'CHF': 0.15, 'GBP': 0.12, 'CNY': 1})
    else:
        print('вы ввели не валидную валюту')
