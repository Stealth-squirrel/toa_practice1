def is_unstable(h_prefs, s_prefs, h_s_pairs, pairs_check):
    # Создаем словари рангов
    h_rank = {}
    for h, prefs in h_prefs.items():
        h_rank[h] = {s: i for i, s in enumerate(prefs)}

    s_rank = {}
    for s, prefs in s_prefs.items():
        s_rank[s] = {h: i for i, h in enumerate(prefs)}
    # Словарь, где данные паросочетания больница-студент представлены в виде студент-больница
    s_h_pairs = {s: h for h, s in h_s_pairs.items()}

    # Проверка пар на неустойчивость
    for h, s in pairs_check.items():
        current_s = h_s_pairs[h]
        current_h = s_h_pairs[s]

        # Проверка пар на существование
        if current_h == h and current_s == s:
            return f'Пара {h} - {s} уже установлена'
            continue

        # 1. Больница предпочитает этого студента своему текущему студенту
        h_prefers_s = h_rank[h][s] < h_rank[h][current_s]

        # 2. Студент предпочитает эту больницу своей текущей больнице
        s_prefers_h = s_rank[s][h] < s_rank[s][current_h]

        # Если оба условия верны -> найдена нестабильная пара
        if h_prefers_s and s_prefers_h:
            return f"Пара {h} - {s}: неустойчивое"
        else:
            return f"Пара {h} - {s}: устойчивое"

h_prefs = {'Atlanta': ['Xavier', 'Yolanda', 'Zeus'],
          'Boston': ['Yolanda', 'Xavier', 'Zeus'],
          'Chicago': ['Xavier', 'Yolanda', 'Zeus']}

s_prefs = {'Xavier': ['Boston', 'Atlanta', 'Chicago'],
            'Yolanda': ['Atlanta', 'Boston', 'Chicago'],
            'Zeus': ['Atlanta', 'Boston', 'Chicago']}

# Данные пары
h_s_pairs = {"Atlanta":   "Xavier",
                "Boston": "Zeus",
                "Chicago":   "Yolanda"}

print(is_unstable(h_prefs, s_prefs, h_s_pairs, {'Atlanta':'Yolanda'})) 
print(is_unstable(h_prefs, s_prefs, h_s_pairs, {'Boston':'Xavier'}))
print(is_unstable(h_prefs, s_prefs, h_s_pairs, {'Boston':'Zeus'}))

# Пара Atlanta - Yolanda: устойчивое
# Пара Boston - Xavier: неустойчивое
# Пара Boston - Zeus уже установлена
