from quart import Quart, jsonify, request
from models import ChatQuestion
from bot import ask_question

app = Quart(__name__)


@app.route("/", methods=['POST'])
async def ask():
    try:
        data = await request.get_json()
        chat_question = ChatQuestion(**data)
    except Exception as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400
    bot_response = await ask_question(chat_question)

    # Return the ChatConversation as JSON
    return jsonify(bot_response), 200


if __name__ == '__main__':
    app.run(debug=True)
