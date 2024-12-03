
from ollama import chat

from file_management.chat_history_file_manager import read_history, write_history
from models import ChatConversation, ChatQuestion

async def ask_question(question: ChatQuestion) -> ChatConversation:
    history = await read_history()

    history.append(
        {
            'role': 'user',
            'content': question.question
        })
    try:
        data = chat(model='llama3.2', messages=history, )
        history.append(
            {
                'role': 'assistant',
                'content': data.message.content
            }
        )
        await write_history(history)
        return ChatConversation.for_assistant(
            content=data.message.content,            
        )
    except Exception as e:
        return e.args