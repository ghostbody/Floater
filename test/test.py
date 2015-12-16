import json

if __name__ == '__main__':
    f = open("data.json")
    s = json.load(f)
    s[0].key
    print s
