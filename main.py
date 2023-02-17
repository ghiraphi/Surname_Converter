#программа добавляет регулякри к фамилиям, учитывая окончания
from itertools import permutations
import re
import difflib
import codecs
original_file= "files/fiodo1.txt"
def zapusk(original_file):
    #открываем исходный файл с ФИО
    file = codecs.open( original_file, "r", "utf-8" )
    data = file.read()
    file .close()

    #в новый список добавляются фамилии-имена, ковертированные в регулярки на основе популярных мужских окончаний фамилий
    dict=[]
    for fio in data.split('\n'):

        surname=fio.split()[0]
        surname=surname+'1'
        if len(surname)>=5:
            surname=surname.replace('ова1', 'ов([ау]|ой)').replace('ов1', 'ов([ауе]|ым)?').replace('ева1', 'ев([ау]|ой)').replace('ев1', 'ев([ауе]|ым)?').replace('ёва1', 'ев([ау]|ой)').replace('ёв1', 'ев([ауе]|ым)?').replace('ин1', 'ин([ауе]|ым)?').replace('ина1', 'ин([ау]|ой)').replace('ын1', 'ин([ауе]|ым)?').replace('ына1', 'ин([ау]|ой)').replace('ый1', '(ый|ого|ому?)').replace('ая1', '(ая|ой|ую)').replace('ий1', '(ий|ого|ому?)').replace('ий1', '(ий|ого|ому?)')
            dict.append(surname+' '+fio.split()[1])
        else:
            dict.append(surname+' '+fio.split()[1])

    #открываем список основных мужских имен
    print(len(dict), 'количество исходных фамилий')
    name_list=[]
    file = codecs.open("files/name1.txt", "r", "utf-8")
    name_file = file.read()
    file .close()
    for name in name_file.split():
        name_list.append(name)
    name_list=' '.join(name_list)

    #открываем список основных мужских имен, меняем на регулярки редкие окончания
    dict2=[]
    for surname in dict:

        #print(surname, '***случаи')
        if re.search('\(', surname.split()[0])==None and re.search('ко1', surname.split()[0])==None and len(surname.split()[0])>=5:
            if re.search(surname.split()[1], name_list):
                if re.search('[ауоыеиюя][бвгджзклмнпрстфхцчш]1', surname.split()[0]):
                    newsurname = surname.split()[0].replace('1', '([ауе]|[ое]м)?')
                    newfio = newsurname + ' ' + surname.split()[1]
                    #print(newfio, 'первый случай')
                    dict2.append(newfio)
                    continue

                if re.search('[бвгджзклмнпрстфхцш]ь1', surname.split()[0]):
                    newsurname = surname.split()[0].replace('ь1', '([ьяюе]|[ое]м)')
                    newfio = newsurname + ' ' + surname.split()[1]
                    #print(newfio, 'второй случай')
                    dict2.append(newfio)
                    continue

                if re.search('[бвгджзклмнпрстфхцш]а1', surname.split()[0]):
                    newsurname = surname.split()[0].replace('а1', '([ауе]|[ое]й)')
                    newfio = newsurname + ' ' + surname.split()[1]
                    #print(newfio, 'третий случай')
                    dict2.append(newfio)
                    continue

                if re.search('[бвгджзйклмнпрстфхцшь][бвгджзклмнпрстфхцш]1', surname.split()[0]):
                    newsurname = surname.split()[0].replace('1', '([ауе]|[ое]м)?')
                    newfio = newsurname + ' ' + surname.split()[1]
                    #print(newfio, 'четвертый случай')
                    dict2.append(newfio)
                    continue

                if re.search('[ауоыеиюя]й1', surname.split()[0]):
                    newsurname = surname.split()[0].replace('й1', '([йяюе]|[ое]м)')
                    newfio = newsurname + ' ' + surname.split()[1]
                    #print(newfio, 'пятый случай')
                    dict2.append(newfio)
                    continue

                if re.search('[бвгджзклмнпрстфхцш]я1', surname.split()[0]):
                    newsurname = surname.split()[0].replace('я1', '([яюеи]|[ое]й)')
                    newfio = newsurname + ' ' + surname.split()[1]
                    #print(newfio, 'шестой случай')
                    dict2.append(newfio)
                    continue

                else:
                    dict2.append(surname.split()[0] + ' ' + surname.split()[1])

            else:
                dict2.append(surname.split()[0] + ' ' + surname.split()[1])
                #print(surname.split()[0] + ' ' + surname.split()[1], 'четвертый случай')

        else:
            dict2.append(surname.split()[0] + ' ' + surname.split()[1])
            #print(surname.split()[0] + ' ' + surname.split()[1], 'пятый случай')

    print(dict2[:100], '-образец получившихся регулярок')
    print(len(dict2), 'длина второго словаря')

    count=0
    print('=== Далее список строк, которые остались без регулярко. Либо программа не узнала редкое мужское имя, '
          'либо строка короткая и нужно решить - стоит ли вообще добавлять такую строку тем более её менять ===')
    for surname in dict2:
        if re.search('\(', surname.split()[0])==None and re.search('о1', surname.split()[0])==None and re.search('е1', surname.split()[0])==None and re.search('ли1', surname.split()[0])==None and re.search('ы1', surname.split()[0])==None and re.search('о1', surname.split()[0])==None and re.search('и1', surname.split()[0])==None and re.search('о1', surname.split()[0])==None and re.search('у1', surname.split()[0])==None and re.search('я', surname[len(surname)-1])==None and re.search('а', surname[len(surname)-1])==None:
            #if re.search(surname.split()[1], name_list):
            surname = surname.replace('1', '')
            print(surname)
            count+=1
    print(count, 'количество элементов не вошедших')

    file_for_record = open('files/surname_regular.txt', 'w', encoding="utf-8")
    for newlinerec in dict2:
        try:
            newlinerec=newlinerec.replace('1','')
            file_for_record.write(str(newlinerec + '\n'))
        except UnicodeEncodeError:
            pass
    file_for_record.close()

    # сравнение фамилий с общеупотребительной лексикой. Возможно, некоторые фамилии придётся удалить
    file = codecs.open("files/popwords.txt", "r", "utf-8")
    dataother = file.read()
    file .close()
    def similarity(s1, s2):
      normalized1 = s1.lower()
      normalized2 = s2.lower()
      matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
      return matcher.ratio()
    dict_compare=[]
    count_notunic=0

    print('Идёт сравнение фамилий с общеупотребительной лексикой. Возможно, некоторые фамилии придётся удалить')
    for indexwordfile, word_file in enumerate(dataother.split()):
        print(indexwordfile, len(dataother.split()) )
        for word_dict in data.split('\n'):
            newworddict=word_dict.split()[0]
            if similarity(word_file, newworddict)>0.95:
                count_notunic+=1
                print(newworddict+' '+word_dict.split()[1], '--',word_file)
    print(count_notunic, 'количество фамилий, схожих с обычными словами')

    #программа убирает дубли фамилий, учитывая пол
    def repreg(base_line):
        counter_num_orig_line = 0
        new_list_for_line = []
        global substring
        counter_num_orig_line += 1
        # программа меняет регулярки на спецсимволы. на входе строка с регуляркой. на выходе список строк без регулярок, на входе a - '(под|пере)жар* картошку' - на выходе a - ['поджар* картошку', 'пережар* картошку']
        base_line = base_line.replace('[а-я]', '.').replace('[a-z]', '.').replace('[а-яa-z]', '.').replace('[a-zа-я]', '.').replace('[^а-я]', '£').replace('[1-9]', '£').replace('[0-9]', '£').replace('+', '*').replace('&#091', '©091').replace('&#093', '©093').replace('&#092', '©092').replace('&#047', '©047').replace('&#094', '©094').replace('&#036', '©036').replace('&#046', '©046').replace(
            '&#124', '©124').replace('&#063', '©063').replace('&#042', '©042').replace('&#043', '©043').replace('&#040', '©040').replace('&#041', '©041').replace('&#123', '©123').replace('&#125', '©125').replace('&#821', '©821').replace('&#061', '©061').replace('&#182', '©182')  # замена регулярок на звёздочки и точки
        # программа раскрывает квадратные скобки по выбранному диапозону. (0|1|2|3) вместо [0-3]
        p1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        p2 = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        if re.fullmatch('.*\[\w\-\w\].*', base_line):
            num = len(re.findall('\[\w\-\w\]', base_line))  # количество квадратных скобок с '-'
            for i in range(num):  # замена квадратных скобко и букв на варианты круглых скобок
                dl = len(base_line)  # количество букв в элементе
                for k in range(dl):  # в диапозоне количества букв
                    if base_line[k] == '[' and base_line[k + 2] == '-':
                        if base_line[k + 1] in p1:
                            s_o = p1.index(base_line[k + 1])
                        if base_line[k + 1] in p2:
                            s_o = p2.index(base_line[k + 1])
                        start = k  # начальная позиция квадратной скобки
                    if base_line[k] == ']' and base_line[k - 2] == '-':
                        if base_line[k - 1] in p1:
                            s_f = p1.index(base_line[k - 1])
                        if base_line[k - 1] in p2:
                            s_f = p2.index(base_line[k - 1])
                        end = k  # финальная позиция квадратной скобки
                        break
                if base_line[k - 1] in p1:  # если это цифра
                    p = '|'.join(p1[s_o:s_f + 1])  # добавляем в указанное перечисление цифр этой скобки слэши
                if base_line[k - 1] in p2:  # если это буква
                    p = '|'.join(p2[s_o:s_f + 1])  # добавляем в указанное перечисление букв  этой скобки слэши
                base_line = base_line[:start] + '(' + p + ')' + base_line[end + 1:]  # преобразовываем квадратные скобки в круглые. становится основным выражением.
                # дальше по кругу

        # программа рабоатет с выражением [^x], раскрывает и выдаёт полную скобку за исключением символа x
        if re.findall('.*\[\^.*', base_line):
            p0 = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы',
                  'ь', 'э', 'ю', 'я', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # символы, которые используются в [^x]
            y = 0
            num = len(re.findall('\^', base_line))  # количество квадратных скобок с '^'
            base_line = base_line.split(' ', 0)  # сделай из изначальной строки список с одним элементом
            schetchik = 0
            for s in base_line:
                dl = len(s)  # количество букв в элементе
                for k in range(dl):  # в диапозоне количества букв
                    if s[k] == '^' and y == 0:  # высчитывает, откуда начинается скобка и где заканчивается
                        start = k + 1
                        y = y + 1
                    if s[k] == ']' and y == 1:
                        end = k
                        y = y - 1
                        break
                x = s[int(start):int(end)]  # все буквы-цифры , которые не должны учитываться
                vrem = []
                for i in x:  # перебирает все символы в скобке
                    isk = p0.index(i)  # находит индекс в списке, чтобы потом исключить его
                    p = p0[:isk] + p0[isk + 1:]  # собирает скобку без учёта указанных символов
                    vrem.append(p)  # добавляет во временный список
                vrem = '(' + '|'.join(list(set.intersection(*map(set, vrem)))) + ')'  # собирает готовую скобку
                s = s[:start - 2] + vrem + s[end + 1:]  # собирает готовое выражение, строку
                base_line.append(s)  # добавляет в текущий список
                schetchik = schetchik + 1
                if schetchik != num:  # прекращает работать, если проверил все значения
                    continue
                else:
                    break
            base_line = [i for i in base_line if '^' not in i]  # выбирает значения только без ^
            base_line = ''.join(base_line)

        # программа заменяет квадратные скобки и буквы в них на варианты круглых скобок
        #base_line = re.sub(' \d,\d+ ', ' ', base_line)  # убираем расстояния, делаем так, будто их не было
        base_line = base_line.replace(',', '®')
        num = len(re.findall('\[', base_line))  # количество квадратных скобок
        num2 = len(re.findall('\[\^', base_line))  # количество квадратных скобок исключений
        num = num - num2  # вычитаем разницу, чтобы считать нужное число вариантов
        r = 0
        for i in range(num):  # замена квадратных скобко и букв на варианты круглых скобок
            dl = len(base_line)  # количество букв в элементе
            for k in range(dl):  # в диапозоне количества букв
                if base_line[k] == '[' and base_line[k + 2] != '-' and base_line[k + 1] != '^':
                    start = k  # начальная позиция квадратной скобки
                    r = r + 1
                if base_line[k] == '[' and base_line[k + 1] == '^':
                    continue
                if base_line[k] == '[' and base_line[k + 2] == '-':
                    continue
                if base_line[k] == ']' and base_line[k - 2] != '-' and r == 1:
                    end = k  # финальная позиция квадратной скобки
                    r = r - 1
                    break
            p = base_line[start + 1:end]  # участок квадратной скобки
            p = '|'.join(p)  # добавляем между буквами в этой скобки слэши
            base_line = base_line[:start] + '(' + p + ')' + base_line[end + 1:]  # преобразовываем квадратные скобки в круглые. становится основным выражением.  дальше по кругу


        # программа раскрывает фигурные скобки и даёт все значения согласно {x}
        base_line = base_line.split(' ', 0)  # сделай из изначальной строки список с одним элементом
        for str_ss in base_line:  # итерация по списку строк
            if '{' in str_ss:  # если в строке есть круглая скобка
                for kes in range(len(str_ss)):  # пройдись по каждому элементу строки. по каждой букве
                    if str_ss[kes] == '{':  # если есть открыв.скобка
                        t1 = kes  # назначь индекс этой скобке
                    if str_ss[kes] == '}':  # если есть открыв.скобка
                        t2 = kes  # назначь индекс этой скобке
                        if re.search('®', str_ss[t1 + 1:t2]):  # в этих круглых скобках есть диапозон?
                            start_finish = str_ss[t1 + 1:t2].split('®')
                            start_f1 = round(float(start_finish[0]))
                            finish_f1 = round(float(start_finish[1]))
                            len_sumok = finish_f1 - start_f1  # знай сколько вариантов в диапазоне
                        else:
                            start_finish = [(str_ss[t1 + 1:t2]), (str_ss[t1 + 1:t2])]
                            start_f1 = round(float(start_finish[0]))
                            finish_f1 = round(float(start_finish[1]))
                        break
                nvs = []  # временный список для добавления новых значений
                for dnkz in range(start_f1, (finish_f1) + 1):  # в диапозоне начального и конечного значения
                    if str_ss[t1 - 1] != ')' and str_ss[t1 - 1] != ']':
                        nvs.append(str_ss[:t1 - 1] + str_ss[t1 - 1] * dnkz + str_ss[t2 + 1:])  # добавь в новый список строки с учётом количества {
                    if str_ss[t1 - 1] == ')':
                        for index, bukva in reversed(list(enumerate(str_ss[:t1]))):
                            if bukva == '(':
                                nvs.append(str_ss[:index] + str_ss[index:t1] * dnkz + str_ss[t2 + 1:])
                                break
                    if str_ss[t1 - 1] == ']':
                        for index, bukva in reversed(list(enumerate(str_ss[:t1]))):
                            if bukva == '[':
                                nvs.append(str_ss[:index] + str_ss[index:t1] * dnkz + str_ss[t2 + 1:])
                                break
                [base_line.append(nvs_i) for nvs_i in nvs]  # добавь новые значения из временного в основной список
        base_line = [ai for ai in base_line if '{' not in ai]

        # программа убирает лишние скобки, которые не имели нагрузки
        for substring in base_line:
            substring = list(substring)  # строка меняется на элемент списка
            kn = len(substring)  # количество строк в списке
            predel = 0
            # определяет, где начинается старт и финиш - маскируя внутренние скобки со слешами, убирая пустые скобки , где нет слеша или знака вопрсоа
            while '(' in substring or ')' in substring or '|' in substring:  # пока есть слэши и скобки в списке
                predel += 1
                for k in range(0, kn):  # итерация по количеству букв в списке
                    if re.fullmatch('\(', substring[k]) and re.fullmatch('\)', substring[k + 1]):  # если в строке есть скобка откр и закр ()
                        start = k  # фиксация начала
                        finish = k + 1  # фиксация конца
                        break
                    if re.fullmatch('\(', substring[k]) and re.fullmatch('(\w|©|®|£|\{|\}|\%|\=|\?|@|<|\-|\*|\[|\]|\+|\.|#)', substring[k + 1]):  # если в строке скобка откр и дальше буква
                        start = k  # фиксация начала
                        continue
                    if re.fullmatch('\)', substring[k]) and re.fullmatch('(\w|©|®|£|\{|\}|\%|\=|\?|@|>|\-|\*|\[|\]|\?|\+|\.|#)', substring[k - 1]):  # если в строке скобка закр  и перед этим буква
                        finish = k  # фиксация конца
                        break  # останавливай цикл, переходи к след
                dlskob = len(''.join(substring[start + 1:finish]))
                try:
                    if '|' not in substring[start + 1:finish] and '(' not in substring[start + 1:finish] and ')' not in substring[start + 1:finish] and finish != dlskob + 1:  # если нет слэша внутри скобок , тогда
                        if '?' not in substring[finish + 1]:
                            substring[start] = '@'  # меняй скобки начала и конца на знак
                            substring[finish] = '@'
                    if '|' not in substring[start + 1:finish] and '(' not in substring[start + 1:finish] and ')' not in substring[start + 1:finish] and '?' not in substring[finish] and finish == dlskob + 1:  # если нет слэша внутри скобок , тогда
                        substring[start] = '@'  # меняй скобки начала и конца на знак
                        substring[finish] = '@'
                    if '|' not in substring[start + 1:finish] and '(' not in substring[start + 1:finish] and ')' not in substring[start + 1:finish] and '?' in substring[finish + 1] and dlskob >= 2:  # если нет слэша внутри скобок , тогда
                        substring[start] = '<'  # меняй скобки начала и конца на знак
                        substring[finish] = '>'
                    if '|' not in substring[start + 1:finish] and '(' not in substring[start + 1:finish] and ')' not in substring[start + 1:finish] and '?' in substring[finish + 1] and dlskob == 1:  # если нет слэша внутри скобок , тогда
                        substring[start] = '@'  # меняй скобки начала и конца на знак
                        substring[finish] = '@'
                    if '|' in substring[start + 1:finish]:  # если слэш между скобок
                        substring[start] = '<'  # меняй скобки начала и конца на знак
                        substring[finish] = '>'
                        spisok = []  # создай пустой список
                        for k, i in enumerate(substring[start + 1:finish]):  # итерация по внутренности скобки
                            if i == '|':  # есть если слэш
                                spisok.append(k)  # добавь в список индекс этого слэша
                        for i in range(len(spisok)):  # итерация по индексам слэшей
                            substring[start + 1 + spisok[i]] = '&'  # меняй слэш на знак, учитывая расстояние (индекс)
                except IndexError:
                    if '|' not in substring[start + 1:finish] and '(' not in substring[start + 1:finish] and ')' not in substring[start + 1:finish] and finish != dlskob + 1:  # если нет слэша внутри скобок , тогда
                        substring[start] = '@'  # меняй скобки начала и конца на знак
                        substring[finish] = '@'
                    if '|' not in substring[start + 1:finish] and '(' not in substring[start + 1:finish] and ')' not in substring[start + 1:finish] and '?' not in substring[finish] and finish == dlskob + 1:  # если нет слэша внутри скобок , тогда
                        substring[start] = '@'  # меняй скобки начала и конца на знак
                        substring[finish] = '@'
                    if '|' in substring[start + 1:finish]:  # если слэш между скобок
                        substring[start] = '<'  # меняй скобки начала и конца на знак
                        substring[finish] = '>'
                        spisok = []  # создай пустой список
                        for k, i in enumerate(substring[start + 1:finish]):  # итерация по внутренности скобки
                            if i == '|':  # есть если слэш
                                spisok.append(k)  # добавь в список индекс этого слэша
                        for i in range(len(spisok)):  # итерация по индексам слэшей
                            substring[start + 1 + spisok[i]] = '&'  # меняй слэш на знак, учитывая расстояние (индекс)
                if predel > 100:
                    substring = (''.join([k for k in substring]))  # подготавливаем из списка строку
                    substring = list(substring.replace('@|@', '|').replace(' @', ' (').replace('@ ', ') '))
                    if substring[0] == '@':
                        substring[0] = '('
                    if substring[len(substring) - 1] == '@':
                        substring[len(substring) - 1] = ')'

        base_line = (''.join([k for k in substring if k != '@']))  # верни строку, не замечая знак @ - пустые скобки
        f = base_line.replace('<', '(').replace('>', ')').replace('&', '|')
        f = f.split(maxsplit=0)

        # программа раскрывает скобки со знаком '?' и делает все возможные варианты
        for x, i in enumerate(f):  # иетарция по элементам списка, где есть знак вопроса, так мы находим скобки , после которых стоит знак вопроса. означает - или да или нет.
            if ')?' in i:
                i = list(i)  # преобразуем строку в список. чтобы была итерация по буквам этой строки
                for k in range(len(i)):  # итерация по количеству букв в списке
                    if re.fullmatch('\(', i[k]) and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|@|<|\-|\*|\[|\]|\.|\+|\|)', i[k + 1]):  # если в строке скобка
                        start = k  # фиксация начала скобки со знаком вопроса
                        continue
                    if re.fullmatch('\(', i[k]) and re.fullmatch('\)', i[k + 1]) and re.fullmatch('\?', i[k + 2]):  # если есть выражение вида ()?, то сразу преобраует в спец символы, чтобы потом убирать эту строку
                        f[x] = '#$'
                        break
                    try:
                        if re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|\?|\.|@|&|<|>|\-|\*|\[|\]|\.|\+|\||\.)', i[k - 1]) and re.fullmatch('\)', i[k]) and re.fullmatch('(\|)', i[k + 1]):  # если есть выражение вида -   текст)|
                            i[k] = '>'  # преобразовывает в спец символ ближнюю скобку и слэши внутри, замораживая, чтобы программа думала, что это буквы и не обращала внимание на скобки и слэши
                            i[start] = '<'
                            otrezok = i[start + 1:k]
                            if '|' in otrezok:  # работа по заморозке слешей внутри скобки
                                spisok = []
                                for r in range(len(otrezok)):
                                    if otrezok[r] == '|':
                                        spisok.append(r)
                                for y in range(len(spisok)):  # итерация по индексам слэшей
                                    i[start + 1 + spisok[y]] = '&'  # меняй слэш на знак, учитывая расстояние (индекс)
                            f.append(''.join(i))
                            f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                            break
                        if re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|\?|\.|@|&|<|>|\-|\*|\[|\]|\.|\+|\||\.)', i[k - 1]) and re.fullmatch('\)', i[k]) and re.fullmatch('\)', i[k + 1]) and re.fullmatch('\?', i[k + 2]):  # если есть выражение вида -  ( абв))?
                            i[k] = '>'  # преобразовывает в спец символ ближнюю скобку и слэши внутри, замораживая, чтобы программа думала, что это буквы и не обращала внимание на скобки и слэши
                            i[start] = '<'
                            otrezok = i[start + 1:k]
                            if '|' in otrezok:  # работа по заморозке слешей внутри скобки
                                spisok = []
                                for r in range(len(otrezok)):
                                    if otrezok[r] == '|':
                                        spisok.append(r)
                                for y in range(len(spisok)):  # итерация по индексам слэшей
                                    i[start + 1 + spisok[y]] = '&'  # меняй слэш на знак, учитывая расстояние (индекс)
                            f.append(''.join(i))
                            f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                            break
                        if re.fullmatch('(\|)', i[start - 1]) and re.fullmatch('\)', i[k]) and i[k + 1] != '?':  # если есть выражение вида -   текст)|
                            i[k] = '>'  # преобразовывает в спец символ ближнюю скобку и слэши внутри, замораживая, чтобы программа думала, что это буквы и не обращала внимание на скобки и слэши
                            i[start] = '<'
                            otrezok = i[start + 1:k]
                            if '|' in otrezok:  # работа по заморозке слешей внутри скобки
                                spisok = []
                                for r in range(len(otrezok)):
                                    if otrezok[r] == '|':
                                        spisok.append(r)
                                for y in range(len(spisok)):  # итерация по индексам слэшей
                                    i[start + 1 + spisok[y]] = '&'  # меняй слэш на знак, учитывая расстояние (индекс)
                            f.append(''.join(i))
                            f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                            break
                        if re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|\?|\.|@|&|<|>|\-|\*|\[|\]|\.|\+|\||\.)', i[k - 1]) and re.fullmatch('\)', i[k]) and re.fullmatch('(\w|©|®|£|\{|\}|\%|\.|@|&|<|>|\-|\*|\[|\]|\.|\+|\||\.)', i[k + 1]):  # !!! тут был прецедент. стоял знак вопроса. я его убрал.   если есть выражение вида -   текст))
                            i[k] = '>'
                            i[start] = '<'
                            otrezok = i[start + 1:k]
                            if '|' in otrezok:
                                spisok = []
                                for r in range(len(otrezok)):
                                    if otrezok[r] == '|':
                                        spisok.append(r)
                                for y in range(len(spisok)):  # итерация по индексам слэшей
                                    i[start + 1 + spisok[y]] = '&'  # меняй слэш на знак, учитывая расстояние (индекс)
                            f.append(''.join(i))
                            f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                            break

                        if i[0] == '(' and start == 1 and re.fullmatch('\)', i[k]) and i[k + 1] != '?':  # если есть выражение вида -   текст)|
                            i[k] = '>'  # преобразовывает в спец символ ближнюю скобку и слэши внутри, замораживая, чтобы программа думала, что это буквы и не обращала внимание на скобки и слэши
                            i[start] = '<'
                            otrezok = i[start + 1:k]
                            if '|' in otrezok:  # работа по заморозке слешей внутри скобки
                                spisok = []
                                for r in range(len(otrezok)):
                                    if otrezok[r] == '|':
                                        spisok.append(r)
                                for y in range(len(spisok)):  # итерация по индексам слэшей
                                    i[start + 1 + spisok[y]] = '&'  # меняй слэш на знак, учитывая расстояние (индекс)
                            f.append(''.join(i))
                            f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                            break
                        if re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|\?|\.|@|&|<|>|\-|\*|\[|\]|\.|\+|\||\.)', i[k - 1]) and re.fullmatch('\)', i[k]) and re.fullmatch('(\?)', i[k + 1]):  # если  выражение -   текст)? - дальше перечисляются все ситуации, чтобы раскрывать эти скобки
                            finish = k  # фиксация конца скобки со знаком вопроса
                            if ')' not in i[start + 1:finish] and '(' not in i[start + 1:finish]:
                                if '|' in i[start + 1:finish] and i[start - 1] != '|' and i[start - 1] != '(' and finish + 1 == len(i) - 1:  # 1.2.2.0
                                    f.append(''.join(i[:start] + i[start:finish + 1] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break
                                if '|' in i[start + 1:finish] and i[start - 1] != '|' and i[start - 1] != '(' and i[finish + 2] != ' ':  # 1.1.1.0
                                    f.append(''.join(i[:start] + i[start:finish + 1] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start] + i[finish + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break
                                if '|' in i[start + 1:finish] and i[start - 1] != '|' and i[start - 1] != '(' and i[finish + 2] == ' ':  # 1.2.2.0
                                    f.append(''.join(i[:start] + i[start:finish + 1] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start] + i[finish + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break

                                if '|' in i[start + 1:finish] and i[start - 1] != '|' and i[start - 1] == '(' and i[finish + 2] != '|':  # 1.1.1
                                    f.append(''.join(i[:start] + i[start:finish + 1] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start] + i[finish + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break
                                if '|' in i[start + 1:finish] and i[start - 1] != '|' and i[start - 1] == '(' and i[finish + 2] == '|':  # 1.1.2
                                    f.append(''.join(i[:start] + i[start:finish + 1] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start] + i[finish + 3:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break

                                if '|' not in i[start + 1:finish] and i[start - 1] == '|' and i[start - 2] == '(':  # 1.2.1
                                    f.append(''.join(i[:start] + i[start + 1:finish] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start - 1] + i[finish + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break
                                if '|' not in i[start + 1:finish] and i[start - 1] == '|' and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|\.|@|&|<|>|\-|\*|\[|\]|\+)', i[start - 2]) and i[finish + 2] == ')':  # 1.2.2.1
                                    f.append(''.join(i[:start] + i[start + 1:finish] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start - 1] + i[finish + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break
                                if '|' not in i[start + 1:finish] and i[start - 1] == '|' and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|\.|@|&|<|>|\-|\*|\[|\]|\+)', i[start - 2]) and i[finish + 2] == '|':  # 1.2.2.2
                                    f.append(''.join(i[:start] + i[start + 1:finish] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start] + i[finish + 3:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break
                                if '|' not in i[start + 1:finish] and i[start - 1] == '|' and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|\.|@|&|<|>|\-|\*|\[|\]|\+)', i[start - 2]) and re.fullmatch(
                                        '(\w|©|®|£|\{|\}|\%|\?|\.|@|&|<|>|\-|\*|\[|\]|\+)', i[finish + 2]):  # 1.2.2.3
                                    f.append(''.join(i[:start] + i[start + 1:finish] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start] + i[finish + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break

                                    # дальше была одна скобка, но её  из-за длины и несовпадения (индекс выходил за пределы диапозона) пришлось размножить
                                if len(i) - 1 < finish + 2:  # если длина итеририруемого выражения меньше индекса элемента, то тогда проверяем ближайший элемент после )

                                    if '|' not in i[start + 1:finish] and i[start - 1] != '|' and i[finish + 1] != '|':  # 1.3.1
                                        f.append(''.join(i[:start] + i[start + 1:finish]))  # добавь в общий список скобку, где есть знак вопроса
                                        f.append(''.join(i[:start]))  # добавь в общий список скобку, где нет знака вопроса
                                        f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                        break
                                if len(i) - 1 >= finish + 2:  # если длина итеририруемого выражения больше или равна индексу элемента, то тогда всё ок, проверяем дальний элемент после ) (финиша)

                                    if '|' not in i[start + 1:finish] and i[start - 1] != '|' and i[finish + 2] != '|':  # 1.3.2
                                        f.append(''.join(i[:start] + i[start + 1:finish] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                        f.append(''.join(i[:start] + i[finish + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                                        f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                        break

                                if '|' not in i[start + 1:finish] and i[start - 1] != '|' and i[finish + 2] == '|' and i[start - 1] == '(':  # 1.4.1
                                    f.append(''.join(i[:start] + i[start + 1:finish] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start] + i[finish + 3:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break
                                if '|' not in i[start + 1:finish] and i[start - 1] != '|' and i[finish + 2] == '|' and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|\.|@|&|<|>|\-|\*|\[|\]|\+)', i[start - 1]):  # 1.4.2
                                    f.append(''.join(i[:start] + i[start + 1:finish] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start] + i[finish + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break

                                if '|' in i[start + 1:finish] and i[start - 1] == '|':  # 1.5
                                    f.append(''.join(i[:start] + i[start:finish + 1] + i[finish + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                                    f.append(''.join(i[:start] + i[finish + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                                    f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                                    break
                    except IndexError:
                        pass
                if re.search('\)\)\?', ''.join(i)) and re.search('\(\(', ''.join(i)):  # chebur
                    for k in range(len(i)):  # итерация по количеству букв в списке
                        if re.fullmatch('\(', i[k - 1]) and re.fullmatch('\(', i[k]) and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|@|<|\-|\*|\[|\]|\.|\+|\|)', i[k + 2]):  # если в строке скобка ((а
                            start2 = k  # фиксация начала скобки со знаком вопроса
                            continue
                        if re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|\?|\.|@|&|<|>|\-|\*|\[|\]|\.|\+|\||\.)', i[k - 2]) and re.fullmatch('\)', i[k - 1]) and re.fullmatch('\)', i[k]) and re.fullmatch('(\?)', i[k + 1]):  # б))?
                            f.append(''.join(i[:start2] + i[start2 + 1:k] + i[k + 2:]))  # добавь в общий список скобку, где есть знак вопроса
                            f.append(''.join(i[:start2 - 1] + i[k + 2:]))  # добавь в общий список скобку, где нет знака вопроса
                            f[x] = '#$'  # замени обрабатываемую строку на эти символы, чтобы потом их скрыть
                            break
            base_line = (list(set([k for k in f if k != '#$'])))  # генерируем список, в котором нет обрабатываемых строк. через множество избавляемся от повторяющихся значений. создаём обратно список
            for x in range(len(base_line)):
                base_line[x] = base_line[x].replace('<', '(').replace('>', ')').replace('&', '|')  # возвращаем обратно скобки и слэши

        sl_zap = []
        for i in base_line:
            sl_zap.append(i.replace(',', '®'))
        base_line = sl_zap

        # программа раскрывает скобки и делает все возможны варианты
        stroka = ', '.join(base_line)

        while '|' in stroka:
            spis_strok = stroka.split(',')

            spis_strok = list(set(spis_strok))
            for indexstr, stroka in enumerate(spis_strok):
                if '|' in stroka:
                    if re.search('\(\S+ ', stroka):
                        while re.search('\(\S+ ', stroka) or re.search(' \S+\)', stroka) or re.search(' \S+\|', stroka) or re.search('\|\S+ ', stroka):
                            for bukva in range(len(stroka)):
                                if (re.fullmatch('\(', stroka[bukva])) and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|@|<|>|\-|_|\?|\*|\[|\]|\.|\+|\|)', stroka[bukva + 1]):  # если в строке скобка
                                    start = bukva  # фиксация начала скобки со знаком вопроса
                                    continue
                                if (re.fullmatch('\)', stroka[bukva])) and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|@|<|>|\-|_|\?|\*|\[|\]|\.|\+|\|)', stroka[bukva - 1]):  # если в строке скобка
                                    end = bukva  # фиксация начала скобки со знаком вопроса
                                    break
                            skobka = stroka[start:end + 1]
                            if re.search('\(\S+ ', skobka) or re.search(' \S+\)', skobka) or re.search(' \S+\|', skobka) or re.search('\|\S+ ', skobka):
                                skobka = skobka.replace(' ', '_').replace('(', '<').replace(')', '>').replace('|', '&')
                                stroka = stroka[:start] + skobka + stroka[end + 1:]
                            else:
                                skobka = skobka.replace('(', '<').replace(')', '>').replace('|', '&')
                                stroka = stroka[:start] + skobka + stroka[end + 1:]
                        stroka = stroka.replace('<', '(').replace('>', ')').replace('&', '|')
                    spis_slov = stroka.split()
                    for slovo in spis_slov:  # определяем кусок со скобкой
                        if re.match('\)\S*', slovo) or re.match('\S*\(', slovo):
                            slovo = list(slovo)
                            for bukva in range(len(slovo)):
                                if re.fullmatch('\(', slovo[bukva]) and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|@|<|>|\-|_|\?|\*|\[|\]|\.|\+|\|)', slovo[bukva + 1]):  # если в строке скобка
                                    start = bukva  # фиксация начала скобки со знаком вопроса
                                    continue
                                if re.fullmatch('\)', slovo[bukva]) and re.fullmatch('(\w|©|®|£|\{|\}|\%|\?|@|<|>|\-|_|\?|\*|\[|\]|\.|\+|\|)', slovo[bukva - 1]):  # если в строке скобка
                                    end = bukva  # фиксация начала скобки со знаком вопроса
                                    break
                            slovo = ''.join(slovo)
                            skobka = slovo[start:end + 1]
                            skobka = skobka.replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace("'", '')
                            slova_v_skobke = skobka.split('|')  # сделали варианты внутри скобки. добавили в новый список
                            slova_v_skobke.insert(0, spis_slov.index(slovo))  # добавили индекс
                            kolvo_slov_v_skob = len(slova_v_skobke) - 1  # минусуем на один, потому что один из элементов - это индекс. а нам надо знать точно количество слов
                            break
                    new_stroki_vmeste = []
                    for nomer_slova_v_skob in range(0, kolvo_slov_v_skob):
                        new_stroka = []
                        for indexslova, slovo in enumerate(spis_slov):
                            if '|' not in slovo:
                                new_stroka.append(slovo)
                            if '|' in slovo:
                                if indexslova == slova_v_skobke[0]:
                                    vrem1 = []
                                    vrem1.append(slovo[:start])
                                    vrem1.append(slova_v_skobke[nomer_slova_v_skob + 1])
                                    vrem1.append(slovo[end + 1:])
                                    new_stroka.append(''.join(vrem1))
                                else:
                                    new_stroka.append(slovo)
                        new_stroki_vmeste.append(' '.join(new_stroka))
                    for new_stroka_vmeste in new_stroki_vmeste:
                        new_stroka_vmeste = new_stroka_vmeste.replace('_', ' ')
                        spis_strok.append(new_stroka_vmeste)
                    spis_strok[indexstr] = '$'
                    stroka = ', '.join([k for k in spis_strok if k != '$'])

            base_line = list(set([k for k in spis_strok if k != '$']))


        # программа перебирает все возможные варианты с одиночным знаком вопроса
        sp_bez_zn_vopr = []
        for nom_strok in range(len(base_line)):
            if '?' in base_line[nom_strok]:
                #print(a[nom_strok], 'a[nom_strok]')
                slovo = base_line[nom_strok]
                count = 0
                slovo = slovo.replace('((', '(').replace('))', ')').replace(')|(', '|')
                slovo = re.sub('^\(', '', slovo)
                slovo = re.sub('\)$', '', slovo)
                chet = []
                num_var = 2 ** len(re.findall("\?", slovo))  # количество вариатов перебора со знаком вопроса
                for k, e in enumerate(slovo):
                    if e == '(':
                        chet.append(k)
                    if e == ')':
                        chet.append(k)
                lend = len(chet)
                for i in range(0, lend - 1):
                    if i % 2 == 0:
                        k = slovo[chet[i]:chet[i + 1] + 1].replace('(', '<').replace(')', '>').replace('|', '$')
                        slovo = slovo[:chet[i]] + k + slovo[chet[i + 1] + 1:]  # код ради того, чтобы правильно делить внутренние скобки
                if re.match('.*\?*', slovo):
                    slovo = slovo.split('|')  # разбили строку на подстроки-слова по слэшу
                    for i, j in enumerate(slovo):  # индекс слова. итерируем внутри каждого элемента между слэшами
                        if '?' in j:  # если в элементе есть знак вопроса, то
                            for k, p in enumerate(j):  # итерируем этот элемент между слэшами по буквам
                                if '?' in p:  # если '?' в букве, то
                                    slovo.append(slovo[i][:k] + slovo[i][k + 1:])  # добавляем обработанные новые элементы в тек.список
                                    slovo.append(slovo[i][:k - 1] + slovo[i][k + 1:])
                                    slovo[i] = []  # делаем пустыми элементы, которые уже обработали
                name_var = list(filter(lambda x: x, slovo))  # итоговый варианты (список) со знаком "?" и без него.
                for i in name_var:
                    sp_bez_zn_vopr.append(''.join(i))
            else:
                sp_bez_zn_vopr.append(base_line[nom_strok])
        new_list_from_original_line_key = list(set(sp_bez_zn_vopr))
        return new_list_from_original_line_key
    file = codecs.open("files/surname_regular.txt", "r", "utf-8")
    datasur = file.read()
    file .close()
    dict4=[]
    for onlysur in datasur.split('\n'):
        try:
            dict4.append(onlysur.split()[0])
        except:
            pass
    workdict=list(set(dict4))

    #дубли убираются с помощью анализа регулярок на совпадения - сверху вниз
    dict5=[]
    for indexorig_line, orig_line in enumerate(workdict):
        dict5.append(repreg(orig_line))
    print(len(workdict), workdict, 'до')
    for indexline1, line1 in enumerate(dict5):
        for indexline2,line2 in enumerate(dict5):
            if indexline2>indexline1:
                counter_match=0
                for substring1 in line1:
                    substring1 = substring1.replace('\ufeff', '')
                    for substring2 in line2:
                        substring2 = substring2.replace('\ufeff', '')
                        if substring1==substring2:

                            counter_match+=1
                            print(substring1, substring2, 'субстринги', counter_match, len(line2))
                            if counter_match==len(line2):
                                print(workdict[indexline1], '--', workdict[indexline2])
                                workdict[indexline2]='¶'
    workdict=[k for k in workdict if k != '¶']
    print(len(workdict), workdict, 'после1')

    #дубли убираются с помощью анализа регулярок на совпадения - снизу вверх
    dict6=[]
    for lin in reversed(workdict):
        dict6.append(repreg(lin))
    dict7=[]
    for lin in reversed(workdict):
        dict7.append(lin)
    for indexline1, line1 in enumerate(dict6):
        for indexline2,line2 in enumerate(dict6):
            if indexline2>indexline1:
                #print(line1, line2, '++++++')
                counter_match=0
                for substring1 in line1:
                    substring1=substring1.replace('\ufeff','')
                    for substring2 in line2:
                        substring2 = substring2.replace('\ufeff', '')
                        if substring1==substring2:
                            #print(substring1,substring2, '-----+-+-')
                            counter_match+=1
                            if counter_match==len(line2):
                                print(dict7[indexline1], '-/-', dict7[indexline2])
                                dict7[indexline2]='¶'
    workdict=[k for k in dict7 if k != '¶']
    print(len(workdict), workdict, 'после2')

    #сохранение итоговой очищенной версии в файл
    file_for_record = open('files/surname_reg_without_dublicates.txt', 'w', encoding="utf-8")
    for newlinerec in workdict:
        try:
            file_for_record.write(str(newlinerec + '\n'))
        except UnicodeEncodeError:
            pass
    file_for_record.close()

zapusk(original_file)