# If the try / except does not work then run this manually,
# pip install sympy

try:
    import sympy
except ImportError:
    try:
        import pip
        from importlib import reload

        pip.main(["install", "--user", sympy])
        reload(sympy)
    except Exception as e:
        raise Exception(e)

import sympy as sym
x,y = sym.symbols('x,y')
eq1 = sym.Eq(x+2*y,8)
eq2 = sym.Eq(x**2+y**2,13)
result = sym.solve([eq1,eq2],(x,y))
print(result)