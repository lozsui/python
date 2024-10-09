def show_count(count: int, singular: str, plural: str | None = None) -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}s'

def parse_token(token: str) -> str | float:
    try:
        return float(token)
    except ValueError:
        return token
