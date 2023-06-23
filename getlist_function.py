# -*- coding: utf-8 -*-
import json

# Get Err List
def geterrlist(json_data):
    errlist = []

    # Read ERR.log
    with open(json_data["logfile_name"], 'r') as f:
        datalist = f.read().splitlines()

        for data in datalist:
            data_obj = json.loads(data)
            errlist.append(data_obj)

    return errlist
