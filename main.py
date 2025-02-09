import hashlib
from datetime import datetime

class SecureDataStorageAgent:
    def __init__(self, network_interface):
        self.network_interface = network_interface  # Interface to interact with the blockchain

    def encrypt_data(self, data):
        """Encrypts data before storing."""
        # Simple encryption for demonstration; use more secure methods in production.
        encrypted_data = hashlib.sha256(data.encode()).hexdigest()
        return encrypted_data

    def store_data_on_chain(self, encrypted_data):
        """Stores encrypted data on the blockchain."""
        # Simulate storing on-chain; replace with actual blockchain interaction.
        transaction_id = self.network_interface.store_transaction(encrypted_data)
        return transaction_id

    def retrieve_and_decrypt(self, transaction_id):
        """Retrieves and decrypts stored data."""
        # Simulate retrieval from chain; replace with actual retrieval logic.
        retrieved_encrypted_data = self.network_interface.get_transaction(transaction_id)
        
        # For demonstration purposes only; decryption would require original key used for encryption.
        decrypted_data = f"Decrypted: {retrieved_encrypted_data}"
        
        return decrypted_data


# Example usage:
if __name__ == "__main__":
    class MockNetworkInterface:
        def store_transaction(self, data):
            print(f"Storing {data}...")
            return "TransactionID123"

    mock_network = MockNetworkInterface()
    
    agent = SecureDataStorageAgent(mock_network)
    
    original_message = "Hello Blockchain!"
    
    encrypted_message = agent.encrypt_data(original_message)
    
    transaction_id = agent.store_data_on_chain(encrypted_message)
    
    print(f"Transaction ID: {transaction_id}")
    
    retrieved_decrypted_message = agent.retrieve_and_decrypt(transaction_id)
    
    print(retrieved_decrypted_message)

