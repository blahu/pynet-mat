
from net_system.models import NetworkDevice,SnmpCredentials
import django


if __name__ == "__main__":

    django.setup()

    v3_creds, created = SnmpCredentials.objects.get_or_create(
        community = 'pysnmp',
        auth_key  = 'galileo1',
        encrypt_key  = 'galileo1',
    )
    print v3_creds

    if created:
        v3_creds.save()

    ciscos = ['pynet-rtr1', 'pynet-rtr2']

    for rtr in ciscos:
        cisco = NetworkDevice.objects.get(device_name=rtr)
        print cisco
        cisco.snmp_creds = v3_creds
        cisco.save()

