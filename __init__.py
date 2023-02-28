import configparser
import json
import os
import requests

global token
global server_


module = GetParams('module')

if module == 'Login':
    ruta_ = GetParams("ruta_")

    config = configparser.ConfigParser()
    config.read(ruta_)
    email_ = config.get('USER', 'user')
    pass_ = config.get('USER', 'password')
    server_ = config.get('USER', 'server')

    try:
        data = {'email': email_, 'password': pass_}
        res = requests.post(server_ + '/api/auth/login', data,
                            headers={'content-type': 'application/x-www-form-urlencoded'})

        if res.status_code == 200:
            res = res.json()
            if res['success']:
                token = res['data']
            else:
                raise Exception(res['message'])
        else:
            raise Exception(res.content)

    except Exception as e:
        PrintException()
        raise e

if module == 'UploadDocument':
    document = GetParams("document")
    template_id = GetParams("template_token")
    result = GetParams("result")

    if not document:
        raise Exception("Missing document")
    if not template_id:
        raise Exception("Missing template token")

    try:
        data = {'template_token': template_id}
        tmp = open(document, 'rb')
        res = requests.post(server_ + '/process/async', data=data,
                            files={'file': tmp}, headers={'Authorization': 'Bearer ' + token})

        if res.status_code == 200:
            if result:
                print(res.json())
                SetVar(result, res.json()['data'])
        else:
            raise Exception(res.json()['message'])
        try:
            tmp.close()
        except:
            pass
    except Exception as e:
        PrintException()
        raise e
    finally:
        tmp.close()

if module == 'UploadFolder':
    folder = GetParams('folder')
    template_id = GetParams('template_token')
    result = GetParams('result')

    if not folder:
        raise Exception('Missing folder')

    if not os.path.isdir(folder):
        raise Exception("The path entered is not a valid directory")

    if not template_id:
        raise Exception("Missing template token")
    try:
        files = {}
        data = {'template_token': template_id}
        for f in os.listdir(os.path.normpath(folder)):
            if os.path.basename(f).endswith('jpg') or os.path.basename(f).endswith('jpeg') or os.path.basename(f).endswith('png') or os.path.basename(f).endswith('pdf'):
                files[os.path.splitext(f)[0]] = open(os.path.join(folder, f), 'rb')
        res = requests.post(server_ + '/process/batch', files=files, data=data, headers={'Authorization': 'Bearer ' + token})
        if res.status_code == 200:
            if result:
                SetVar(result, res.json()['data'])
        else:
            raise Exception(res.json()['message'])
    except Exception as e:
        PrintException()
        raise e

if module == 'CheckResultStatus':
    token_ = GetParams('token_')
    result = GetParams('result')

    if not token_:
        raise Exception('Missing token')

    try:
        res = requests.post(server_ + '/result/check/' + token_, headers={'Authorization': 'Bearer ' + token})
        if res.status_code == 200:
            if result:
                SetVar(result, res.json()['data'])
        else:
            raise Exception(res.text)
    except Exception as e:
        PrintException()
        raise e

if module == 'GetResult':
    token_ = GetParams('token_')
    result_ = GetParams('result_')

    if not token_:
        raise Exception('Missing token')

    try:
        res = requests.post(server_ + '/result/get/' + token_, headers={'Authorization': 'Bearer ' + token})
        if res.status_code == 200:
            tmp = res.json()['data']
            tmp = json.loads(tmp['result'])
            if result_:
                SetVar(result_, tmp)
        else:
            raise Exception(res.text)
    except Exception as e:
        PrintException()
        raise e