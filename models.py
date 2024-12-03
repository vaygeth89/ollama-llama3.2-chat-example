import datetime
from pydantic import BaseModel

#define enum for conversation role
from enum import Enum

class RoleType(Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"

class ConversationMessage(BaseModel):
    role: RoleType
    content: str
    created_at: str = datetime.now().isoformat()
    
    def __init__(self, role:RoleType, content:str):
        self.role = role
        self.content = content
    @classmethod
    def for_user(cls, content:str):
        return cls(role=RoleType.USER, content=content)
    @classmethod
    def for_system(cls, content:str):
        return cls(role=RoleType.SYSTEM, content=content)
    @classmethod
    def for_assistant(cls, content:str):
        return cls(role=RoleType.ASSISTANT, content=content)

class ChatQuestion(BaseModel):
    question: str
    # user_id: int
    
# Define the ChatConversation class
class ChatConversation(ConversationMessage):
    def __init__(self, content:str,role:RoleType, thread_id:int, conversation_id:int):
        self.content = content
        self.role = role
        self.conversation_id = conversation_id
    conversation_id: int
    
    #class methods for each role
    @classmethod
    def for_user(cls, content:str, thread_id:int, conversation_id:int):
        return cls(content=content, role=RoleType.USER, thread_id=thread_id, conversation_id=conversation_id)
    
    @classmethod
    def for_system(cls, content:str, thread_id:int, conversation_id:int):
        return cls(content=content, role=RoleType.SYSTEM, thread_id=thread_id, conversation_id=conversation_id)
    
    @classmethod
    def for_assistant(cls, content:str, thread_id:int, conversation_id:int):
        return cls(content=content, role=RoleType.ASSISTANT, thread_id=thread_id, conversation_id=conversation_id)