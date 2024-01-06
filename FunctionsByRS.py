class Func:

    @staticmethod
    def animationtype(x, z):
        import time as t
        y = list(x)
        for char in y:
            t.sleep(z)
            print(char, end="")

    @staticmethod
    def create(y):
        with open(y, "a") as f:
            pass

    @staticmethod
    def clearcmd():
        import os
        os.system('cls')

    @staticmethod
    def getip():
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        print("Hostname: ", hostname)
        print("IPv4 Address: ", ip_address)
