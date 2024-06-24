import streamlit as st
import json
# from web3 import Web3
from flask import Flask, request, jsonify
import time
from streamlit.web import cli as stcli
import sys

# Load secrets from Streamlit
# infura_project_id = st.secrets["infura_project_id"]
# private_key = st.secrets["private_key"]
# wallet_address = st.secrets["wallet_address"]

# Initialize Flask app within Streamlit
app = Flask(__name__)

# # Connect to Ethereum node
# w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{infura_project_id}'))

# # Load Uniswap Router ABI
# with open('UniswapV2RouterABI.json') as f:
#     router_abi = json.load(f)

# uniswap_router_address = '0x7a250d5630b4cf539739df2c5dacab40b68e3e7a'
# uniswap_router = w3.eth.contract(address=uniswap_router_address, abi=router_abi)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    st.write(data)  # Display data in Streamlit app
    # execute_trade(data)
    return jsonify({'status': 'success'}), 200

# def execute_trade(data):
#     token_to_trade = '0x...TOKEN_ADDRESS...'  # Update with actual token address
#     amount_in_wei = w3.toWei(data['amount'], 'ether')
#     min_amount_out = 1  # Example minimum amount out (slippage control)
#     deadline = int(time.time()) + 60  # Transaction deadline (60 seconds from now)

#     tx = uniswap_router.functions.swapExactETHForTokens(
#         min_amount_out,
#         [w3.toChecksumAddress(w3.eth.default_account), w3.toChecksumAddress(token_to_trade)],
#         wallet_address,
#         deadline
#     ).buildTransaction({
#         'from': wallet_address,
#         'value': amount_in_wei,
#         'gas': 2000000,
#         'gasPrice': w3.toWei('50', 'gwei'),
#         'nonce': w3.eth.getTransactionCount(wallet_address),
#     })

#     signed_tx = w3.eth.account.signTransaction(tx, private_key=private_key)
#     tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
#     st.write(f'Trade executed, transaction hash: {w3.toHex(tx_hash)}')

# Run Flask app with Streamlit
if __name__ == '__main__':
    def run():
        app.run()
    st.write("Webhook server is running")
    st.write("Send your TradingView alerts to /webhook")
    run()
    