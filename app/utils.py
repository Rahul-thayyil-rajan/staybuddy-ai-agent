def normalize_time(t):
    if not t:
        return 0

    h, m = map(int, t.split(":"))
    return h * 60 + m