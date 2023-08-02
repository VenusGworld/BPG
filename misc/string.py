def ascii_lowercase() -> str:
    return "".join(chr(i) for i in range(97, 123))


def ascii_uppercase() -> str:
    return "".join(chr(i) for i in range(65, 91))


def ascii_number() -> str:
    return "".join(chr(i) for i in range(48, 58))


def ascii_special() -> str:
    return "".join(
        chr(i) for i in list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127)))
