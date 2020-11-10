alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
while True:
    print('Введите Ш чтобы зашифровать сообщение, Р чтобы расшифровать и В чтобы выйти')
    menu = input('>>> ').lower() #приведем ответ к нижнему регистру методом .lower()
    if menu == 'в': #проверим условие, если пользователь выбрал В
        break
    elif not (menu == 'ш' or menu == 'р'): #если пользователь ошибочно ввел любой символ кроме Ш и Р запустим наш цикл заново командой continue
        continue
    output = ''
    message = input('Введите строку: ').lower() #ввод строки
    key = int(input('Введите ключ: ')) #ключ для шифрования
    if menu == 'р': #проверим условие, если пользователь выбрал Р 
        key *= -1 #значение ключа key умножим на -1, чтобы оно стало противоположным по знаку
    for letter in message: 
        if letter in alphabet: #проверим, является ли полученный символ буквой 
            t = alphabet.find(letter) #методом .find() найдем позицию буквы из сообщения в нашем алфавите и запишем в переменную t
            new_key = (t + key) % len(alphabet) #вычислим новое значение с учетом смещения на значение нашего ключа
            output += alphabet[new_key] #добавим в строку output букву с индексом new_key
        else:
            output += letter #выведем строку output с нашим зашифрованным сообщением
    print('Результат: ' + output)
