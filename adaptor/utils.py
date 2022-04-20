from forest_timer import ForestTimer

def ft_timer(func):
    def timed(*args, **kwargs):
        ft = ForestTimer()
        ft.step(f'{func.__name__} args:{args,kwargs}, ')
        result = func(*args, **kwargs)
        ft.step(f'{func.__name__}')
        return result
    return timed
