#В строке заменить все Е на число 3

string = 'Ботнет IPStorm, в который ранее входили лишь Windows - машины, увеличился до 13500 зараженных систем'.replace('e','3')
print(string.replace('е','3'))



#создать приложение, где одна часть предложения написана в маленьком регистре, а вторая в большом

b = string[0: len(string)//2].lower()
c = string[len(string)//2: len(string)].upper()
print(b+c)

#сделать из Булева значения True - строку