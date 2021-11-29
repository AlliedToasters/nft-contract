from web3 import Web3
import web3
from web3.middleware import construct_sign_and_send_raw_middleware
import json
import argparse
from util import get_contract

contract_address = '0x06816c8b63Bb14F7213dad345a0c59B2b766dE46'
owner_address = "0x71267FBddE07E4a66c897ff05BaBCAe141FE9d88"
provider_address = 'http://localhost:8545'

def mint_nft_local(
        to,
        contract=None,
        provider_address="http://localhost:8545", 
        contract_address=contract_address
        ):
    w3 = Web3(Web3.HTTPProvider(provider_address))
    if contract is None:
        contract = get_contract('./client/src/contracts/KelpToken.json', contract_address, w3)
    success = str(contract.functions.mint(2).transact({"from":to}))
    return success

if __name__ in "__main__":
    good = True
    if good:
        w3 = Web3(Web3.HTTPProvider(provider_address))
        contract = get_contract('./client/src/contracts/WGMINFT.json', contract_address, w3)

        for acct in w3.eth.accounts[1:]:
            print(acct)
        #     amount = int(np.random.randint(100000000, 100000000000))
        #     print('want to send: ', amount, ' plankton to: ', acct)
        #     success = str(contract.functions.transfer(acct, amount).transact({"from":w3.eth.accounts[0]}))
        #     print("success: ", success)

        #bene = str(np.random.choice(w3.eth.accounts[0]))
        bene = w3.eth.accounts[0]
        #mass = 1000000000#int(np.random.randint(1000000000, 1000000000000))
        print('Minting nft for: ', bene)
        mint_success = mint_nft_local(bene, contract=contract, contract_address=contract_address)
        contract.functions.reveal().transact({"from":bene})
        print('mint success: ', mint_success)
        uri = contract.functions.tokenURI(1).call()
        print(uri)


