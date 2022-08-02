from brownie import UwUToken, accounts, config

def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    UwUToken_contract = "0xab4233eBC2e21Fe9DcD2Fb13DC574Af8b505c529"
    print(f"Account identifier is: {account}")
    tokenErc20 = UwUToken.deploy(
        UwUToken_contract, 
        {"from":account}
    )

def main(): 
    deploy()