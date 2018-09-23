import wmi

def change_IP():
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled = True)
    nic = nic_configs[0]
    
    ip = u'192.168.0.12'
    subnetmask = u'255.255.255.0'
    gateway = u'192.168.0.1'

    nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])

change_IP()
