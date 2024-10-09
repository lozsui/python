from collections.abc import Callable


def expect_float(arg: float) -> None: ...
def expect_int(arg: int) -> None: ...

# int is subtype-of float
expect_float(int(4))

expect_int(int(4))
expect_int(float(1.2))
expect_int('4')

def my_foo(arg: Callable[[float], None]) -> None:
    arg(42)

my_foo(expect_int)