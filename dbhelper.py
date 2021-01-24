from datetime import datetime

import pymysql
import dbconf


class DBHelper:

    def connect(self, database="db_pinfood"):
        return pymysql.connect(host='localhost',
                               user=dbconf.dbuser,
                               passwd=dbconf.dbpassword,
                               db=database)

    def get_all_foods(self):
        connection = self.connect()
        try:
            query = "SELECT latitude, " \
                    "longitude, " \
                    "date, " \
                    "category, " \
                    "description FROM foods;"

            with connection.cursor() as cursor:
                cursor.execute(query)

            named_foods = []

            for food in cursor:
                named_food = {
                    'latitude': food[0],
                    'longitude': food[1],
                    'date': datetime.strftime(food[2], '%Y- %m-%d'),
                    'category': food[3],
                    'description': food[4]
                }

                named_foods.append(named_food)

            return named_foods

        finally:
            connection.close()

    def add_food(self, category, date, latitude, longitude, description):
        connection = self.connect()

        try:
            query = "INSERT INTO foods (" \
                    "category, " \
                    "date, " \
                    "latitude, " \
                    "longitude, " \
                    "description) \
                    VALUES (%s, %s, %s, %s, %s)"

            with connection.cursor() as cursor:
                cursor.execute(query,
                               (category,
                                date,
                                latitude,
                                longitude,
                                description))
                connection.commit()

        except Exception as e:
            print(e)

        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()

        try:
            query = "DELETE FROM foods;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()