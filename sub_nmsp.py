#!/Users/fsedanoc/python/subscribe/netconf/bin/python

from ncclient import manager
from ncclient.xml_ import to_ele
from lxml import etree

rpc = """
<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications" xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
    <stream>yp:yang-push</stream>
    <yp:xpath-filter>/wireless-nmsp-oper:nmsp-oper-data/cmx-connection/active</yp:xpath-filter>
    <yp:dampening-period>0</yp:dampening-period>
</establish-subscription>
"""

root = etree.fromstring(rpc)

host = "1.1.1.1"
username = "user"
password = "pass"

if __name__ == '__main__':
    with manager.connect(host=host,
                         port=830,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False) as m:

        response = m.dispatch(to_ele(rpc))
        print("Waiting for notify\n")
        while True:
            n = m.take_notification()
            print(n.notification_xml)
            active = n._root_ele.find('.//{http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-nmsp-oper}active').text
            if active == "true":
                print(f"NMSP connection is ACTIVE\n")
            else:
                print(f"NMSP connection is INACTIVE\n")
