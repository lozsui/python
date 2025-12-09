from decimal import Decimal, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP

def test_first():
    a = Decimal('1.41421356')
    b = a.quantize(Decimal('1.000'))
    c = a.quantize(Decimal('1.0000'))
    d = a.quantize(Decimal('1.00'), rounding=ROUND_HALF_DOWN)
    e = a.quantize(Decimal('1.00'), rounding=ROUND_HALF_EVEN)
    f = a.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)
    assert b == Decimal('1.414')
    assert c == Decimal('1.4142')
    assert d == Decimal('1.41')
    assert e == Decimal('1.41')
    assert f == Decimal('1.41')
