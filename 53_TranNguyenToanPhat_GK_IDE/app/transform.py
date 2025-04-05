def transform_data(data):
    data['buy_price'] = float(data['buy_price'].replace('đ', '').replace('.', ''))
    data['sell_price'] = float(data['sell_price'].replace('đ', '').replace('.', ''))
    return data

