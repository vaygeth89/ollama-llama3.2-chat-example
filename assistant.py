from ollama import chat

from file_management.chat_history_file_manager import read_history, write_history
from models import ChatQuestion, ConversationMessage


async def ask_question(question: ChatQuestion) -> ConversationMessage:
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
        return ConversationMessage.for_assistant(
            content=data.message.content,
            conversation_id=len(history) - 1
        )
    except Exception as e:
        print("error: ", e)
