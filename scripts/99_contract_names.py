import base
from base import *

with project.get_chain(CHAIN) as chain:
    names = chain.provider.get_all_contract_names()
    simple_prettify(names)
    
