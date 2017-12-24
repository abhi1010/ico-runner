import base
from base import *

import utils
from utils import *


print('about to deploy mintable token')





CROWDSALE_TOKEN = None
CONTRACT = CROWDSALE_TOKEN_ADDRESS = None

chain = CHAIN
address = OWNER
contract_name = 'CrowdsaleToken'
name = 'ChatQ Token'
symbol = 'Q'
supply = 21000000
decimals = 1
mintable = True
minting_agent = OWNER
release_agent = OWNER
verify = False
verify_filename = False
master_address = None


with project.get_chain(chain) as c:

    web3 = c.web3
    provider = web3.providers[0]
    print("Web3 provider is", provider)
    print("Deployer address is", address)
    print("Deployer balance is", from_wei(web3.eth.getBalance(address), "ether"), "ETH")

    try:
        is_account_locked = is_account_locked(web3, address)
        print('is_account_locked = {}'.format(is_account_locked))
        request_account_unlock(c, address, None)
        if is_account_locked:
            print('Trying to unlock {}'.format(address))
            request_account_unlock(c, address, None)
    except:
        pass

    decimal_multiplier = 0

    transaction = {"from": address}
    args = [name, symbol, supply * decimal_multiplier, decimals, mintable]

    # Make sure Populus does not pull up any cached instances of deployed contracts
    # TODO: Fix Populus support this via an deploy argument
    if "JSONFile" in c.registrar.registrar_backends:
        del c.registrar.registrar_backends["JSONFile"]

    print('Starting ', contract_name, ' deployment')
    # This does deployment with all dependencies linked in
    contract, txhash = c.provider.get_or_deploy_contract(contract_name, deploy_transaction=transaction, deploy_args=args)
    print('contract={}, txhash = {}'.format(contract, txhash))
    check_succesful_tx(web3, txhash)
    print("Contract address is", contract.address)
    CROWDSALE_TOKEN = contract
    CONTRACT = CROWDSALE_TOKEN_ADDRESS = contract.address

    # This is needed for Etherscan contract verification
    # https://etherscanio.freshdesk.com/support/solutions/articles/16000053599-contract-verification-constructor-arguments
    const_args = get_constructor_arguments(contract, args)
    print("CrowdsaleToken constructor arguments is", const_args)

    if release_agent:
        print("Setting release agent to", release_agent)
        txid = contract.transact(transaction).setReleaseAgent(release_agent)
        check_succesful_tx(web3, txid)

    if minting_agent:
        print("Setting minting agent")
        txid = contract.transact(transaction).setMintAgent(minting_agent, True)
        check_succesful_tx(web3, txid)

    if master_address:
        print("Moving upgrade master to a team multisig wallet", master_address)
        txid = contract.transact({"from": address}).setUpgradeMaster(master_address)
        check_succesful_tx(web3, txid)
        print("Moving total supply a team multisig wallet", master_address)
        contract.transact({"from": address}).transfer(master_address, contract.call().totalSupply())
        check_succesful_tx(web3, txid)

    if verify:
        chain_name = chain
        fname = verify_filename
        browser_driver = "chrome"
        verify_contract(
            project=project,
            libraries={},  # TODO: Figure out how to pass around
            chain_name=chain_name,
            address=contract.address,
            contract_name=contract_name,
            contract_filename=fname,
            constructor_args=const_args,
            # libraries=runtime_data["contracts"][name]["libraries"],
            browser_driver=browser_driver)
        link = get_etherscan_link(chain_name, contract.address)

        print("Verified contract is", link)

    print("Token supply:", contract.call().totalSupply())

    # Do some contract reads to see everything looks ok
    try:
        print("Token owner:", contract.call().owner())
    except ValueError:
        pass  # No owner

    try:
        print("Token upgradeMaster:", contract.call().upgradeMaster())
    except ValueError:
        pass

    try:
        print("Token minting finished:", contract.call().mintingFinished())
    except ValueError:
        pass

    try:
        print("Token released:", contract.call().released())
        print("Token release agent:", contract.call().releaseAgent())
    except ValueError:
        pass

    print("All done! Enjoy your decentralized future.")
