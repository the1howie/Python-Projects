# If the try / except doesn't work then run this manually,
# pip install mpmath

try:
    import mpmath
except ImportError:
    try:
        import pip
        from importlib import reload

        pip.main(["install", "--user", mpmath])
        reload(mpmath)
    except Exception as e:
        raise Exception(e)

mpmath.mp.dps = 1000

print("e: {}".format(mpmath.e))
print("π: {}".format(mpmath.pi))