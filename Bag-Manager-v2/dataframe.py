import database as db
import pandas as pd



index, name_list, quantity_list, status_list, date_list = db.show_all_data()


def data_frame(index, name_list, quantity_list, status_list, date_list):

    df = pd.DataFrame(
        {'Name': name_list, 'Inventory': quantity_list, 'Status': status_list, 'Last Edited at': date_list},
        columns=['Name', 'Inventory', 'Status', 'Last Edited at'], index= index)

    return df


def data_frame_2(name_list, quantity_list, status_list, date_list):

    df = pd.DataFrame(
        {'Name': name_list, 'Inventory': quantity_list, 'Status': status_list, 'Last Edited at': date_list},
        columns=['Name', 'Inventory', 'Status', 'Last Edited at'])

    return df



html_data  = data_frame(index, name_list, quantity_list, status_list, date_list).to_html()



