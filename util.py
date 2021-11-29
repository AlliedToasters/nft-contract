from web3 import Web3
import web3
import json

def get_contract(path, contract_address, w3, is_truffle=True):
    with open(path, 'r') as f:
        abi = json.loads(f.read())
    if is_truffle: #get abi out of greater truffle blob
        abi = abi['abi']
        print(json.dumps(abi))

    contract = w3.eth.contract(address=contract_address, abi=abi)
    return contract

def extract_abi(input_path, output_path):
    with open(input_path, 'r') as f:
        abi = json.loads(f.read())['abi']
    
    with open(output_path, 'w') as f:
        f.write(json.dumps(abi))

    return True
