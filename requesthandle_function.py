# -*- coding: utf-8 -*-
import datetime, json

# Request Form Handle
def requestFormHandler(form_obj, json_data):
    form_dict = {}
    
    # now datetime timezone + 9
    now = datetime.datetime.now() + datetime.timedelta(hours=9)

    # err_id
    form_dict.setdefault("err_id", "err-" + str(int(now.timestamp())))
    
    # timestamp  
    form_dict.setdefault("timestamp", str(now))

    # system_name
    if form_obj['system_name'] is not None and len(form_obj['system_name']) > 0:
        form_dict.setdefault("system_name", form_obj['system_name'])
    else:
        form_dict.setdefault("system_name", json_data["system_name"])
    
    # err_target
    if form_obj['err_target'] is not None and len(form_obj['err_target']) > 0:
        form_dict.setdefault("err_target", form_obj['err_target'])
    else:
        form_dict.setdefault("err_target", json_data["err_target"])

    # err_code
    if form_obj['err_code'] is not None and len(form_obj['err_code']) > 0:
        form_dict.setdefault("err_code", form_obj['err_code'])
    else:
        form_dict.setdefault("err_code", json_data["err_code"])
    
    # context
    if form_obj['context'] is not None and len(form_obj['context']) > 0:
        form_dict.setdefault("context", form_obj['context'])
    else:
        form_dict.setdefault("context", "")

    # memo
    if form_obj['memo'] is not None and len(form_obj['memo']) > 0:
        form_dict.setdefault("memo", form_obj['memo'])
    else:
        form_dict.setdefault("memo", "")

    return form_dict
