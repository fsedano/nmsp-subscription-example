# Small demo to subscribe for NMSP connection status for 9800 wireless controller

## How to run:
- Update user, password and hostname
- pip install -r requirements.txt
- Enable NETCONF on the controller:
    ```fsedanoc-wlc(config)#netconf-yang```

## Example output


![Animated demo](https://github.com/fsedano/nmsp-subscription-example/blob/master/demo.gif)


```(netconf) FSEDANOC-M-54DR:netconf fsedanoc$ ./sub_nmsp.py
NMSP connection is INACTIVE

<?xml version="1.0" encoding="UTF-8"?>
<notification xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0"><eventTime>2019-11-19T21:20:21.93Z</eventTime><push-change-update xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push"><subscription-id>2147483671</subscription-id><datastore-changes-xml><yang-patch xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-patch"><patch-id>null</patch-id><edit><edit-id>edit1</edit-id><operation>merge</operation><target>/nmsp-oper-data/cmx-connection=64.103.36.133</target><value><cmx-connection xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-nmsp-oper"><active>true</active></cmx-connection></value></edit></yang-patch></datastore-changes-xml></push-change-update></notification>

NMSP connection is ACTIVE

<?xml version="1.0" encoding="UTF-8"?>
<notification xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0"><eventTime>2019-11-19T21:20:25.22Z</eventTime><push-change-update xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push"><subscription-id>2147483671</subscription-id><datastore-changes-xml><yang-patch xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-patch"><patch-id>null</patch-id><edit><edit-id>edit1</edit-id><operation>merge</operation><target>/nmsp-oper-data/cmx-connection=64.103.36.133</target><value><cmx-connection xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-nmsp-oper"><active>false</active></cmx-connection></value></edit></yang-patch></datastore-changes-xml></push-change-update></notification>

NMSP connection is INACTIVE
```