# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, session, redirect, url_for
from login_function import login_check
from requesthandle_function import requestFormHandler
from getlist_function import geterrlist
import json, logging

app = Flask(__name__)

# Secret
app.secret_key = b'_5#y2L"F9Q8z\n\xec]/'

# Logger
f = open("static/config/default.json", 'r')
json_data = json.load(f)
#
app.logger.setLevel(logging.ERROR)
log_handler = logging.FileHandler(json_data["logfile_name"])
log_handler.setLevel(logging.ERROR)
app.logger.addHandler(log_handler)


# Root
@app.route("/")
def index():
    return render_template('index.html', title='障害発生アプリ')

# Logout
@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# Menu
@app.route("/menu", methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        check_result = login_check(request.form)
        if check_result:
            session['username'] = request.form["mtg_username"]
            return render_template('menu.html', title='メニュー画面')
        else:
            return render_template('index.html', title='障害発生アプリ', message="UserID,またはPasswordが間違っています。")
    else:
        if session['username'] is not None and len(session['username']) > 0:
            return render_template('menu.html', title='メニュー画面')
        else:
            return redirect(url_for('index'))   

# PutData
@app.route("/putdata")
def putData():
    if session['username'] is not None and len(session['username']) > 0:
        return render_template('putdata.html', title='障害登録画面')
    else:
        return redirect(url_for('index'))

# PostData
@app.route('/post', methods=['POST'])
def post():
    if session['username'] is not None and len(session['username']) > 0:
        if request.method == 'POST':
            # data setting
            inst_dict = requestFormHandler(request.form, json_data)

            if len(inst_dict.keys()) > 0:
                # ERR Create
                try:
                    app.logger.error(json.dumps(inst_dict))
                    return render_template('complete.html', title='障害登録完了画面', form_dict=inst_dict, message="登録完了しました。")
                except:
                    return render_template('putdata.html', title='障害登録画面', message='登録に失敗しました。')
            else:
                return render_template('putdata.html', title='障害登録画面', message='データが入力されていません。')
    
        else:
            return render_template('putdata.html', title='障害登録画面', message="Only post data allowed.")
    else:
        return redirect(url_for('index'))

# ReferList
@app.route("/eventlist")
def eventlist():
    if session['username'] is not None and len(session['username']) > 0:
        resultDataList = geterrlist(json_data)
        return render_template('eventlist.html', title='障害一覧画面', resultList=resultDataList)
    else:
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8032, debug=True)
