from func import is_unstable

if __name__ == "__main__":
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
    # Проверяемы пары
    print(is_unstable(h_prefs, s_prefs, h_s_pairs, {'Atlanta':'Yolanda'}))
    print(is_unstable(h_prefs, s_prefs, h_s_pairs, {'Boston':'Xavier'}))
    print(is_unstable(h_prefs, s_prefs, h_s_pairs, {'Boston':'Zeus'}))
