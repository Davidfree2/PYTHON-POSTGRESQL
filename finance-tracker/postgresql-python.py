import psycopg2
connection = psycopg2.connect(database='financeapp', user='python', password='python', host='127.0.0.1', port='5432')

def insert_into_database(one, two, three):
    query = f'''insert into finances (item, amount, date) values ('{one}', {two}, '{three}');'''
    cur = connection.cursor()
    cur.execute(query)
    connection.commit()
    cur.close()
    connection.close()


def select_from_database():
    query = f'''select * from finances;'''
    cur = connection.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print("--------------------")
        print("item = ", row[0])
        print("price = ", row[1])
        print("date  = ", row[2],)
        print("--------------------")
        cur.close()
        connection.close()

def search_from_database_for(search_by, value_being_searched):
    query = f"select * from finances where {search_by} = '{value_being_searched}';"
    cur = connection.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print("--------------------")
        print("item = ", row[0])
        print("price = ", row[1])
        print("date  = ", row[2],)
        print("--------------------")
        cur.close()
        connection.close()

def delete_from_table(item_to_delete):
    query = f'''DELETE FROM finances WHERE item = %s;'''
    cur = connection.cursor()
    cur.execute(query, (item_to_delete,))
    connection.commit()
    cur.close()
    connection.close()

def reconnect():
    connection = psycopg2.connect(database='financeapp', user='python', password='python', host='127.0.0.1', port='5432')
    return connection





opening_program_questions = input('''hello what would you like to do with your finacnesapp database and finances table?
--------------------------------
type (view) to view everything
--------------------------------
type (delete) to delete from database
--------------------------------
type (insert) to insert into database
--------------------------------
type (search) to search your database
--------------------------------
type (quit) to quit program
''')

if opening_program_questions == 'view':
    select_from_database()
elif opening_program_questions == 'insert':
    your_item = input('what item would you like to add?')
    your_amount = input('what amount would you like to add? use numbers')
    your_date = input('what date would you like to add')
    insert_into_database(your_item, your_amount, your_date)
    see_database_question = input('\nwould you like to see your database? (yes/no)')
    if see_database_question == 'yes':
        connection = reconnect()
        select_from_database()
    else:
        pass
elif opening_program_questions == 'delete':
    select_from_database()
    delete_this = input('which item name would you like to delete?')
    connection = reconnect()
    delete_from_table(delete_this)
    see_after_deleting = input('would you like to see your database now?')
    if see_after_deleting == 'yes':
        connection = reconnect()
        select_from_database()
    else:
        pass
elif opening_program_questions == 'search':
    search_by = input('what would you like to search by? ie (item?, amount?, date?)')
    search_for = input('select everything with what keyword (or keynumber if chose price)')
    search_from_database_for(search_by, search_for)
else:
    print('goodbye')
