def count_letters(text):
    lower_text = text.lower()
    dictionary_chars = {}
    for char in lower_text:
        if char.isalpha():
            if char in dictionary_chars:
                dictionary_chars[char] += 1
            else:
                dictionary_chars[char] = 1

    return dictionary_chars


def calculate_frequency(dictionary_chars):
    total_chars_count = sum(dictionary_chars.values())

    chars_frequency = {}
    for count, letter in dictionary_chars.items():
        chars_frequency[count] = letter / total_chars_count
    return chars_frequency


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

count_chars = count_letters(main_str)
frequency_chars = calculate_frequency(count_chars)

for letter, frequency in frequency_chars.items():
    print(f"{letter}: {frequency:.2f}")
