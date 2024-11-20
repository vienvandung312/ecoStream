from abc import ABC, abstractmethod
import json

class AbstractKafkaService(ABC): 
    def __repr__(self):
        return f'{type(self).__name__}(conf={self.config.get("bootstrap.servers")})'

    def _serialize(self, data: dict) -> bytes:
        if not data:
            raise Exception(f'{data.__repr__()} is not serializable', )
        return json.dumps(data).encode('utf-8')
    
    def _deserialize(self, data: bytes) -> dict:
        if not data:
            raise Exception(f'{data.__repr__()} is not deserializable', )
        try:
            return json.loads(data.decode('utf-8'))
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f'Failed to deserialize message: {e}')
    
    @abstractmethod
    def _delivery_report(self, err, msg):
        raise NotImplementedError

    def add_brokers(self, servers: str) -> None:
        servers = servers.replace(' ', '')
        current_bootstrap_servers = self.config.get('bootstrap.servers')
        
        if current_bootstrap_servers:
            bootstrap_servers = f"{current_bootstrap_servers},{servers}"
        else:
            bootstrap_servers = servers
        
        self.config['bootstrap.servers'] = bootstrap_servers

    @abstractmethod
    def _default_config(self) -> dict:
        raise NotImplementedError