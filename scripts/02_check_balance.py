import base
from base import *

with project.get_chain(CHAIN) as chain:

    web3 = chain.web3
#     print('project.config = {}\n\n'.format(project.config))
#     print('project.config = {}\n\n'.format(project.config.get('chains.web3http.web3')))

    print('web3= {}'.format(vars(web3)))


    print("Web3 provider is", web3.providers)
    print('acounts = {}'.format(web3.eth.accounts))
    print('total blocks: blocknumber = {}'.format(web3.eth.blockNumber))

    for account in web3.eth.accounts:
        print("Owner {}; balance ={}".format(account, from_wei(web3.eth.getBalance(account), "ether"), "ETH"))

    print('block 3 = {}'.format(web3.eth.getBlock(3)))
    print('transactions at block 3 = {}'.format(web3.eth.getBlock(3)['transactions']))
    print('getBlockTransactionCount 3 = {}'.format(web3.eth.getBlockTransactionCount(3)))
