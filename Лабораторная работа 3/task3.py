def count_letters(text):
    dictionary_of_words = {}
    text = text.replace(' ', '')
    text = text.lower()

    for word in text:
        if word.isalpha() and word not in dictionary_of_words:
            dictionary_of_words[word] = 1
        elif word.isalpha():
            dictionary_of_words[word] = dictionary_of_words[word] + 1

    return dictionary_of_words

def calculate_frequency(dictionary):
    count_words = sum(dictionary.values())

    for frequency in dictionary:
        dictionary[frequency] = dictionary[frequency] / count_words

    return dictionary


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

count_dictionary = count_letters(main_str)
frequency_dictionary = calculate_frequency(count_dictionary)

for word, frequency in frequency_dictionary.items():
    print(f"{word}: {frequency:.2f}")