#!/usr/bin/env python

from common.parse_netflow import parse_netflow
from canari.framework import configure
from common.entities import DumpFile
from canari.maltego.message import UIMessage, Field, MatchingRule
from canari.maltego.entities import IPv4Address

__author__ = 'Adam Maxwell'
__copyright__ = 'Copyright 2015, Gotflow Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Adam Maxwell'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


@configure(
    label='[NF] - Get Source IP',
    description='Get Source IPs from dump file',
    uuids=['netflow.v2.dump_2_getsourceip'],
    inputs=[('Netflow', DumpFile)],
    debug=True
)
def dotransform(request, response):
    try:
        dump = request.fields['dumpfile']
    except:
        dump = request.value
    x = parse_netflow(dump)
    for i in x:
        sip = i[4]
        sip = sip.split(':')[0]
        proto = i[3]
        e = IPv4Address(sip)
        e += Field('dumpfile', dump, displayname='Dump File', matchingrule='loose')
        # e.linklabel = proto
        if proto == 'TCP':
            e.linkcolor = 0xff0000
        if proto == 'UDP':
            e.linkcolor = 0x002bff
        if proto == 'ICMP':
            e.linkcolor = 0x2f9a0d
        response += e
    return response
