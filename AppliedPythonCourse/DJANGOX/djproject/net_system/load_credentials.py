from net_system.models import NetworkDevice,Credentials
import django





if __name__ == "__main__":

    django.setup()

    cisco_creds = Credentials.objects.get_or_create(
        username = 'pyclass',
        password = '88newclass',
        description = 'Cisco router credentials'
    )
    print cisco_creds

    arista_creds = Credentials.objects.get_or_create(
        username = 'admin1',
        password = '99saturday',
        description = 'Arista credentials'
    )
    print arista_creds

    net_devices = NetworkDevice.objects.all()

    for d in net_devices:
        if 'arista' in d.device_class:
            d.credentials = arista_creds
        if 'cisco' in d.device_class:
            d.credentials = cisco_creds
       print ("name={} class={} creds={}".format(d.device_name,d.device_class, d.credentials))
       d.save()
    

