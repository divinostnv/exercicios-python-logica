palavras= ('Tatu', 'Cebola', 'Calça', 'Sofia', 'Par', 'Coitado', 'Semente')
Vogal= ('aeiouAEIOU')
social=0
off=0
cont=0
repitida=0
for social in palavras:
    vogais= Vogal.count(social)
    print(f'\nNa palavra {social} tem', end=' ')
    for off in Vogal:
        if off in social:
            print(off, end=' ')
            repitida= social.count(off)
            while repitida>1:
                print(off, end=' ')
                repitida-=1