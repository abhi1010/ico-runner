##### from ico.state import CrowdsaleState
import base
from base import *


# p = Project
# print('Crowdsale name = {}; Address={}'.format(CONTRACT_NAME, CROWDSALE_ADDRESS))


with p.get_chain(CHAIN) as chain:
    web3 = chain.web3
    Crowdsale = get_contract_by_name(chain, 'UncappedCrowdsale')
    crowdsale = Crowdsale(address=CACHE[FIELDNAME.CROWDSALE_ADDRESS])

#     ab, hx = crowdsale.transact({'from': OWNER}).getState()
    ab = crowdsale.transact({'from': OWNER}).getState()
    ab = crowdsale.transact({'from': OWNER}).weiRaised()
    print(' State = ', crowdsale.call().getState())
    print(' weiRaised = ', crowdsale.call().weiRaised())
    print(' tokensSold = ', crowdsale.call().tokensSold())
    print(' isFinalizerSane = ', crowdsale.call().isFinalizerSane())
    print(' isPricingSane = ', crowdsale.call().isPricingSane())
    print(' investorCount = ', crowdsale.call().investorCount())
    print(' requireCustomerId = ', crowdsale.call().requireCustomerId())
    print(' requiredSignedAddress = ', crowdsale.call().requiredSignedAddress())
