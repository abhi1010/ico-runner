### """Deploy crowdsale contract."""

import base
from base import *

print('CACHE[FIELDNAME.CONTRACT] = {}'.format(CACHE[FIELDNAME.CONTRACT]))

CONTRACT_NAME = 'Crowdsale'


def utc_time():
    """UTC UNIX time.

    http://stackoverflow.com/a/22101249/315168
    """
    d = datetime.datetime.utcnow()
    epoch = datetime.datetime(1970, 1, 1)
    t = (d - epoch).total_seconds()
    return t


print('Deploying: {}'.format(CONTRACT_NAME))

chain, address, owner, days = CHAIN, OWNER, OWNER, 1

starts_at = int(utc_time() - 100)
freeze_ends_at = int(utc_time() + days * 24 * 3600)

args = [starts_at, freeze_ends_at, to_wei(10, 'ETHER'), address]

with project.get_chain(chain) as c:

    web3 = c.web3
    print("Web3 provider is", web3.currentProvider)
    print("Deploy address is", address)
    if not address:
        sys.exit(
            "You need to explicitly give the address from where we are deploying from"
        )

    print("Deploy address balance is", from_wei(
        web3.eth.getBalance(address), "ether"))

    # Goes through geth account unlock process if needed
    if is_account_locked(web3, address):
        request_account_unlock(c, address, None)

    print("Deploying contracts with args={}; address={}".format(args, address))
    print('=' * 80)
    print()
    # crowdsale, txhash = c.provider.get_or_deploy_contract(
    crowdsale, txhash = c.provider.get_or_deploy_contract(
        CONTRACT_NAME,
        deploy_transaction={
            "from": address,
            # 'gas': 10000000,
            # 'gasLimit': 1000000000
        },
        deploy_args=args)
    print("Deploying crowdsale, tx hash is: ", txhash)
    print("CrowdSale contract address is (CROWDSALE_ADDRESS): ",
          crowdsale.address)
    CACHE[FIELDNAME.CROWDSALE_ADDRESS] = crowdsale.address

    print("All done! Enjoy your decentralized future.")
    save_cache()
