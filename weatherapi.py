#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json

AK = "K1SSTviL7hVkldh2gOd9G3Ie"


class WeatherAPI(object):
    """docstring for Baidu WeatherAPI"""
    def __init__(self):
        self.ak = AK

    def getCityWeatherData(self, c):
        url = "http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=%s" % (c, self.ak)
        text = urllib2.urlopen(url).read()
        json_text = json.loads(text)
        data = []
        # 1
        item1 = {}
        item1['city'] = json_text['results'][0]['currentCity']
        item1['pm'] = json_text['results'][0]['pm25']
        item1['date'] = json_text['date']
        # 2
        item2 = {}
        item2['weather_data'] = json_text['results'][0]['weather_data']
        # 3
        item3 = {}
        item3['index'] = json_text['results'][0]['index']
        return (item1, item2, item3)

