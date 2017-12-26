import base
from base import *

with project.get_chain(CHAIN) as chain:

    web3 = chain.web3
    logging.info('web3= {}'.format(vars(web3)))

    logging.info("Web3 provider is {}".format(web3.providers))
    logging.info('acounts = {}'.format(web3.eth.accounts))
    logging.info('total blocks: blocknumber = {}'.format(web3.eth.blockNumber))

    for account in web3.eth.accounts:
        logging.info("Owner {}; balance ={}".format(
            account, from_wei(web3.eth.getBalance(account), "ether"), "ETH"))
