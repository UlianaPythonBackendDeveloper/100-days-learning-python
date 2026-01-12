def get_super_series_winner(scores):
    canada_wins = 0
    ussr_wins = 0
    
    for game in scores:
        # Распаковываем счёт
        canada, ussr = game
        
        # Сравниваем счёт
        if canada > ussr:
            canada_wins += 1
        elif ussr > canada:
            ussr_wins += 1
        # Ничья - ничего не делаем
    
    # Определяем победителя
    if canada_wins > ussr_wins:
        return 'canada'
    elif ussr_wins > canada_wins:
        return 'ussr'
    else:
        return None
        
scores = [[3, 7], [4, 1], [4, 4], [3, 5], [4, 5], [3, 2], [4, 3], [6, 5]]
print(get_super_series_winner(scores))  # Должно быть 'canada'