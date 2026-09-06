from dataclasses import field
from typing import Any
from enum import Enum
from dataclasses import dataclass

class AgentEventType(str, Enum):
    # Agent lifecycle
    AGENT_START = "agent_start"
    AGENT_END = "agent_end"
    AGENT_ERROR = "agent_error"

    # Text streaming
    TEXT_DELTA = "text_delta"
    TEXT_COMPLETE = "text_complete"
    

@dataclass
class AgentEvent:
    type: AgentEventType
    data: dict[str, Any] = field(default_factory=dict)    