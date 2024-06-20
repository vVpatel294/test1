def items_after_four(iter: list) -> int:
    if len(iter) <= 4:
        return 0
    else:
        return len(iter) - 4
