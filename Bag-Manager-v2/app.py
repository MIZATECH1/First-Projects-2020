from datetime import date
from flask import Flask, render_template, request
import database as db
import dataframe as df
import send_mail as sm
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/change_bag_inventory')
def change_bag_inventory():
    return render_template('change_bag_inventory.html')


@app.route('/change_bag_response', methods=['POST'])
def change_bag_response():

    date_today = date.today()
    bag_name = request.form['bag_name']
    operation = request.form['operation']
    quantity = request.form['quantity']
    old_quantity = db.get_bag_quantity(bag_name)
    if operation == '+':
        new_quantity = int(old_quantity) + int(quantity)
        db.update_quantity(bag_name, str(new_quantity))
        db.update_date(bag_name, date_today)
    elif operation == '-':
        new_quantity = int(old_quantity) - int(quantity)
        db.update_quantity(bag_name, str(new_quantity))
        db.update_date(bag_name, date_today)
    else:
        pass
    return render_template('change_inventory_respose.html', data="Entry recorded successfully, thank you for using this application.")


@app.route('/add_new_bag')
def add_bag_():
    return render_template('add_new_bag.html')



@app.route('/add_new_bag_respose', methods=['POST'])
def add_new_bag_response():

    bag_name = request.form['bag_name']
    quantity = request.form['quantity']
    date_today = date.today()
    if int(quantity) < 200:
        status = "Low inventory"
    else:
        status = "Ok"
    db.add_bag(bag_name, quantity, status, date_today)
    return render_template('change_inventory_respose.html', data="Entry recorded successfully, thank you for using this application.")



@app.route('/view_bag_data')
def view_bag_data():
    return render_template('sp_bag_data.html')


@app.route('/sp_bag_response', methods=['POST'])
def view_bag_data_response():
    name = request.form['bag_name']
    data = db.specific_bag_data(name)
    return render_template('change_inventory_respose.html', data=data)


@app.route('/view_report')
def view_report():
     return df.html_data




@app.route('/delete_record')
def delete_a_record():
    return render_template('delete_bag.html')


@app.route('/delete_bag', methods=['POST'])
def delete_a_bag():
    name = request.form['bag_del']
    db.delete_record(name)
    return render_template('response_delete.html', data=name)


@app.route('/home')
def home_again():
    return render_template('home.html')


@app.route('/show_warnings')
def shoe_me_warnings():
    return render_template('show_warnings.html')



@app.route('/warning_result', methods=['POST'])
def get_data_show_warnings():
    sq = request.form['min_quantity']
    name_list, quantity_list, status_list, date_list = db.show_all_warnings(sq)
    html_data = df.data_frame_2(name_list, quantity_list, status_list, date_list).to_html()
    return html_data



@app.route('/mail_report')
def sending_mail():
    index, name_list, quantity_list, status_list, date_list = db.show_all_data()
    message = sm.table(df.data_frame(index, name_list, quantity_list, status_list, date_list))
    sm.send_mail(message)
    return render_template('mail.html')





if __name__ == "__main__":
    app.run()
