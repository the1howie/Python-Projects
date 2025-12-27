try:
    import numpy
except ImportError:
    try:
        import pip
        from importlib import reload

        pip.main(["install", "--user", numpy])
        reload(numpy)
    except Exception as e:
        raise Exception(e)

numpy.set_printoptions(precision=200)
x = numpy.array([numpy.e, numpy.pi])
print(x)