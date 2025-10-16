import importlib

for mod in ('pandas_profiling','ydata_profiling'):
    try:
        m = importlib.import_module(mod)
        ver = getattr(m, '__version__', 'unknown')
        print(f"{mod} available: {ver}")
    except Exception as e:
        print(f"{mod} not available -> {type(e).__name__}: {e}")
