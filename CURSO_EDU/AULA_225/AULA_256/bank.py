from conta import Account
from pessoa import Client

class Bank:
    
    agencias = [123, 456, 789]
    
    def __init__(self, name) -> None:
        self._accounts = []
        self._clients = []
        self._name = name
        
    def add_account(self, account):
        self._accounts.append(account)
        
    def add_client(self, client):
        self._clients.append(client)
        
    @property
    def accounts(self):
        return(self._accounts)