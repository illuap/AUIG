from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ActionProfileMetaModel:
    starting_node_name: str
