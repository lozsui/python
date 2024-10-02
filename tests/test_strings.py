"""
Inspired by https://github.com/PacktPublishing/The-Complete-Python-Course/tree/master/1_intro/lectures
"""
import datetime


def test_multiline():
    my_multiline_string = """Dear Reader,
    enjoy what you see!

    Regarads,
    Sam

    PS: Run me like 'pytest -s -k test_multiline'
    """
    print(my_multiline_string)

def test_f_string():
    age = 20
    my_age = f"I am {age} years old."
    assert my_age == "I am 20 years old."

class FStringDemo():

    def __str__(self):
        return "Instance of FStringDemo"

def test_f_string2():
    o = FStringDemo()
    assert f"{o}" == "Instance of FStringDemo"

def test_f_string_with_date():
    my_date = datetime.datetime.now()
    print(f"Todays date is {my_date}")

def test_format_string():
    name = "lozsui"
    greeting = f"Hello {name}!"
    assert greeting == "Hello lozsui!"
    name = "Peter"
    assert greeting == "Hello lozsui!"
    greeting = "Hello {}!"
    assert greeting.format(name) == "Hello Peter!"
    name = "lozsui"
    assert greeting.format(name) == "Hello lozsui!"

def test_format_string2():
    name = "lozsui"
    greeting = "Hello {name}!"
    assert greeting.format(name=name) == "Hello lozsui!"

def test_json_string():
    hostname = "HOSTNAME"
    port = 4242
    config = """{{"credentials":{{"username":"test_user","password":"test_pwd"}},"hostname":"{hostname}","port":"{port}"}}""".format(hostname=hostname, port=port)
    print(config)
    assert config == """{"credentials":{"username":"test_user","password":"test_pwd"},"hostname":"HOSTNAME","port":"4242"}"""

def test_multiply_string():
    my_str = "3"
    assert my_str * 3 == "333"
