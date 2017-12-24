
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




FINALIZER_CONTRACT_ADDRESS = None

p  = project

with p.get_chain(CHAIN) as chain:
    web3 = chain.web3

    args = [
        CACHE[FIELDNAME.CONTRACT], CACHE[FIELDNAME.CROWDSALE_ADDRESS]
    ]
    print('args = {}'.format(args))
    finalizser_contract, txhash = chain.provider.get_or_deploy_contract(
        'DefaultFinalizeAgent',
        deploy_transaction={'from': OWNER},
        deploy_args=args)

    print("Deploying finalizser_contract, tx hash is", txhash)
    print("finalizser_contract address is", finalizser_contract.address)

#     prettify(finalizser_contract)

    FINALIZER_CONTRACT = finalizser_contract
    FINALIZER_CONTRACT_ADDRESS = finalizser_contract.address
    CACHE[FIELDNAME.FINALIZER_CONTRACT_ADDRESS] = FINALIZER_CONTRACT_ADDRESS


    save_cache()
