def find_max_value(dict):
    a = ""
    max_val = None
    for key, value in dict.items():
        if max_val is None or value > max_val:
            max_val = value
            a = key
    return a


def reverse_dict(dict):
    reverse_dict = dict()
    for key,value in dict.items():
        reverse_dict[value] = key
    return reverse_dict

def word_freq_counter(words):
    
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def find_biggest_expense(dict):
    max_avg = 0
    max_expense = ''
    
    for category, costs in dict.items():
        if costs:
            average = sum(costs) / len(costs)
            if average > max_avg:
                max_avg = average
                max_expense = category
                
    return max_expense


def sum_of_expenses(expenses):
    expenses = dict ()
    for categoria,costos in expenses.items():
        suma = 0
        for numeros in costos:
            suma += numeros 
        expenses [categoria] = suma
    return expenses



def sum_of_expenses_by_type(expenses):
    res = {}
    for category, costs in expenses.items():
        for item_type, amount in costs:
            if item_type in res:
                res[item_type] += amount 
            else:
                res[item_type] = amount
    return res
