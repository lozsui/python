

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

def test_multiply_string():
    my_str = "3"
    assert my_str * 3 == "333"
