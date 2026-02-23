"""
Mit 'pytest .\test_print.py' wird nur 'capsys disabled print'
ausgegeben.

Mit 'pytest -s .\test_print.py' wird 'normal print' und
'capsys disabled prin' ausgegeben.
"""

def test_normal():
    print("\nnormal print")


def test_disabled(capsys):
    with capsys.disabled():
        print("\ncapsys disabled print")
