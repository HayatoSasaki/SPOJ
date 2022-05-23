def series_sum(n):
    return "%.2f" % round(sum([1/(1 + x * 3) for x in range(n)]), 2)
