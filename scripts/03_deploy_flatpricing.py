import base
from base import *

print('CACHE[FIELDNAME.CONTRACT] = {}'.format(CACHE[FIELDNAME.CONTRACT]))


CONTRACT = CACHE[FIELDNAME.CONTRACT]

if not CONTRACT:
    print('there is no valid contract. We are looking for'
    ' CrowdsaleToken. Exiting.')
    set_environment_variable('CONTRACT', CACHE[FIELDNAME.CONTRACT])
    sys.exit(0)
print('CONTRACT = {}'.format(CONTRACT))



deploy_address = OWNER
crowdsale_address = CONTRACT
team_multisig = OWNER


p  = project

with p.get_chain(CHAIN) as chain:
    web3 = chain.web3

    args = [
        to_wei(1, "ether"),
    ]
    print('args = {}'.format(args))
    pricing_strategy, txhash = chain.provider.get_or_deploy_contract(
        'FlatPricing',
        deploy_transaction={'from': deploy_address} ,
        deploy_args=args)

    print("Deploying pricing_strategy, tx hash is", txhash)
    print("Flat Pricing contract address is", pricing_strategy.address)

#     prettify(pricing_strategy)

    # CACHE[FIELDNAME.FLAT_PRICING_CONTRACT] = pricing_strategy
    CACHE[FIELDNAME.FLAT_PRICING_CONTRACT_ADDRESS] = pricing_strategy.address
    save_cache()
