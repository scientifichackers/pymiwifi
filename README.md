# pyMiWiFi
A python API to the Xiaomi Mi WiFi Router web interface

(Tested on the Mi Router 3C)

## Install

`pip install pymiwifi`

## Use

```python
import pymiwifi


miwifi = pymiwifi.MiWiFi()
miwifi.login('admin_pass')

miwifi.status()
```

```
{'dev': [{'mac': 'xx:xx:xx:xx:xx:xx',
   'maxdownloadspeed': '933178',
   'upload': '28777897',
   'upspeed': '339',
   'downspeed': '194',
   'online': '1320',
   'devname': 'android-xx',
   'maxuploadspeed': '672600',
   'download': '69654908'},
  {'mac': 'xx:xx:xx:xx:xx:xx',
   'maxdownloadspeed': '1239976',
   'upload': '1249682170',
   'upspeed': '431417',
   'downspeed': '8283',
   'online': '5531',
   'devname': 'xx-pc',
   'maxuploadspeed': '744959',
   'download': '42672896'},
  {'mac': 'xx:xx:xx:xx:xx:xx',
   'maxdownloadspeed': '1074270',
   'upload': '1745315',
   'upspeed': '63',
   'downspeed': '84',
   'online': '5392',
   'devname': 'xy-pc',
   'maxuploadspeed': '37234',
   'download': '19197169'},
  {'mac': 'xx:xx:xx:xx:xx:xx',
   'maxdownloadspeed': '0',
   'upload': '0',
   'upspeed': '0',
   'downspeed': '0',
   'online': '5531',
   'devname': '5C:CF:7F:33:BD:41',
   'maxuploadspeed': '0',
   'download': '0'}],
 'code': 0,
 'mem': {'usage': 0.38, 'total': '64 M', 'hz': '800MHz', 'type': 'DDR2'},
 'temperature': 0,
 'count': {'all': 4, 'online': 3},
 'hardware': {'mac': 'xx:xx:xx:xx:xx:xx',
  'platform': 'R3L',
  'version': '2.8.50',
  'channel': 'release',
  'sn': '15516/20172849'},
 'upTime': '5573.27',
 'cpu': {'core': 1, 'hz': '575MHz', 'load': 0.3267},
 'wan': {'downspeed': '9023',
  'maxdownloadspeed': '1264691',
  'history': '460239,437753,431551,444594,443864,444399,437105,425708,444010,443786,443956,443522,437202,425671,444129,448279,443948,437086,429470,440070,444176,444169,444589,436990,424927,443799,446999,447205,431575,430753,467157,444888,444520,443385,432773,429452,443798,444853,445282,436298,425354,444444,444744,444884,442913,429838,434359,444254,444070,445424',
  'devname': 'eth0.2',
  'upload': '1296497767',
  'upspeed': '436401',
  'maxuploadspeed': '751567',
  'download': '136487233'}}

```

## Advanced

**If there's an endpoint that's not available in the API, you can just -**

`miwifi.get_api_endpoint('xqsystem/wifi_macfilter_info')`

(Use chrome dev tools' "Network" Tab to see these endpoints)