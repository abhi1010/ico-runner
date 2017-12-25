



### """Deploy crowdsale contract."""

import base
from base import *

print('CACHE[FIELDNAME.CONTRACT] = {}'.format(CACHE[FIELDNAME.CONTRACT]))

CONTRACT_NAME = 'SaleAbhi'



def utc_time():
    """UTC UNIX time.

    http://stackoverflow.com/a/22101249/315168
    """
    d = datetime.datetime.utcnow()
    epoch = datetime.datetime(1970, 1, 1)
    t = (d - epoch).total_seconds()
    return t

print('')


chain, address, owner, days, minimum, verify = CHAIN, OWNER, OWNER, 1, 0.001, False

# Parse command line args to crowdsale constructor args
minimum = to_wei(0.001, "ether")
starts_at = int(utc_time())
freeze_ends_at = int(utc_time() + days * 24*3600)


# args = [starts_at, freeze_ends_at,
#         1, 10000, 100000, OWNER]
args = [OWNER]

# CONTRACT_NAME = "Crowdsale"

# CONTRACT_NAME = "UncappedAbhi"

# This is configured in populus.json
# We are working on a testnet
print("Make sure {} chain is running, you can connect to it, or you'll get timeout".format(chain))

CROWDSALE = None
CROWDSALE_ADDRESS = None

with project.get_chain(chain) as c:

    web3 = c.web3
    print("Web3 provider is", web3.currentProvider)
    print("Deploy address is", address)
    if not address:
        sys.exit("You need to explicitly give the address from where we are deploying from")

    print("Deploy address balance is", from_wei(web3.eth.getBalance(address), "ether"))

    # Goes through geth account unlock process if needed
    if is_account_locked(web3, address):
        request_account_unlock(c, address, None)


    # This does deployment with all dependencies linked in
    print("Deploying contracts with args={}".format(args))
    print('='*80)
    print()
    crowdsale, txhash = c.provider.deploy_contract(
        CONTRACT_NAME,
        deploy_transaction={"from": address},
        deploy_args=args)
#     print("Deploying crowdsale, tx hash is: ", txhash)
    print("CrowdSale contract address is (CROWDSALE_ADDRESS): ", crowdsale.address)
    CROWDSALE = crowdsale
    CROWDSALE_ADDRESS = crowdsale.address
    CACHE[FIELDNAME.CROWDSALE_ADDRESS] = CROWDSALE_ADDRESS



    print("All done! Enjoy your decentralized future.")
    save_cache()
