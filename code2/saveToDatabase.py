import MySQLdb

class SaveToDatabase():
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost", user="root", passwd='computer', db='imageSensor')
        self.cur = self.db.cursor()

    def insertIntoImagesTable(self, sensor, imageNumber, count, leftVal, rightVal, middleVal):
        tableName = 'images'
        query = "INSERT INTO " + tableName + " VALUES (NULL, '" + sensor + "', "  + str(imageNumber) + ",  " + str(count) + ",  " + str(leftVal) + ",  " + str(rightVal) + ",  " +  str(middleVal) + ")"
        # print query
        self.cur.execute(query)
        self.db.commit()

    def closeAll(self):
        self.db.close()

# saveValues = SaveToDatabase()
# saveValues.insertIntoImagesTable('im', 2,3,1,1,1)
# saveValues.closeAll()