from random import randint
from random import uniform
import math
from functions import *


def task_1():
    patients_from_onefive = randint(1, 5)
    patients_from_six = patients_from_onefive * 2
    answer = "1. \n"
    text = f"1. В больнице у кабинета врача ожидают приема по одному больному из палат № 1-5 {int(patients_from_onefive)} и {int(patients_from_six)} больных из палаты № 6 " \
           "Врач наугад приглашает по одному больному. Какова вероятность того, что:\n"
    text += "a) первым будет приглашен больной из палаты № 6, а второй — не из палаты № 6\n"
    p1 = patients_from_six / (patients_from_onefive + patients_from_six)  # Вероятность, что первым будет приглашен больной из палаты № 6
    p2 = patients_from_onefive / (patients_from_onefive + patients_from_six - 1)  # Вероятность, что вторым приглашенным не будет больной из палаты № 6
    answer += f"а) {p1 * p2}\n"
    text += f"б) трое первых больных, принятых врачом, окажутся соответственно из палат №№ 1, 2 и 3?\n"
    p3 = (patients_from_onefive / (patients_from_onefive + patients_from_six)) * ((patients_from_onefive - 1) / (patients_from_onefive + patients_from_six - 1)) * ((patients_from_onefive - 2) / (patients_from_onefive + patients_from_six - 2))
    answer += f"б) {p3}\n"
    return text, answer
from math import comb
from random import randint

def task_2():
    juice_sm = randint (5, 15)
    juice_vish = juice_sm * 2 
    vin = juice_sm
    vibor = juice_sm
    answer = "2. \n"
    text = f"2. На прилавках супермаркета 'Тройка' выставлены одинаковые банки: {int(juice_sm)} - с соком смородины, {int( juice_vish)} - с соком вишни и {int(vin)} - с вином. Неразборчивый покупатель не глядя берет {int(vibor)} банок. Найти вероятность того, что:\n"
    text += "а) три из них будут с вином;\n"
    p_vin = vin / (juice_sm + juice_vish + vin)
    p_three_vin = (p_vin ** 3) * ((1 - p_vin) ** 2)
    answer += f"а) {p_three_vin}\n"

    p_smorodina = juice_sm / (juice_sm + juice_vish)
    p_vishnya = juice_vish / (juice_sm + juice_vish)
    p_two_smorodina_two_vishnya = (comb(vibor, 2) * p_smorodina ** 2 * p_vishnya ** 2) / comb(juice_sm + juice_vish + vin, vibor)
    text += "б) две банки будут со смородиновым и две — с вишневым соком.\n"
    answer += f"б) {p_two_smorodina_two_vishnya}\n"

    return text, answer

def task_3():
    text = "3. Машинно-котельная установка состоит из двух котлов и одной машины. Рассмотрим события: A - исправна машина; Bk - исправен k-й котел (k = 1,2); C - установка исправна. Установка считается исправной, если работает машина и хотя бы один котел. Выразить события C и ¬C через A и Bk.\n"
    answer = "3. \n" \
             "C = A ∩ (B1 ∪ B2)\n" \
             "¬C = ¬A ∪ (¬B1 ∩ ¬B2)\n"
    return text, answer

def task_4():
    s1 = randint(6, 9) / 10
    s2 = randint(4, 7) / 10
    answer = "4. \n"
    text = f"4.В университете ожидают иностранную делегацию,
в которую входят два иллюзиониста. Первый из них дает
интервью с вероятностью {s1}, второй — {s2}." \
           " Какова вероятность того, что корреспонденту газеты «Транспортник»:\n"

    text += "а) дадут интервью оба иллюзиониста;\n"
    answer += f"a) {round(s1 * s2, 2)}\n"

    text += "б) даст интервью хотя бы один из них;\n"
    answer += f"б) {round(1 - ((1 - s1) * (1 - s2)), 2)}\n"

    text += "в) даст интервью только первый иллюзионист?\n"
    o2 = ((s1 * (1 - s2)) + ((1 - s1) * s2))
    answer += f"в) {round(o2, 2)}\n"
    return text, answer


def task_5():
    kr1 = randint(1, 4) / 10
    kr2 = randint(2, 6) / 10
    text = f"5. Вероятность того, что в течение месяца на кафедру высшей математики по электронной почте придет контрольная работа студента-заочника из г. Бердяуш, равна {kr1}, а из г. Топки — {kr2}. В течение месяца были получены 4 контрольные работы. Какова вероятность, что работ из Бердяуша было больше, чем из Топков?\n"
    
    p = 0
    for i in range(1, 5): # работ из Бердяуша должно быть больше, чем из Топков, т.е. от 1 до 4
        for j in range(0, i): # работ из Топков меньше, чем из Бердяуша
            p += comb(4, i) * (kr1 ** i) * (1 - kr1) ** (4 - i) * comb(4 - i, j) * (kr2 ** j) * (1 - kr2) ** (4 - i - j)
    
    answer = f"5. Вероятность, что работ из Бердяуша было больше, чем из Топков: {round(p, 6)}.\n"
    return text, answer

def task_6():
    vsego = 36
    new = randint(20, 30)  # предположим, что у нас 20-30 новых карт
    old = vsego - new
    need = 2  # так как вынимают 2 карты
    text = f"6. В колоде находятся {new} новых и {old} израсходованные карты. Наугад вынимают 2 карты. Найти вероятность того, что второй вынутая карты окажется королем, если первой появилась дама.\n"
    
    total_ways = comb(vsego, need)  # всего способов вытянуть 2 карты из колоды
    ways_to_get_queen_first = comb(new, 1) * comb(old, 1)  # способы, которыми первой может быть дама и второй - король
    probability = ways_to_get_queen_first / total_ways  # вероятность

    answer = f"6. Вероятность того, что второй вынутая карты окажется королем, если первой появилась дама: {round(probability, 5)}\n"
    return text, answer

def task_7():
    f1 = randint(6, 9) / 10
    f2 = randint(6, 9) / 10
    f3 = randint(6, 9) / 10
    text = f"7. Половина выпускников лицея бизнеса и информационных технологий становятся абитуриентами Института менеджмента и экономики (ИМЭК), третья часть подает документы на факультеты Университета путей сообщения (ОмГУПС), остальные пытаются поступить в другие вузы России. Вероятность поступления для абитуриентов ИМЭК равна {f1}, для поступающих в ОмГУПС — {f2}, в
другие вузы — {f3}. Какова вероятность того, что выпускник лицея Вася продолжит свое образование в высшем
учебном заведении?\n"
    otv = 0.25 * f1 + 0.5 * f2 + 0.25 * f3
    answer = f"7. Вероятность того, что выпускник лицея Вася продолжит свое образование в высшем учебном заведении : {round(otv, 4)}\n"

    return text, answer

def task_8():
    mercedes = randint(3, 6) / 10
    zhiguli = mercedes / 1.5
    tavriya = 1 - zhiguli - mercedes
    p_expulsion_mercedes = randint(4, 7) / 10
    p_expulsion_zhiguli = p_expulsion_mercedes / 5
    p_expulsion_tavriya = 1 - p_expulsion_zhiguli - p_expulsion_mercedes

    text = f"8. Сотрудник ГИБДД останавливает «Мерседес» с вероятностью {mercedes}, " \
           f"«Жигули» — {zhiguli} и «Таврию» — {tavriya}. " \
           f"Водителя «Мерседеса» удается оштрафовать с вероятностью {p_expulsion_mercedes}, " \
           f"Водителя «Жигулей» — {p_expulsion_zhiguli}, «Таврии» — {p_expulsion_tavriya}. " \
           "Счастливый водитель первой встретившейся вам машины сообщил, что ему удалось избежать штрафа. " \
           "Водителем какой машины вероятнее всего он был?\n"

    p_expulsion = mercedes * p_expulsion_mercedes + zhiguli * p_expulsion_zhiguli + tavriya * p_expulsion_tavriya
    p_stay = 1 - p_expulsion

    max_probability = max(p_expulsion_mercedes, p_expulsion_zhiguli, p_expulsion_tavriya)
    answer = f"8. Водителем какой машины вероятнее всего он был: "
    if max_probability == p_expulsion_mercedes:
        answer += f"{round(max_probability, 4)} Mercedes\n"
    elif max_probability == p_expulsion_zhiguli:
        answer += f"{round(max_probability, 4)} Zhiguli\n"
    else:
        answer += f"{round(max_probability, 4)} Tavriya\n"

    return text, answer

def задача_9():
    p_wrong = randint(2, 8) / 10
    p_sucsess = round(1 - p_wrong, 2)
    kolv_prib = randint(6, 12)
    kolv_wrong = randint(1, kolv_prib - 2)
   kolv_sucsess = kolv_prib - kolv_wrong
    text = f"9. Вероятность отказа каждого прибора при испытании не зависит от отказов остальных приборов и равна {kolv_wrong}. " \
           f"Испытано {kolv_prib} приборов. Найти вероятность того, что {kolv_wrong} из них отказали. " \
           f"Вероятность того, что любой из приборов откажет, равна {p_wrong}.\n"
    p_itog = comb(kolv_prib, kolv_wrong) * pow(p_wrong, kolv_wrong) * pow(p_sucsess, kolv_sucsess)
    answer = f"9. Вероятность того, что {kolv_wrong} из них отказали: {round(p_itog, 4)}\n"
    return text, answer

def task_10():
    p = randint(5, 9) / 10
    n = randint(100, 150)
    k = randint(50, 70)
    skail = randint(10, 20)

    text = f"10. Вероятность появления события в некотором опыте равна {p}." \
                   f"Какова вероятность того, что это событие наступит " \
                   f"а) в большинстве из {n} опытов;\n" \
                   f"б) в половине опытов из {n}?\n"

    x = (k - n * p) / (n * p* (1 - p))
    y = (k + skail - n * p) / (n * p * (1 - p))
    otvet_a = local_lapl(x)
    otvet_b = round(integr_lapl(round(y, 2)) - integr_lapl(round(x, 2)), 5)

    answer += f"a) {otvet_a}\nб) {otvet_b}\n"
    return text, answer

def task_11():
    vsego = randint(100, 200)  # общее количество изделий
    p = randint(1, 9)/100 # вероятность брака
    k = randint(3, 9)# количество бракованных изделий

    text = f"11. Завод отправил на базу {vsego} изделий. Вероятность брака составляет {p}. Найдите вероятность того, что бракованными окажется более {k} изделий.\n"

    # Используем биномиальное распределение для вычисления вероятности
    itogver = 1 - sum(combination(vsego, i) * (p ** i) * ((1 - p) ** (vsego - i)) for i in range(k))

    answer += f"{itogver}\n"

    return text, answer

def задача_12():
    n = randint(1000, 3000)
    n1 = randint(1, 3)  # количество выигрышей в 2000 руб.
    n2 = randint(1, 4)  # количество выигрышей в 1000 руб.
    n3 = randint(1, 5)   # количество выигрышей в 500 руб.
    n4 = randint(1, 10)# количество выигрышей в 100 руб.
    
    p1 = n1 /n  # вероятность выигрыша в 2000 руб.
    p2 = n2 /n  # вероятность выигрыша в 1000 руб.
    p3 = n3 /n  # вероятность выигрыша в 500 руб.
    p4 = n4 /n  # вероятность выигрыша в 100 руб.
    
    text = f"12. В денежной лотерее выпущено {n} билетов. Разыгрывается (int{n1}) выигрыш в 2000 руб., (int{n2}) — по 1000 руб., (int{n3}) — по 500 руб. и (int{n4}) выигрышей — по 100 руб. Составить ряд распределения стоимости выигрыша для владельца одного лотерейного билета. Найти М(Х), D(X), (X), F(X) этой случайной величины.\n"
    
    M = p1 * 2000 + p2 * 1000 + p3 * 500 + p4 * 100  # математическое ожидание
    D = p1 * (2000 - M) ** 2 + p2 * (1000 - M) ** 2 + p3 * (500 - M) ** 2 + p4 * (100 - M) ** 2  # дисперсия
    S = D ** 0.5  # стандартное отклонение
    
    answer = f'M(X) = {M}\nD(X) = {D}\nσ = {S}\n'
    
    answer += "F(x):\n"
    answer += f"\t| 0, x<=0\n"
    answer += f"\t| {p4}, 0<x<=100\n"
    answer += f"\t| {p4 + p3}, 100<x<=600\n"
    answer += f"\t| {p4 + p3 + p2}, 600<x<=1600\n"
    answer += f"\t| 1, 1600<x\n"
    
    return text, answer

def task_13():
    p = randint(1, 9)/10 # вероятность брака детали
    q = round(1 - p, 2)  # вероятность небрака
    n = randint(10, 20)  # количество изготовленных деталей

    text = f"Станок-автомат штампует детали. Вероятность того, что деталь окажется бракованной, равна {p}. " \
           f"Составить ряд распределения числа бракованных деталей среди {n} изготовленных. " \
           "Найти M(X) и D(X) этой случайной величины.\n"

    answer = "X|\t"
    for i in range(0, n + 1):
        answer += f"{i}\t\t\t|\t\t\t\t"
    answer += f"... |\t\t{n}\nP|\t"
    answer += f"{q}^{n}\t"
    for i in range(1, n + 1):
        answer += f"\t|{combination(n, i)[2]}*{p}^{i}*{q}^{n - i}"
    answer += f" |\t\t\t\t... |\t{p}^{n}\t\n\n"

    M = n * p  # математическое ожидание
    D = n * p * q  # дисперсия

    answer += f"M(X) = {round(M, 3)}\nD(X) = {round(D, 5)}\n"

    return text, answer

def task_14():
    p = randint(1, 5) / 100  # вероятность сброшюрования книги неправильно
    q = round(1 - p, 2)  # вероятность правильного сброшюрования
    n = randint(20, 40) * 1000  # количество изданных книг

    text = f"Книга издана тиражом {n} экземпляров. Вероятность того, что книга сброшюрована неправильно, равна {p}. " \
           f"Составить ряд распределения числа книг, сброшюрованных неправильно. Найти M(X) этой случайной величины.\n"

    answer = "X|\t"
    for i in range(0, n + 1):
        answer += f"{i}\t\t\t|\t\t\t\t\t"
    answer += f"... |\t\t{n}\nP|\t"
    answer += f"{q}^{n}\t"
    for i in range(1, n + 1):
        answer += f"|{combination(n, i)[2]}*{p}^{i}*{q}^{n - i} "
    answer += f" |\t\t\t\t\t... |\t\t{p}^{n}\t\n\n"

    M = n * p  # математическое ожидание

    answer += f"M(X)={round(M, 5)}\n"

    return text, answer

 def task_15(): #простите парни я тупой нихуя не понятно циферки какие то букавки 

def task_18():
    sigma = randint(20,30)  # сигма случайных ошибок взвешивания
    error_limit = randint(5,15) # предельная ошибка взвешивания

    text = f"Производится взвешивание некоторого вещества без систематических ошибок. " \
           f"Случайные ошибки взвешивания подчинены нормальному закону с сигма = 20 г. " \
           f"Найти вероятность того, что очередное взвешивание будет произведено с ошибкой, " \
           f"не превосходящей по абсолютной величине {error_limit} г.\n"

    # Используем функцию интеграла Лапласа для вычисления вероятности
    probability = round(0.5 - float(integr_lapl(round(error_limit / sigma, 2))), 5)

    answer = f"P = {probability}"

    return text, answer
