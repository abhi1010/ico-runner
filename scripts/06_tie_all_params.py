
import base
from base import *


p  = project

with p.get_chain(CHAIN) as chain:
    web3 = chain.web3


    Crowdsale = get_contract_by_name(chain, 'UncappedCrowdsale')
    crowdsale = Crowdsale(address=CACHE[FIELDNAME.CROWDSALE_ADDRESS])

    print('Attempting to set finalize agent for crowdsale')
    crowdsale.transact({'from': OWNER}).setFinalizeAgent(CACHE[FIELDNAME.FINALIZER_CONTRACT_ADDRESS])
    print('Done')


    CrowdsaleToken = get_contract_by_name(chain, 'CrowdsaleToken')
    crowdsaletoken = CrowdsaleToken(address=CACHE[FIELDNAME.CONTRACT])
    print('Attempting to set finalize agent for crowdsale token')
    crowdsaletoken.transact({'from': OWNER}).setReleaseAgent(CACHE[FIELDNAME.FINALIZER_CONTRACT_ADDRESS])
    print('Done')
