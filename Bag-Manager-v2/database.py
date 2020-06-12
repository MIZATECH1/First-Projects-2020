import sqlite3



def add_bag(name, quantity, status, date):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO records VALUES (?,?,?,?)", (name.lower(), int(quantity), status, date))
    conn.commit()
    conn.close()


def show_all_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM records")
    data = c.fetchall()
    index = []
    name_list = []
    quantity_list = []
    status_list = []
    date_list = []

    for s in data:
        index.append(str(s[0]))
        name_list.append(s[1])
        quantity_list.append(s[2])
        status_list.append(s[3])
        date_list.append(s[4])

    conn.commit()
    conn.close()
    return index, name_list, quantity_list, status_list, date_list




def specific_bag_data(bag_name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * from records WHERE name = (?)", (bag_name,))
    details = c.fetchall()
    for s in details:
        control_data = f"Bag Name: {s[0]}, Inventory: {s[1]}, status: {s[2]}, Date: {s[3]}"

    conn.commit()
    conn.close()
    return control_data


def get_bag_quantity(bag_name):

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * from records WHERE name = (?)", (bag_name.lower(),))
    details = c.fetchall()
    for s in details:
        bag_inventory = int(s[1])
    conn.commit()
    conn.close()
    return bag_inventory



def delete_record(bag_name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE from records WHERE name = (?)", (bag_name, ))
    conn.commit()
    conn.close()



def update_quantity(bag_name, quantity):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("UPDATE records SET quantity = (?)  WHERE name = (?)", (quantity, bag_name))
    conn.commit()
    conn.close()


def update_date(date, bag_name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("UPDATE records SET date = (?)  WHERE name = (?)", (date, bag_name))
    conn.commit()
    conn.close()



def show_all_warnings(sq):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT  * from records WHERE quantity < (?)", (sq,))
    details = c.fetchall()
    name_list = []
    quantity_list = []
    status_list = []
    date_list = []
    for s in details:
        name_list.append(s[0])
        quantity_list.append(s[1])
        status_list.append(s[2])
        date_list.append(s[3])
    conn.commit()
    conn.close()
    return  name_list, quantity_list, status_list, date_list


