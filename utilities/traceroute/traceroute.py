from os import system


def tracer():
    ip = input("IP: ")
    max_time = input("Max time: ")
    max_jump = input("Max jumps: ")

    system(f"tracert -w {max_time} -h {max_jump} {ip}")
    