from web3 import Web3, exceptions
import json

rpc_url = "http://localhost:8545"
wallet_manager = '0xF441DB0464C050FB1570F3747b5C99146ebB9e94'
private_key = '0x0558f2f58ed88f9bdb7bc2aa6839dcd97b46400d71cc86d23ecab989ff1ccf21'

contrat_address = '0x4305D929859d6490A731C3dd881EcF37ed9EC50b'

web3 = Web3(Web3.HTTPProvider(rpc_url))

account = web3.eth.account.from_key(private_key)


if web3.is_connected():
    print("Connecté à la Blockchain")
    print("Version du client :", web3.client_version)
    print("ID de la chaîne :", web3.eth.chain_id)
else:
    print("Impossible de se connecter")
    exit(-1)
    

with open("tuto_metadata.json", "r") as metadata_file:
     contract_metadata = json.load(metadata_file)
     
contract = web3.eth.contract(abi=contract_metadata['abi'], address=contrat_address)
welcome = contract.functions.getWelcome().call()
print(welcome)

added = contract.functions.add(15,8).call()
print(added)