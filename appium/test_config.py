#!/usr/bin/env python

def get_test_config():
    config = {
        'platformName': 'Android',
        'platformVersion': '${platformVersion}',
        'deviceName': '${deviceName}',
        'app': "${app}",
        'newCommandTimeout': 30,    
        'automationName': 'Appium'
    }

    return config

def get_uri():
    return "http://localhost:${port}/wd/hub"