# Standard Lib Imports
from pathlib import Path
FILE_DIR = Path(__file__).parent

# Third Party Imports
import docker # pip install docker
from docker.types import LogConfig

class DockerFactory:
    def __init__(self, swarm: bool = False) -> None:
        self.client = docker.from_env()
        self.logconfig = LogConfig(type=LogConfig.types.JSON)
        
        self.prune() # Kill all unused entities
        
        self.containers: list = self.client.containers.list()
        self.images: list = self.client.images.list()
        self.networks: list = self.client.networks.list()
        self.volumes: list = self.client.volumes.list()
                
        if swarm:
            self._swarm_init()
    
    def prune(self) -> None:
        self.client.swarm.leave(force=True)
        self.client.images.prune()
        self.client.containers.prune()
        self.client.networks.prune()
        self.client.volumes.prune()
    
    def _swarm_init(self) -> None:
        try:
            self.client.swarm.init()
        except:
            raise Exception("Swarm already initialized")
        
        self.nodes: list = self.client.nodes.list()
        self.secrets: list = self.client.secrets.list()
        self.services: list = self.client.services.list()
        
    def build_container(self, img: str=None, tag: str='clips', img_path: str=None) -> None:
        """Hard coding for CLIPs container for now"""
        img = self.client.images.build(path=str(FILE_DIR), tag=tag, rm=True)[0]
        container_config = {
            'name': 'clips',
            'image': img.id,
            'log_config': self.logconfig,
            'auto_remove': False,
            'detach': True,
            'stdin_open': True,
            'tty': True,
            'privileged': True,
        }
        c = self.client.containers.run(**container_config)
        self.containers.append(c)
        return c