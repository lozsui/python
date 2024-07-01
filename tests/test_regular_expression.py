import re

def test_re_sub_nicest():
    pattern = re.compile(
        rb'''
        (?P<start_tag><MessageDateTime\ v=")
        (\d{4}-\d{2}-\d{2}T\d{2}:\d{2})
        (?P<end_tag>"/>)
        ''',
        re.VERBOSE)
    byte_data = b'<MessageDateTime v="2024-06-01T15:03"/>'
    assert re.sub(
        pattern,
        (rb'\g<start_tag>'
         rb'2099-06-01T15:03'
         rb'\g<end_tag>')
        ,
        byte_data, count=1) == b'<MessageDateTime v="2099-06-01T15:03"/>'

def test_re_match_1():
    pattern = re.compile(b'(<)(MessageDateTime)( v=")(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})("/>)')
    byte_data = b'<MessageDateTime v="2024-06-01T15:03"/>'
    result = re.match(pattern, byte_data)
    assert b'<MessageDateTime v="2024-06-01T15:03"/>' == result[0]
    assert b'<' == result[1]
    assert b'MessageDateTime' == result[2]
    assert b' v="' == result[3]
    assert b'2024-06-01T15:03' == result[4]
    assert b'"/>' == result[5]

def test_re_match_2():
    pattern = re.compile(b'(<MessageDateTime v=")(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})("/>)')
    byte_data = b'<MessageDateTime v="2024-06-01T15:03"/>'
    result = re.match(pattern, byte_data)
    assert b'<MessageDateTime v="2024-06-01T15:03"/>' == result[0]
    assert b'<MessageDateTime v="' == result[1]
    assert b'2024-06-01T15:03' == result[2]
    assert b'"/>' == result[3]

def test_re_sub_1():
    # re.sub(pattern, repl, string, count=0, flags=0)
    pattern = re.compile(b'(<MessageDateTime v=)(")(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})(")(/>)')
    byte_data = b'<MessageDateTime v="2024-06-01T15:03"/>'
    assert re.sub(pattern, rb'\1"2099-06-01T15:03"\5', byte_data, count=1) == b'<MessageDateTime v="2099-06-01T15:03"/>'

def test_re_sub_2():
    pattern = re.compile(
        rb'''
        (?P<start_tag><MessageDateTime\ v=")
        (\d{4}-\d{2}-\d{2}T\d{2}:\d{2})
        (?P<end_tag>"/>)
        ''',
        re.VERBOSE)
    byte_data = b'<MessageDateTime v="2024-06-01T15:03"/>'
    assert re.sub(pattern, rb'\g<start_tag>2099-06-01T15:03\g<end_tag>', byte_data, count=1) == b'<MessageDateTime v="2099-06-01T15:03"/>'
