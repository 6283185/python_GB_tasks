# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.


names = ['Alex', 'Steve', "Mia"]
salaries = [12000, 8000, 15000]
bonus = ['10.0%', '7.25%', '5%']


def dict_summ_prize_and_bet(name, bet, interest):
    dict_func = {}
    for name_key, bet, prize in zip(name, bet, interest):
        dict_func[name_key] = bet + ((bet / 100) * (float(prize.replace("%", ""))))
    return dict_func


res = dict_summ_prize_and_bet(names, salaries, bonus)
print(res)
