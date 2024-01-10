# import trsfile


# with trsfile.open('TSGoods.trs', 'r') as traces:
# # Show all headers
#     for header, value in traces.get_headers().items():
#         print(header, '=', value)
# print()

# with open('TSGoods.trs', 'r', encoding='utf-8') as f:
#     f.read()
#     print(f.read())
#     f.close()


file = 'C:/Users/2021/Desktop/site/TSGoods.trs'
f = open(file, 'r', encoding='utf-8')
x = f.readlines()
for line in x:
    splitted_line = line.split(';')
    article = splitted_line[0].replace('"', '')
    country = splitted_line[6].replace('"', '')
    season = splitted_line[8].replace('"', '')
    category = splitted_line[1].replace('"', '')
    try:
        subcategory =  splitted_line[1].replace('"', '').split(',')[1]
    except IndexError as e:
        subcategory =  None
    material = splitted_line[4].replace('"', '')
    try:
        color = splitted_line[5].split(',')[0].split(' ')[1]
    except IndexError as e:
        color = ''
    size = splitted_line[5].split()[-1].replace('"', '')
    price = splitted_line[-1]


    print('Артикул:', splitted_line[0].replace('"', ''))
    print('Страна: ', splitted_line[6])
    print('Сезон:', splitted_line[8].replace('"', ''))
    print('Категория:', splitted_line[1].replace('"', '').split(',')[0])
    try:
        subcategory =  splitted_line[1].replace('"', '').split(',')[1]
        print(subcategory)
    except IndexError as e:
        subcategory =  None
        print(subcategory)
    
    print('Материал:', splitted_line[4].replace('"', ''))
    try:
        print('Цвет:', splitted_line[5].split(',')[0].split(' ')[1])
    except IndexError as e:
        print('Цвет: Не указан')
    print('Размер: ', splitted_line[5].split()[-1].replace('"', ''))
    print('Цена: ' + str(splitted_line[-1]), '\n')

    
    print(splitted_line)
    
# splitted_line = x[1].split(';')
# print(splitted_line)
