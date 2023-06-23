# -*- coding: utf-8 -*-
import json, hashlib

# login check
def login_check(form_obj):
    input_user = form_obj["mtg_username"]
    input_pw   = form_obj["mtg_password"]

    if input_user is not None and len(input_user):
        if input_pw is not None and len(input_pw):
            # input password hash
            input_pw_hash = hashlib.md5(input_pw.encode("utf-8")).hexdigest()

            # user json
            f = open("static/config/user.json", 'r')
            json_data = json.load(f)

            # getUserPass
            try:
                json_pw = json_data[input_user]

               # Check
                if json_pw is not None:
                    if json_pw == input_pw_hash:
                        return True
                    else:
                        return False
                else:
                    return False
            
            except Exception as e:
                return False
