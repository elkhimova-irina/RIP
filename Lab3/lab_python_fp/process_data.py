import json
import sys
from gen_random import gen_random
from print_result import print_result
from unique import Unique
from cm_timer import cm_timer_1, cm_timer_2
from field import field
import time


path = "/Users/irinaelkhimova/RIP_labs/Lab3/lab_python_fp/data_light.json"



with open(path, encoding='utf8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, 'job-name'), ignore_case=True)), key=lambda x: str.casefold(x))


@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x.lower(), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return dict(zip(arg, gen_random(len(arg), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

    with cm_timer_2():
        f4(f3(f2(f1(data))))