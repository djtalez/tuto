from web3 import Web3, exceptions
import json

rpc_url = "http://localhost:8545"
wallet_manager = '0xF441DB0464C050FB1570F3747b5C99146ebB9e94'
private_key = '0x0558f2f58ed88f9bdb7bc2aa6839dcd97b46400d71cc86d23ecab989ff1ccf21'


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
     
contrat = web3.eth.contract(abi=contract_metadata['abi'], bytecode=contract_metadata['bytecode']['object'])

transaction = contrat.constructor().build_transaction({
    'from':wallet_manager,
    'value':0,
    'gasPrice': web3.eth.gas_price,
    'nonce': web3.eth.get_transaction_count(wallet_manager)
})
gas_estimated = web3.eth.estimate_gas(transaction)
print(f"Gas estimated: {gas_estimated} x {web3.eth.gas_price}")

transaction = contrat.constructor().build_transaction({
    'from':wallet_manager,
    'value':0,
    'gas':gas_estimated,
    'gasPrice': web3.eth.gas_price,
    'nonce': web3.eth.get_transaction_count(wallet_manager)
})

signed = account.sign_transaction(transaction)

tx_hash= web3.eth.send_raw_transaction(signed.rawTransaction)
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
tx=web3.eth.get_transaction(tx_hash)
if receipt['status'] == 1 :
    print(receipt)
    print(f"Contrat correctement deployer a l'adresse:  {receipt.contractAddress}")
else:
    try:
        web3.eth.call(tx, tx['blockNumber'])
    except exceptions.ContractLogicError as error:
        print(error)
        
