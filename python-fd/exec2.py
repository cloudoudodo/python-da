import re
import sys


def get_address(port):
    f = open()

    while ture:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break

        if not data:
            break
        try:
            PORT = re.match(r'\S+', data).group()
        except Exception as e:
            print(e)
            continue

        if PORT == port:
            pattern = r'address is (\w{4}.\w{4}.\w{4})'
            addr = re.search(pattern, data).group(1)
            return addr


if __name__ = "__main__":
    port = sys.argv[1]
    print(get_address(port))
