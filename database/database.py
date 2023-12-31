import sqlite3

class DataBase:
    def __init__(self):
        self.database = sqlite3.connect('shop.db', check_same_thread=False)

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False):
        with self.database as db:
            cursor = db.cursor()
            cursor.execute(sql, args)
            if commit:
                result = db.commit()
            if fetchone:
                result = cursor.fetchone()
            if fetchall:
                result = cursor.fetchall()
            return result


    def create_users_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS users(
            telegram_id BIGINT PRIMARY KEY,
            full_name VARCHAR(100),
            phone VARCHAR(20) UNIQUE
        )'''
        result = self.manager(sql, commit=True)
        print("Insert result:", result)


    def get_user_by_id(self, telegram_id):
        sql = '''
        SELECT * FROM users WHERE telegram_id = ?
        '''
        return self.manager(sql, telegram_id, fetchone=True)


    def insert_user(self, telegram_id, full_name, phone):
        sql = '''
        INSERT INTO users(telegram_id, full_name, phone) VALUES (?,?,?)
        '''
        self.manager(sql, telegram_id, full_name, phone, commit=True)

    def create_filials_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS filials(
            filial_id INTEGER PRIMARY KEY AUTOINCREMENT,
            filial_name VARCHAR(100),
            places INTEGER,
            worktime VARCHAR(100),
            address VARCHAR(100)
        )
        '''
        self.manager(sql, commit=True)


    def insert_filials(self):
        sql = '''
        INSERT INTO filials(filial_name, places, worktime, address) VALUES
        ('Чиланзар', 50, '11:00-23:00', 'На чиланзаре'),
        ('Максимка', 70, '10:00-23:00', 'На максимке'),
        ('Чорсу', 90, '09:00-23:00', 'На чорсу'),
        ('Малика', 40, '11:00-23:00', 'На малике')
        '''
        self.manager(sql, commit=True)

    def get_filials_names(self):
        sql = '''
        SELECT filial_name FROM filials
        '''
        return self.manager(sql, fetchall=True)


    def get_filial(self, filial_name):
        sql = '''
        SELECT filial_name, places, worktime, address FROM filials WHERE filial_name = ?
        '''
        return self.manager(sql, filial_name, fetchone=True)

    def create_coordinates_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS coordinates(
            coordinate_id INTEGER PRIMARY KEY AUTOINCREMENT,
            filial_id INTEGER,
            latitude REAL,
            longitude REAL,
            FOREIGN KEY (filial_id) REFERENCES filials (filial_id)
        )
        '''
        self.manager(sql, commit=True)

    def insert_coordinates(self):
        sql = '''
        INSERT INTO coordinates(filial_id, latitude, longitude) VALUES
        (1, 41.286153, 69.205599),
        (2, 41.286165, 69.205567),
        (3, 41.286181, 69.205465),
        (4, 41.286254, 69.205534)
        '''
        self.manager(sql, commit=True)

    def get_filial_coordinates(self, filial_name):
        sql = '''
        SELECT latitude, longitude FROM coordinates
        INNER JOIN filials ON filials.filial_id = coordinates.filial_id
        WHERE filials.filial_name = ?
        '''
        return self.manager(sql, filial_name, fetchone=True)

    def create_categories_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS categories(
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_title VARCHAR(50) UNIQUE
        )
        '''
        self.manager(sql, commit=True)

    def insert_categories(self):
        sql = '''
        INSERT INTO categories(category_title) VALUES 
        ('🥗 Салаты'),
        ('🍱 Сеты'),
        ('🍤 Роллы'),
        ('🍣 Суши'),
        ('🍵 Супы'),
        ('🧃 Напитки')
        '''
        self.manager(sql, commit=True)

    def get_categories(self):
        sql = '''
        SELECT category_title FROM categories
        '''
        return self.manager(sql, fetchall=True)