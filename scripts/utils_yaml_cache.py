import base
from base import *
import yaml

from collections import namedtuple, defaultdict

CACHE = defaultdict(lambda: '')

_FILE = 'status.yml'

class _KEYS:
    def __init__(self, *args):
        print('args = {}'.format(args))
        for arg in args[0]:
            setattr(self, arg, arg)
ALL_FIELDS = [
    'CONTRACT',
    'CROWDSALETOKEN',
    'CROWDSALE',
    'FLAT_PRICING_CONTRACT_ADDRESS',
    'CROWDSALE_ADDRESS',
    'FINALIZER_CONTRACT_ADDRESS'
    ]

FIELDNAME = _KEYS(ALL_FIELDS)


def load_cache():
    with open(_FILE, 'rt') as outfile:
        x = yaml.load(outfile)
        for key, value in x.items():
            CACHE[key] = value
        print('Loading Cache: = {}'.format(CACHE))

load_cache()


def save_cache():
    print('CACHE to be saved: {}'.format(dict(CACHE)))
    with open(_FILE, 'w') as yaml_file:
        yaml.dump(dict(CACHE), yaml_file, default_flow_style=False)
