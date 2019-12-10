class VirtualMachine:
    def __init__(self, name, ram=1, cpu=1.3, hdd=100, os="debian", status=0):
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        self.os = os
        self.status = status
        self.proc = []

    def estado(self):
        if self.status == 0:
            return 'Parada'

        elif self.status == 1:
            return 'Activa'

        elif self.status == 2:
            return 'Suspendida'

    def stop(self):
        self.status = 0
        self.proc = []

    def start(self):
        self.status = 1


    def suspend(self):
        self.status = 2


    def reboot(self):
        self.stop
        self.start

    def run(self, pid, ram, cpu, hdd):
        procesos = {
            'pid' : pid,
            'ram' : ram,
            'cpu' : cpu,
            'hdd' : hdd
        }
        self.proc.append(procesos)
        print(f'Ejecutando proceso con PID {pid} ...')
    def ram_usage(self):
        ram = 0
        for procesos in self.proc:
            ram += procesos['ram']
        ramusada = ram * 100 // self.ram
        return ramusada

    def hdd_usage(self):
        hdd = 0
        for procesos in self.proc:
            hdd += procesos['hdd']
        hddusado = hdd * 100 // self.hdd
        return hddusado

    def cpu_usage(self):
        cpu = 0
        for procesos in self.proc:
            cpu += procesos['cpu']
        cpusada = cpu * 100 // self.cpu
        return cpusada


    def __str__(self):
        return '''{} <{}> [{}] {:.2f}% RAM used | {:.2f}% CPU used | {:.2f}% HDD used'''.format(
        self.os, self.name, self.estado(), self.ram_usage(), self.cpu_usage(), self.hdd_usage())


if __name__ == '__main__':
    vm1 = VirtualMachine('Minas Tirith', 8, 2.3, 380, 'Ubuntu')

    print(vm1)
    vm1.start()
    print(vm1)
    vm1.run(1,1.7,0.3,20)
    vm1.run(4,4,0.9,100)
    vm1.run(7,0.4,1.1,250)
    print(vm1)
    vm1.stop()
    print(vm1)
    print()

    vm2 = VirtualMachine('Rohan', 6, 1.9, 250, 'Debian')

    print(vm2)
    vm2.start()
    print(vm2)
    vm2.run(2,0.6,0.7,50)
    vm2.run(5,2.1,0.2,75)
    vm2.run(8,2.5,0.4,30)
    print(vm2)
    vm2.stop()
    print(vm2)
    print()

    vm3 = VirtualMachine('Rivendel', 16, 3, 100, 'OpenSuse')
    
    print(vm3)
    vm3.start()
    print(vm3)
    vm3.run(3,2,1,25)
    vm3.run(6,0.3,0.5,12)
    vm3.run(9,1.4,0.8,65)
    print(vm3)
    vm3.stop()
print(vm3)
