import psutil
from helpers import parser, prettytable
from data import templates_


class Memory:
    @staticmethod
    def get_info() -> list:
        mem = psutil.virtual_memory()
        return parser([mem.total, mem.available, mem.used, mem.free, mem.cached])


class Network:
    @staticmethod
    def get_info() -> list:
        net = [[p.fd, p.family, p.type, p.laddr.ip, p.laddr.port, p.status] for p in psutil.net_connections()]
        return parser(net)


class Processes:
    @staticmethod
    def get_info() -> list:
        return parser([p.info for p in psutil.process_iter(["pid", "name", "username"])])


def show(mem, nets, procs):
    prettytable([templates_["memory_template"], mem], "MEMORY INFO")
    for net in nets:
        prettytable([templates_["net_template"], net], "NETWORK INFO")
    for proc in procs:
        prettytable([templates_["procs_template"], proc], "PROCESSES INFO")


def main():
    mem_info = Memory.get_info()
    net_info = Network.get_info()[:3]
    procs_info = Processes.get_info()[:3]
    show(mem_info, net_info, procs_info)


if __name__ == "__main__":
    main()
