import requests
from flask import jsonify, request
from . import proxy


@proxy.route('/proxy/mingyan/')
def mingyan():
    page, row = request.args.get('page'), request.args.get('rows')
    app_key = 'd12157620d654f65a037a1939c4ef2e0'
    api_url = 'https://api.avatardata.cn/MingRenMingYan/LookUp'
    data = {'key': app_key, 'keyword': '勤奋', 'page': page, 'rows': row, 'dtype': 'json', 'format': False}
    resp = requests.get(url=api_url, data=data)
    resp = jsonify(resp.text)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@proxy.route('/proxy/weather/')
def weather():
    app_key = 'd7d40a481c384eb49c8f0e4e83f59a91'
    api_url = 'http://api.avatardata.cn/Weather/Query'
    data = {'key': app_key, 'cityname': '北京', 'dtype': 'json', 'format': False}
    resp = requests.get(url=api_url, data=data)
    resp = jsonify(resp.text)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

