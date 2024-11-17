from abc import ABC, abstractmethod
import json

class AbstractKafkaService(ABC): 
    def _serialize(self, data: dict) -> bytes:
        if not data:
            raise Exception(f'{data.__repr__()} is not serializable', )
        return json.dumps(data).encode('utf-8')
    
    def _deserialize(self, data: bytes) -> dict:
        if not data:
            raise Exception(f'{data.__repr__()} is not deserializable', )
        return json.loads(data.decode('utf-8'))
    
    @abstractmethod
    def _delivery_report(self, err, msg):
        raise NotImplementedError

    @abstractmethod
    def add_bootstrap_servers(self, servers: str):
        raise NotImplementedError

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError