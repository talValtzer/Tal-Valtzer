from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage_func():
    return render_template('HomePage.html')


@app.route('/ContactPage')
def cont_func():
    return render_template('ContactPage.html')


@app.route('/assignment3_1')
def about_page():
    user_info = {'First_Name': 'Tal', 'Last_name': 'Valtzer'}

    hobbies = ('drawing', 'reading', 'traveling', 'TV', 'sea')
    return render_template('assignment3_1.html',
                           user_info=user_info,

                           hobbies=hobbies)
@app.route('/log_in', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in user_dict:
            pas_in_dict = user_dict[username]
            if pas_in_dict == password:
                session['username'] = username
                session['logedin'] = True
                return render_template('LogIn.html',
                                       message='Success',
                                       username=username)
            else:
                return render_template('LogIn.html',
                                       message='Wrong password!')
        else:
            return render_template('LogIn.html',
                                   message='Please sign in!')
    return render_template('LogIn.html')


@app.route('/assignment3_2', methods=['GET', 'POST'])
def ass3():
    if request.method=='GET':
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            if user_name in user_dict:
                return render_template('assignment3_2.html',
                                       user_name=user_name,
                                       user_email=user_dict[user_name][0],
                                       user_Firstname= user_dict[user_name][1],
                                       user_Lastname=user_dict[user_name][2],
                                       user_age=user_dict[user_name][3]
                                       )

            else:
                return render_template('assignment3_2.html',
                                       message='Product not found.')


    return render_template('assignment3_2.html',
                           user_dict=user_dict)



user_dict = {
    'Tal_val': ['Tal@gmail.com','Tal', 'Val', '25']

}


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'




if __name__ == '__main__':
    app.run()
