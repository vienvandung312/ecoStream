from abc import ABC, abstractmethod
import json

class AbstractKafkaService(ABC): 
    def _serialize(self, data: dict) -> bytes:
        if not data:
            raise Exception(f'{data.__repr__()} is not serializable', )
        return json.dumps(data).encode('utf-8')
    
    def _deserialize(self, data: bytes) -> dict:
        return json.loads(data.decode('utf-8'))
    
    @abstractmethod
    def _delivery_report(self, err, msg):
        pass

    @abstractmethod
    def add_bootstrap_servers(self, servers: str):
        pass

    @abstractmethod
    def __repr__(self):
        pass