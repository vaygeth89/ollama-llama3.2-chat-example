import datetime
from enum import Enum


class RoleType(Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"

    def __str__(self):
        return self.value

    def to_dict(self):
        return {
            "role": self.value
        }


class ConversationMessage:
    role: RoleType
    content: str
    created_at: str = datetime.datetime.now().isoformat()
    conversation_id: int

    def __init__(self, role: RoleType, content: str, conversation_id: int):
        super().__init__()
        self.role = role
        self.content = content
        self.conversation_id = conversation_id

    def to_dict(self):
        return {
            "role": self.role.value,
            "content": self.content,
            "created_at": self.created_at,
            "conversation_id": self.conversation_id
        }

    @classmethod
    def for_user(cls, content: str, conversation_id: int):
        return cls(role=RoleType.USER, content=content, conversation_id=conversation_id)

    @classmethod
    def for_assistant(cls, content: str, conversation_id: int):
        return cls(role=RoleType.ASSISTANT, content=content, conversation_id=conversation_id)


class ChatQuestion(BaseModel):
    question: str
    # user_id: int
