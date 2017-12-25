import base
from base import *

import uuid
from populus.utils.accounts import is_account_locked

account = SECOND
# account = "0xcd63Cab084AdC5Ea9A8B5D41ae066F60C6Df2b79"
# account = OWNER
# simple_prettify(locals())
CONTRACT_NAME = 'Crowdsale'
CROWDSALE_ADDRESS = CACHE[FIELDNAME.CROWDSALE_ADDRESS]

print('CONTRACT_NAME = {}'.format(CONTRACT_NAME))
print('crowdlsale add = {}'.format(CROWDSALE_ADDRESS))

value_to_buy = to_wei(0.000000001, 'ETHER')
print('value_to_buy = {}'.format(value_to_buy))

with p.get_chain(CHAIN) as chain:
    web3 = chain.web3
    Crowdsale = get_contract_by_name(chain, CONTRACT_NAME)
    crowdsale = Crowdsale(address=CROWDSALE_ADDRESS)
    #     crowdsale = Crowdsale(address=CROWDSALE_TOKEN_ADDRESS)

    if is_account_locked(web3, account):
        request_account_unlock(chain, account, None)
#     print('get res = {}'.format(crowdsale.call().getRes()))

#     crowdsale = CROWDSALE_ADDRESS

#     print('opcodes = {}'.format(contract.call().opcodes()))
    customer_id = int(uuid.uuid4().hex, 16)  # Customer ids are 128-bit UUID v4

    txid = crowdsale.transact({
        'from': account,
        'sender': account,
        'value': value_to_buy,
    }).buy()

    print('somem form of buy completed')
    # txid = crowdsale.transact({
    #     'from': account,
    #     'sender': account,
    #     'value': value_to_buy,
    #     'customerId': customer_id}).buy()
    #     txid = crowdsale.transact({"from": account, 'customerId': customer_id}).investWithCustomerId(account, customer_id)

    #     print("TXID is", txid)
    check_succesful_tx(web3, txid)
    print("OK")
