import psycopg2

def save_price(data):
    conn = psycopg2.connect(
            host="postgres",
            database="airflow",
            user="airflow",
            password="airflow"
        )
    cur = conn.cursor()
        
    create_table = """
        CREATE TABLE IF NOT EXISTS gold_prices (
            id INTEGER PRIMARY KEY,
            name TEXT,
            buy_price INTEGER,
            sell_price INTEGER
        )
        """
    cur.execute(create_table)
    conn.commit()
        
    insert_query = """
    INSERT INTO gold_prices (id, name, buy_price, sell_price)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(insert_query, (
        data['id'],
        data['name'],
        data['buy_price'],
        data['sell_price']
    ))
    conn.commit()