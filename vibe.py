from web3 import Web3
import web3
from web3.middleware import construct_sign_and_send_raw_middleware
import json
import argparse
from util import get_contract

contract_address = '0xc079F5F312EAda9F43e00998738d98C4B6f90C44'
owner_address = "0xf02a3EAbe49fa2E23661c13Bf3Ed4f0aae1f4AaB"
provider_address = 'https://ropsten.infura.io/v3/e0612a9ac52d4e0ea8b800c5b24e48fb'

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


        raw_transaction = contract.functions.reveal().buildTransaction({})
        print(raw_transaction)
        # key = '0x129b418a329ebcc7fa541862fc66a82603ccad2786adf15c904bee5512902128'
        # signed = w3.eth.account.sign_transaction(raw_transaction, key)
        #print(w3.eth.send_raw_transaction(signed.rawTransaction)  )


        # for acct in w3.eth.accounts[1:]:
        #     print(acct)
        # #     amount = int(np.random.randint(100000000, 100000000000))
        # #     print('want to send: ', amount, ' plankton to: ', acct)
        # #     success = str(contract.functions.transfer(acct, amount).transact({"from":w3.eth.accounts[0]}))
        # #     print("success: ", success)

        # #bene = str(np.random.choice(w3.eth.accounts[0]))
        # bene = w3.eth.accounts[0]
        # #mass = 1000000000#int(np.random.randint(1000000000, 1000000000000))
        # print('Minting nft for: ', bene)
        # mint_success = mint_nft_local(bene, contract=contract, contract_address=contract_address)
        # contract.functions.reveal().transact({"from":bene})
        # print('mint success: ', mint_success)
        # uri = contract.functions.tokenURI(1).call()
        # print(uri)


