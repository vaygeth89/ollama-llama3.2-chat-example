from quart import Quart, jsonify, request
from models import ChatQuestion
from assistant import ask_question

app = Quart(__name__)


@app.route("/", methods=['POST'])
async def ask():
    try:
        data = await request.get_json()
        chat_question = ChatQuestion(**data)
    except Exception as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400
    bot_response = await ask_question(chat_question)
    json = bot_response.to_dict()
    # Return the ChatConversation as JSON
    return jsonify(json), 200


if __name__ == '__main__':
    app.run(debug=True, port=3322)
