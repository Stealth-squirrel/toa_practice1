def is_unstable(cats_prefs, dogs_prefs, cat_dog_pairs, pair_checked):
    # Создаем словари рангов
    cat_rank = {}
    for cat, prefs in cats_prefs.items():
        cat_rank[cat] = {dog: i for i, dog in enumerate(prefs)}

    dog_rank = {}
    for dog, prefs in dogs_prefs.items():
        dog_rank[dog] = {cat: i for i, cat in enumerate(prefs)}
    # Словарь, где данные паросочетания кошка-собака представлены в виде собака-кошка
    dog_cat_pairs = {dog: cat for cat, dog in cat_dog_pairs.items()}

    # Проверка пары на неустойчивость
    for cat, dog in pair_checked.items():
        current_dog = cat_dog_pairs[cat]
        current_cat = dog_cat_pairs[dog]

        # Проверка пары на существование
        if current_cat == cat and current_dog == dog:
            return f'Пара {cat} - {dog} уже установлена'
            continue

        # 1. Кошка предпочитает эту собаку своей текущей собаке
        cat_prefers_dog = cat_rank[cat][dog] < cat_rank[cat][current_dog]

        # 2. Собака предпочитает эту кошку своей текущей кошке
        dog_prefers_cat = dog_rank[dog][cat] < dog_rank[dog][current_cat]

        # Если оба условия верны -> найдена нестабильная пара
        if cat_prefers_dog and dog_prefers_cat:
            return f"Пара {cat} - {dog}: неустойчивое"
        else:
            return f"Пара {cat} - {dog}: устойчивое"

# Предпочтения кошек
cats_prefs = {'Сфинкс': ['Мопс', 'Такса', 'Доберман'],
              'Мейн-кун': ['Такса', 'Мопс', 'Доберман'],
              'Девон-рекс': ['Мопс', 'Такса', 'Доберман']}

# Предпочтения собак
dogs_prefs = {'Мопс': ['Мейн-кун', 'Сфинкс', 'Девон-рекс'],
              'Такса': ['Сфинкс', 'Мейн-кун', 'Девон-рекс'],
              'Доберман': ['Сфинкс', 'Мейн-кун', 'Девон-рекс']}

# Данные пары
cat_dog_pairs = {"Сфинкс":   "Доберман",
                 "Мейн-кун": "Такса",
                 "Девон-рекс":   "Мопс"}

# Проверяемы пары
print(is_unstable(cats_prefs, dogs_prefs, cat_dog_pairs, {'Сфинкс':'Доберман'}))
print(is_unstable(cats_prefs, dogs_prefs, cat_dog_pairs, {'Сфинкс':'Такса'}))
print(is_unstable(cats_prefs, dogs_prefs, cat_dog_pairs, {'Девон-рекс':'Доберман'}))
