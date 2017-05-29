import sqlite3

# create a database
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example (Masculinitive1 VARCHAR, Feminitive1 VARCHAR, SYM BOOLEAN, Definition TEXT) ")

# create_table()

# SQL QUERY:
def enter_data():
    c.execute("INSERT INTO example VALUES ('Філософ', 'Філософеса', 'FALSE', 'Та, хто займається/захоплюється філософією')")
    c.execute("INSERT INTO example VALUES ('Автомобіліст', 'Автомобілістка', 'FALSE', 'Та, хто керує автомобілем')")
    c.execute("INSERT INTO example VALUES ('Викладач', 'Викладачка', 'FALSE', 'Та, хто викладає предмети в школі/університеті')")
    conn.commit()

#mimic user entering data
# def enter_dynamic_data():
#     Masculinitive1 = input("What's the intial Masculinitive? ")
#     Feminitive1 = input("What's the corresponding Feminitive1? ")
#     SYM = input("Is it available in SYM Dict? ")
#     Definition = input("What's the definition of this word? ")
#
#     c.execute("INSERT INTO example(Masculinitive1, Feminitive1, SYM, Definition) VALUES (?, ?, ?, ?)", (Masculinitive1, Feminitive1, SYM, Definition))
#
#     conn.commit()

#reading data
#(*) - read everything
def read_from_database():

    what_fem = input("What Feminitive1 do you want to get? ")
    sql = "SELECT * FROM example WHERE Feminitive1 = ?"

    for row in c.execute(sql, [what_fem]):
        print(row)

read_from_database()


# enter_dynamic_data()



# manual data entry
#enter_data()

# conn.close()
