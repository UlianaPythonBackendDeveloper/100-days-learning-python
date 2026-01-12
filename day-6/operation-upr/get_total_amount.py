def get_total_amount(money,currency):
    total = 0
    for item in money:
        item_currency, amount = item.split()
        
        if item_currency == currency:
            total += int(amount)
        
    return total