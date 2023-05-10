import time


def time_exec(name: str, func, print_time=False, *args):
    before = time.time()
    ret = func(*args)
    after = time.time()
    if print_time:
        print("{name}: {timer}".format(name=name, timer=after - before))
    return ret, after - before


time_bank = {}


def bank_exec(name: str, func, *args):
    ret = time_exec(name, func, print_time=False, *args)
    if name in time_bank:
        time_bank[name] += ret[1]
    else:
        time_bank[name] = ret[1]
    return ret[0], time_bank[name]


def reset_bank():
    dict.clear(time_bank)
