def test_map_one():
    str_list = ['blah ', ' blub', ' foo ', '   bar             ']
    stripped_str_list = list(map(str.strip, str_list))
    for i in range(0, len(str_list)):
        assert str_list[i].strip() == stripped_str_list[i]
