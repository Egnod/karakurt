import datetime
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path

from {{cookiecutter.repo_name}}.action_set.utils.cbor_b85 import CBORb85


@dataclass
class ActionMetadata:
    device_id: str
    timestamp: float
    targets: list[dict[str, str]] | None = None

    @property
    def datetime(self):
        return datetime.datetime.fromtimestamp(self.timestamp)

    def to_dict(self):
        return {"device_id": self.device_id, "datetime": self.datetime.isoformat(), "timestamp": self.timestamp}


class MetadataManager:
    @staticmethod
    def generate() -> ActionMetadata:
        return ActionMetadata(
            device_id=str(uuid.uuid1(uuid.getnode(), 0))[24:], timestamp=datetime.datetime.now().timestamp()
        )

    @staticmethod
    def serialize(metadata: ActionMetadata):
        return CBORb85.dumps(asdict(metadata))

    @staticmethod
    def deserialize(data: str):
        return ActionMetadata(**CBORb85.loads(data))

    @classmethod
    def read(cls, path: Path):
        result = None

        if path.is_file():
            with open(str(path)) as f:
                result = cls.deserialize(f.read())

        return result

    @classmethod
    def write(cls, path: Path, metadata: ActionMetadata):
        data = cls.serialize(metadata)

        with open(str(path), "w+") as f:
            f.write(data)
