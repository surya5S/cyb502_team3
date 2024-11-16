from web3 import Web3
import hashlib

# Connect to Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if web3.is_connected():
    print("Connected to Blockchain")
else:
    print("Connection failed")

# Convert the contract address to a checksum address
contract_address = "0x20c50214ca1689e6496b488c643ae671b82fc2a6"
checksum_contract_address = Web3.to_checksum_address(contract_address)

# Contract ABI
contract_abi = [
    {
        "inputs": [{"internalType": "bytes32", "name": "_hash", "type": "bytes32"}],
        "name": "addDocumentHash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "_hash", "type": "bytes32"}],
        "name": "verifyDocumentHash",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function"
    }
]

# Initialize the contract using the checksum address
contract = web3.eth.contract(address=checksum_contract_address, abi=contract_abi)

# Account for transaction (Ganache default account)
account = web3.eth.accounts[0]

# Generate the document hash (for example using SHA-256)
document_path = '/Users/ASUS1/Downloads/cybproject/doc.txt'

def generate_document_hash(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        return hashlib.sha256(file_data).hexdigest()

# Generate document hash
document_hash = generate_document_hash(document_path)

# Convert the document hash to bytes32
document_hash_bytes = Web3.to_bytes(hexstr=document_hash)
if len(document_hash_bytes) != 32:
    raise ValueError("Hash must be 32 bytes long (SHA-256 hash is required)")

# Send transaction to add document hash
#tx_hash = contract.functions.addDocumentHash(document_hash_bytes).transact({'from': account})
#web3.eth.wait_for_transaction_receipt(tx_hash)

#print("Document hash added successfully.")

# Verify document hash
is_verified = contract.functions.verifyDocumentHash(document_hash_bytes).call()
if is_verified:
    print("Document is verified.")
else:
    print("Document not found.")
