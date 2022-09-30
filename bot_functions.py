from re import S, T
import sqlite3
import re

def find_string(string, search_string):
    if re.search(search_string, string) == None:
        return False
    else: return True

def add_user(username):
    try:
        database.create_table(username, "achivements")
        return True
    except: 
        print("username already saved")
        return False
    	
def add_achivement_to_user(username, achivement):
    if database.find_string_in_db(achivement, username) == True:
        print("achivement already gotten")
        return False
    else:
        database.save_string_to_table(achivement, username, "achivements")
        return True

def return_all_achivements(username):
    return database.return_all_from_column("achivements", username)

class database:

    global connection
    global cursor


    connection = sqlite3.connect("dateabase.sqlite")
    cursor = connection.cursor()
    


    def create_table(table, text):

        sql_command = """
        CREATE TABLE """+table+""" (
        Number INTEGER PRIMARY KEY,   
        """+text+""" TEXT);
        """

        cursor.execute(str(sql_command))

    def remove_table(selected_table):
        sql_command = """
        DROP TABLE """+selected_table+""";
        """
        cursor.execute(str(sql_command))



    def return_one(x, selected_table):
        cursor.execute("SELECT * FROM " + selected_table)
        i = 0
        while i != int(x):
            res = cursor.fetchone() 
            i = i+1
            return res

    def return_all(selected_table):
        cursor.execute("SELECT * FROM " + selected_table)
        result = cursor.fetchall() 
        string = ""
        for r in result:
            print(result)
            string = string + str(result)
            return str(result)
    
    def return_all_from_column(column, selected_table): # returns all strings from a column, seperated by "|"
        cursor.execute("SELECT "+column+" FROM " + selected_table)
        result = cursor.fetchall() 
        # This makes things the output just more readable
        # I have litterally no idea what I did here, but it works pls do not touch
        replace1_result = str(result).replace("',"," | ")
        replace2_result = str(replace1_result.translate({ord(letter): None for letter in "[('),]"}).rstrip(" | "))
        replace_result = replace2_result.lstrip("['").rstrip("', '']")
        return str(replace_result)


    def find_string_in_db(fstring, selected_table):
        if str(database.return_all(selected_table)).find(str(fstring)) != -1:
            return True
            print(str(database.return_all(selected_table)).find(str(fstring)))
        else: return False

    def save_string_to_table(string, selected_table, collumn):
        if database.find_string_in_db(string, selected_table) == False:
            sql_command = """
            INSERT INTO """ + selected_table + """ (
            """ + "Number" + """, """ + collumn + """)
            VALUES (NULL, '""" + string + """'
            )"""
            cursor.execute(sql_command)
            connection.commit()
            return "String saved succesfully"
        else: return "String Already saved to database"