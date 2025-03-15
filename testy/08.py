def recurse(n):
    return recurse(n+1)  # RecursionError: prekročená maximálna hĺbka rekurzie

recurse(1)
