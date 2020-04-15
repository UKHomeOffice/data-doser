#!/usr/bin/env python3
"""
Template functions to generate test data.
"""

__author__ = "David Morris"
__version__ = "0.1.0"
__license__ = "MIT"

import string
import random
from datetime import datetime, timedelta

def get_template_from_file(template_filename):
    """Return the template string from a file."""
    f = open(template_filename)
    s = string.Template(f.read())
    return s


def process_template(template, values):
    t = template
    return t.safe_substitute(values)


def get_template(values):
    t = string.Template("""UNB+UNOB:2+SGNV+COASTS+191021:1052+SRC-$src_number'
UNH+ZD19052044+CUSCAR:D:95B:UN:LOT10'
BGM+85+ZD19052044+9'
DTM+137:201910210852:203'
RFF+SSX:POR121944I'
NAD+MS+SCR:172:20'
TDT+20+ZD19452+1++SGNV:172:20:MS INC+++C6KD8:103::TEST SHIP:'
LOC+60+GBPM1::139'
DTM+132:201910290330:203'
DTM+232:201910290330:203'
GIS+23'
EQD+BB+373MOB907417+9999:ZZZ:5++3+5'
MEA+AAE+G+KGM:55814'
MEA+AAE+AAW+MTQ:0'
CNI+1+SGNV373MOB907417'
RFF+BM:SGNV373MOB907417'
CNT+7:55814:KGM'
CNT+8:60'
LOC+9+CRMOB::139'
LOC+11+$loc_11_prefix$loc_11_number::139'
LOC+76+CRMOB::139'
GIS+23'
NAD+SH+22942+MIKE BASSOON, TEST ADDRESS, LEEDS, LS1 1QQ'
NAD+CN+MOB00125+JOHN SMITH, FRUIT IMPORTS, A WAREHOUSE'
NAD+CZ+MOB00126+A FARMER, FRUIT EXPORTS, A FARM'
GID+1+2880:UNT'
FTX+AAA+++Bananas including plaintains, fresh or dried'
MEA+AAE+G+KGM:55814'
SGP+373MOB907417+60'
PCI+24+HS CODE 080390'
UNT+313+ZD19052044'
UNZ+1+SRC-${src_number}'""")
    return t.safe_substitute(values)


def get_loc_11(number=1):
    """Turn the the number for loc_11 into a string"""
    n = str(number)
    return n


def get_src_number(i=1, pad=6):
    """This one gets zfilled by a pad of default 6 0."""
    return str(i).zfill(pad)


def get_initial_values(startindex):
    now = datetime.now()
    values = {
        'loc_11_prefix': 'GBPM',
        'loc_11_number': get_loc_11(number=startindex),
        'src_number': get_src_number(i=startindex),
        'ship' : f"TEST SHIP {random_string(size=10)}",
        'send_date' :  get_date(now),
        'send_time' : get_time(now),
        'msg_ref' : f"MREF{random_string(size=10)}"
    }
    print(f"Ship: {values['ship']}")
    return values

def get_date(mydate):
    return mydate.strftime("%y%m%d")

def get_time(mydate):
    return mydate.strftime("%H%M")

def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def update_values(values):
    sn = int(values['src_number'])
    sn += 1
    values['src_number'] = get_src_number(sn)
    now = datetime.now()
    values['ship'] = f"TEST SHIP {random_string(size=10)}"
    values['send_date'] = get_date(now)
    values['send_time'] = get_time(now)
    values['msg_ref'] = f"MREF{random_string(size=10)}"
    print(f"Ship: {values['ship']}")