palavras = ('aprender', 'programar', 'linguagem', 'python','curso','gratis', 'estudar', 'praticar',
            'trabalhar','mercado','programador', 'futuro')
print(palavras)
for word in palavras:
    print(f'\nNa palavra {word.upper()} temos ',end='')
    for vowel in word:
        if vowel in 'aeiou':
            print(vowel.lower(), end=' ')