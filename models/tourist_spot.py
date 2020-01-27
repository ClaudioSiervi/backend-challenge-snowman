import sqlite3


class TrouristSpot():
    def find_by_name(self, name):
        pass

    def find_spots_aroud(self, name, gps):
        pass

    @classmethod
    def insert(self, new_spot):
        # if TrouristSpot.find_by_name(name) is not None:
        #     return {"messege ": "This tourist spot already registred."}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO tourist_spots VALUES (NULL, ?, ?, ?, ?)'
        cursor.execute(query, (new_spot['name'], new_spot['gps'], new_spot['id_category'], new_spot['id_user']))

        connection.commit()
        connection.close()