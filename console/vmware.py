import ssl
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

# Información de conexión al servidor VMware
hostname = '10.0.10.107'
username = 'pe280\jporras'
password = 'Z@bb1.2022'

# Desactivar la verificación del certificado SSL
context = ssl._create_unverified_context()

# Conexión al servidor VMware
si = SmartConnect(host=hostname, user=username, pwd=password, sslContext=context)

# Obtiene el objeto rootFolder
content = si.RetrieveContent()
root_folder = content.rootFolder

# Obtiene todas las máquinas virtuales en el servidor
vm_view = content.viewManager.CreateContainerView(
    container=root_folder,
    type=[vim.VirtualMachine],
    recursive=True
)

vms = vm_view.view
vm_view.Destroy()
# Imprime el nombre de todas las máquinas virtuales
for index, vm in enumerate(vms):
    
    print("---------------------------------")
    # Imprime el nombre de la máquina virtual
    print(f'{index}. Nombre: {vm.name}')
    
    # Obtener el objeto de la configuración de la VM
    config = vm.config
    #with open(f'vm/{vm.name}.json','a', encoding='utf-8') as file:
    #    file.write(f'{config}\n')

    # Obtener el objeto padre de la máquina virtual
    parent_obj_1 = vm.parent
    parent_obj_2 = vm.parent.parent
    parent_obj_3 = vm.parent.parent.parent
    parent_obj_4 = vm.parent.parent.parent.parent

    print(f'dato 1: {type(parent_obj_1)}:{parent_obj_1.name}')
    print(f'dato 2: {type(parent_obj_2)}:{parent_obj_2.name}')
    print(f'dato 3: {type(parent_obj_3)}:{parent_obj_3.name}')
    print(f'dato 4: {type(parent_obj_4)}')

    # Obtiene el estado de encendido
    if vm.summary.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
        print('Estado: Encendida')
    else:
        print('Estado: Apagada')

    # Obtiene la cantidad de memoria RAM
    mem_size = vm.summary.config.memorySizeMB
    print(f'Memoria RAM: {mem_size} MB')

    # Obtiene la cantidad de procesadores
    cpu_count = vm.summary.config.numCpu
    print(f'Procesadores: {cpu_count}')

    print(f'Sockets: {config.hardware.numCoresPerSocket}')

    # Obtiene el tamaño del disco duro
    disk_size = vm.summary.storage.committed / (1024*1024)
    print(f'Disco Duro: {disk_size:.2f} GB')

    # Obtiene el idioma del sistema operativo
    guest_id = vm.config.guestId
    guest_full_name = vm.config.guestFullName
    print(f'Sistema Operativo: {guest_full_name} ({guest_id})')

# Desconexión del servidor VMware
Disconnect(si)
