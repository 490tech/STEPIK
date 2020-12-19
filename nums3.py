


inp = list(input())
word = ('тысяч', 'сотен', 'десятков', 'единиц')                                   
[print('Цифра в позиции', word[i], 'равна', inp[i]) for i in range(len(word))]   
