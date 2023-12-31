def tpl_sort(tpl): # Функция tpl_sort принимает единственный параметр tpl входной кортеж
    for i in tpl: # for для перебора каждого элемента 
        if type(i) !=int: # проверяет,не является ли тип каждого элемента целым числом
            return tpl # если не является целым числов,возвращается какой есть 
    result = (sorted(tpl)) # если элементы являются целыми числами,переходит к сортировке 
    return result # возвращается отсортированный кортеж
    
def sliker(tpl, elem):
        if elem not in tpl: # инструкция для проверки присутствует ли elem в tpl
            return() # Если он отсутствует, функция возвращает пустой кортеж
        start = tpl.index(elem) # Если elem присутствует в tpl, функция переходит к поиску начального
        if tpl.cout(elem)==1:
            return tpl[start:] # проверяет, elem появляется в tpl кортеже только один раз. Если произойдет, 
                                      # вернет фрагмент кортежа
        end=tpl.index(elem, start +1) # Если elem появляется более одного раза функция находит следующий вхождения элемента
        return tpl[start:end+1] # возвращает фрагмент кортежа фрагмент будет включать все вхождения 
        
def sieve(tpl):
    return tuple(set(tpl))[::-1] # Функция принимает параметр tpl, который представляет входной кортеж

def del_from_tuple(tpl, elem): # принимает два параметра: tpl, elem
        if elem not in tpl: #  проверяет, существует ли элемент в кортеже, используя оператор in
            return tpl # Если элемент не найден,возвращает исходный кортеж
    
        s = [] # Создаем пустой список для хронение элем кортежа
        for i in tpl: ; # перебираем каждый элемент используя for 
            s.append(i) # внутри цикла добавляем каждый элемент 
        s.remove(elem) # метод для удаления нужного элемента elem из списка s
        return tuple(s) # Преобразуем измененный список s обратно в кортеж с помощью tuple() и возвращаем его.

def good_students(students): # функции good которая принимает список учащихся в качестве входных данных
    a = 0 # a инициализируется значением 0
    for student in students: # цикл для перебора каждого ученика
        a += student[2] # Внутри цикла оценка каждого ученика добавляется к переменной a
    a /= len(students) # значение a делится на длину students списка для расчета средней оценки

    names = [] # Инициализируйте пустой список для хранения имен с оценками выше порогового значения 
    for student in students: # повторить процедуру с каждым учеником 
        if student[2] > a: # проверка не привышает ли оценка,пороговоре значение (а)
            names.append(student[0]) # если условие выполнено то добавляется имя 
            
def generate_short_names(names): # функция принимает параметр names,представляет список полных имен
    shortNames = '' # инициализируем пустую строковую переменную
    for name in names: # перебираем каждое имя 
        end = name.index(' ') # дает нам место первого пробела в полном имени
        shortNames += f'{name[:end]}, ' # объединяем имя с запятой и пробелом shortNames cтроку

    return f"Ученики {shortNames[:-2]} в этом семестре хорошо учатся!" # функция возвращает форматированную строку

students = (("Крячко Марк Александрович", 19, 4.2, "Новосибирск"),
            ("Муллакаев Андрей Евгеньевич", 17, 4.7, "Обь"),
            ("Павлов Александр Витальевич", 20, 4.5, "Новосибирск"),
            ("Муллакаев Андрей Евгеньевич", 17, 4.7, "Новосибирск"),
            ("Левин Максим Максимович", 16, 5.0, "Новосибирск"),
            ("Новиков Дмитрий Дмитриевич", 17, 3.2, "Новосибирск"),
            ("Головин Гордей Романович", 17, 3.1, "Новосибирск"))
print(good_students(students))
