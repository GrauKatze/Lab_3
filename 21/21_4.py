def defractalize(fractal=list()):
    for i in fractal:
        if i == fractal:
            fractal.remove(i)
