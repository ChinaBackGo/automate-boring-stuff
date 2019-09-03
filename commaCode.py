#output: 'apples, bananas, tofu, and cats'

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(list_param):
    comma_string = ''
    for i in range(len(list_param)-1):
        comma_string = comma_string + list_param[i] + ', '
    comma_string = comma_string + 'and ' + list_param[-1]
    return comma_string

print(comma_code(spam))
