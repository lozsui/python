def test_normal():
    print("\nnormal print")


def test_fail():
    print("\nprint failing test")
    assert False


def test_disabled(capsys):
    with capsys.disabled():
        print("\ncapsys disabled print")
