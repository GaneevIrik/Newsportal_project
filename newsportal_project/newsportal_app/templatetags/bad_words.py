from django import template

register = template.Library()

black_list_word = ['who', 'рыбок',]


@register.filter()
def censor(value):
    for word in black_list_word:
       if word.lower() in black_list_word:
            value = value.replace(word[1:], '*' * (len(word) - 1))


    return value