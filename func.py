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
    
    # Проверка пар на неустойчивость
    for cat in list(pair_checked.keys()):
        current_dog = cat_dog_pairs[cat]
        dog = pair_checked[cat]
        current_cat = dog_cat_pairs[dog]

        # 1. Кошка предпочитает эту собаку своей текущей собаке
        cat_prefers_dog = cat_rank[cat][dog] < cat_rank[cat][current_dog]

        # 2. Собака предпочитает эту кошку своей текущей кошке
        dog_prefers_cat = dog_rank[dog][cat] < dog_rank[dog][current_cat]
        
        # Если оба условия верны -> найдена нестабильная пара
        if cat_prefers_dog and dog_prefers_cat:
            print(f"Пара {cat} - {dog} неустойчивая")         
        else: 
          print(f"Пара {cat} - {dog} устойчивая")