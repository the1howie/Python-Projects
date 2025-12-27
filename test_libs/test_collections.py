try:
    import collections
except ImportError:
    try:
        import pip
        from importlib import reload

        pip.main(["install", "--user", collections])
        reload(collections)
    except Exception as e:
        raise Exception(e)

d = {'b':234, 'a':343, 'd':3900, 'c':1112}
od = collections.OrderedDict(d.items())
print(od)