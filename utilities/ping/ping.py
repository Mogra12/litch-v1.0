from os import system


def pingg():
    ip_domain = input("IP/Domain: ")

    system(f"ping {ip_domain}")
    