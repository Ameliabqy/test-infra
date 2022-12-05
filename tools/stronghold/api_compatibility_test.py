"""Contains functions to test API compatibility changes."""


def removed_function() -> None:
    pass


def complex(
    a: int,
    /,
    b: int,
    *args,
    c: int,
    **kwds,
) -> None:
    pass
