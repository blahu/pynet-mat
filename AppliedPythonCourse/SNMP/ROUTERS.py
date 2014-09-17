
ROUTERS = {
    'pynet-rtr1' : {
        'IP' : '50.242.94.227',
        'SNMP Port' : 7961,
        'SNMP Community' : 'galileo',
        'snmp_v' : 3,
        'snmp_user' : ('pysnmp', 'galileo1', 'galileo1'),
    },
    'pynet-rtr2' : {
        'IP' : '50.242.94.227',
        'SNMP Port' : 8061,
        'SNMP Community' : 'galileo',
        'snmp_v' : 3,
        'snmp_user' : ('pysnmp', 'galileo1', 'galileo1'),
    },
    'pymat_rtr1' : {
        'IP' : '10.1.1.1',
        'SNMP Port' : 161,
        'SNMP Community' : 'galileo',
        'snmp_v' : 2,
    },
    'pymat_rtr2' : {
        'IP' : '10.1.1.2',
        'SNMP Port' : 161,
        'SNMP Community' : 'galileo',
        'snmp_v' : 3,
        'snmp_user' : ('pysnmp', 'galileo1', 'galileo1'),
    },
}

