# WARNING: TESTRPC VERSION SHOULD BE 4.1.3

print('start')
# Which network we deployed our contract
# CHAIN = "mainnet"
# CHAIN = "ropsten"
# CHAIN = "local"
# CHAIN = "testrpc"
CHAIN = "horton"

PROJECT_DIR = '/home/abhishek.pandey/apps/code/githubs/TOKENS/chatq-tokens'

FIRST = OWNER = "0x7a4216b955f00f90cb23efe2796291309f11224b"
SECOND = SECOND_ACCOUNT = RECEIVER = "0x708a15c474a5e704f9a0471cc85f362a2d9fcc8d"
THIRD = "0x0d64d6339fdc88c677adff6b4c287aea4726fa8f"
FOURTH = "0xdc32a05f89ab694f5a699fae304dea896607004e"
FIFTH = "0x4953d3e162961b4b39a920b6eeaddf7c6ddb1d75"
SIXTH = "0xd4dc0e2ccad87593b9da6236111512de5686ab73"
SEVENTH = "0x3e2b3d8b6e5559f40ae0885c35e6726583d47745"
EIGHT = "0x0c8788170aee8073c239edff1feea8e8e4463ccf"
NINTH = "0x72e663d65a5d69beaa39617bbbb0b161e5f2dc86"
TENTH = "0x337c6f220d5e07eb43deae99cb3747f67498adfb"


# FIRST = OWNER = "0xa5a5ae854513273e397aecc4c98776594d63db1a"


# ropsten values
if CHAIN == 'ropsten':
    FIRST = OWNER = "0x7DB7BC71d50a1b9d79F147b98B76947ADa49Fc5D"
    SECOND = SECOND_ACCOUNT = RECEIVER = "0x360f19F4c854e4fA07b0346825bE10389f3987d9"



# rinkeby values
if CHAIN == 'rinkeby':
    FIRST = OWNER = "0xdbC24Baa6906b3d3eA9DA4531DDE8c8cb8c2a57c"
    SECOND = SECOND_ACCOUNT = RECEIVER = "0x0299655ae20065BC2434f1f5Cb9AFEa3f2eDEB43"

# --------------------------------------------------------


# horton values
if CHAIN == 'horton':
    print('Setting horton chain values for accounts')
    FIRST = OWNER = "0xfd88a50961c0257b91f151772846cadfe8be5e08"
    SECOND = '0x81db1193334d2cc625418ca319dd77e4dc068b95'

# FIRST = OWNER = "0x9f04eD4418526e527c577D02Af0CaCAC1128DAf7"

ACCOUNTS = [FIRST, SECOND, THIRD, FOURTH, FIFTH,
           SIXTH, SEVENTH, EIGHT, NINTH, TENTH]




import pprint
pp = pprint.PrettyPrinter(indent=10, depth=3)

def prettify(y):
    a = dir(y)
    reduced = [x for x in a if not x.startswith('__')]
    print('Type = {}'.format(type(y)))
    pp.pprint(reduced)

def simple_prettify(y):
    pp.pprint(y)




import time
import sys
import datetime
from decimal import Decimal


import populus
from populus.utils.accounts import is_account_locked
from populus.utils.cli import request_account_unlock
from populus import Project


from eth_utils import to_wei
from eth_utils import from_wei

import utils

from utils import check_succesful_tx
from utils import get_contract_by_name
from utils import get_constructor_arguments
from utils import get_libraries
from utils import *
# from ico.etherscan import verify_contract


import utils_yaml_cache
from utils_yaml_cache import *



p = project = PROJECT = Project(project_dir="/home/abhishek.pandey/apps/code/githubs/TOKENS/chatq-tokens")




print('end')
