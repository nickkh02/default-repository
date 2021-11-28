import json


with open('tests.json', 'r') as f1, open('values.json', 'r') as f2:
    tests = json.load(f1)
    values = json.load(f2)

def flatten(l):
    out = []
    if isinstance(l, (list, tuple)):
        for item in l:
            out.extend(flatten(item))
    elif isinstance(l, (dict)):
        for dictkey in l.keys():
            out.extend(flatten(l[dictkey]))
    elif isinstance(l, (str, int)):
        out.append(l)
    return out

b1 = flatten(values)
bdict = dict(zip(b1[::2], b1[1::2]))  # Тут все работает как надо
print(bdict)

first = tests

def changevalue(js_test, js_values):
    for k, v in js_values.items():
        if (js_test['id']) == k:
            js_test['value'] = v

def deepdown(json):
    if isinstance(json, dict) and len(json.items()) > 3:
        changevalue(json, bdict)
        for item, value in json.items():
            if isinstance(item, dict):
                deepdown(item)
            elif isinstance(value, (dict)):
                deepdown(value)
            elif isinstance(value, (list)):
                if len(value) > 1:
                    for i in value:
                        deepdown(i)
                else:
                    deepdown(*value)
            elif isinstance(item, list):
                deepdown(item)
    elif isinstance(json, dict) and len(json.items()) == 3:
        changevalue(json, bdict)
    elif isinstance(json, dict) and len(json.items()) < 3:
        deepdown(list(json.values())[0])
    elif isinstance(json, list):
        if len(json) > 1:
            for i in json:
                deepdown(i)
        else:
            deepdown(*json)
    else:
        pass

deepdown(first)

with open('report.json', 'w') as f:
    json.dump(first, f, ensure_ascii=False, indent=4)
