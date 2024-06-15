from json5 import dumps

def indented_dumps(obj):
    return dumps(obj, indent=1)

def test_json_dump_empty_dict():
    assert indented_dumps({}) == '{\n}'

def test_json_dump_dict():
    assert indented_dumps({1:1}) == '{\n 1: 1\n}'

def test_json_dump_nested_empty_dict():
    assert indented_dumps([{}]) == '[\n {\n }\n]'

def test_json_dump_nested_dict():
    assert indented_dumps([{1:1}]) == '[\n {\n  1: 1\n }\n]'
