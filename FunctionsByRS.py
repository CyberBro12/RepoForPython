class Func:

    @staticmethod
    def animation_type(x, z):
        import time as t
        lines = x.split('\n')  # Split input into lines
        for line in lines:
            line = line.rstrip()  # Remove trailing whitespace
            for char in line:
                t.sleep(z)
                print(char, end='')
            print()  # Add newline after each line

    @staticmethod
    def create(y):
        open(y, "a")

    @staticmethod
    def clear_cmd():
        import os
        os.system('cls')

    @staticmethod
    def getip():
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        print("Hostname: ", hostname)
        print("IPv4 Address: ", ip_address)

# Version - 2
