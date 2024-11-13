def setup(k):
    kernel = k.get("kernel")

    ti_system = kernel.lib()

    k.mudules["ti_system"] = ti_system
