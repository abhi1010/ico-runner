# ITO Creator

## How to run the sample


1. setup virtualenv
2. Install dependencies (_note_: they are hard-coded; ask me why)
3.
## Geth setup

**Initialize a chain**

This will _also_ initialize the chain
```bash
./scripts/setup_chain.sh
```


**Run the chain**
```bash
./chains/horton/run_chain.sh
```





## Geth sample commands


**Run a one-off command**
```bash
geth attach <IPC_FULL_PATH> --exec <COMMAND>
```


### Accounts


**List Accounts**


```bash

web3.eth.accounts

```

**New Account**

```bash
web3.personal.newAccount()
```


**Get Account balance**


```bash
web3.eth.getBalance(web3.eth.accounts[0])
```





**Transfer money**

```
eth.sendTransaction({from: OWNER, to: SECOND, value: web3.toWei(100, "ether")})

# Owner account to a new account
eth.sendTransaction({from: web3.eth.accounts[0], to: web3.eth.accounts[1], value: web3.toWei(100, "ether")})
```

**Unlock account**

```
personal.unlockAccount(address, "password", 0)

personal.unlockAccount(eth.accounts[1],passphrase="demopassword#", 0)
```

