from global import *

import os.path
import json

class data(object):
    """docstring for data"""
    
    def __init__(self, filename):
        super(data, self).__init__()
        dataFile = open(os.path.join(data_path, filename))
        self.allData = allData = json.load(self.dataFile)

    def find(self, key, value):
        result  = []
        for each in self.allData:
            tempValue = each.get(key)
            if tempValue != None and tempValue == value:
                result.append(each)
        return result

    def insert(self, jsonString):
        self.allData.append(json.loads(jsonString))

    def delete(self, key, value):
        for each in self.allData[:]:
            tempValue = each.get(key)
            if tempValue != None and tempValue == value:
                allData.remove(each)

    def modify(self, key, value, jsonString):
        self.delete(key, value)
        self.insert(jsonString)

    def __del__(self):
        dataFile = open(os.path.join(data_path, filename))
        json.dump(self.allData, dataFile)
