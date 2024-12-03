# Lama 3.2 as an API Using Ollama

### About

This is a simple web application that exposed a POST endpoint using [Flask Framework](https://flask.palletsprojects.com/en/stable/) that accepts a question to converse with.

#### Behaviour Breakdown

* The program receives the user question from the POST endpoint in a form of json

```json
{
  "question": "let's play a game"
}
```

* Appends/Writes the request to [history.json](./files/history.json) file as role "user" with the
  question as "content" like soo

```json
[
  //rest of the system prompts
  {
    "role": "system",
    "content": "You can also provide the user with a random joke, by saying 'Tell me a joke'. When telling a joke, keep it safe and clean, and never tell a joke that is offensive or inappropriate."
  },
  {
    "role": "user",
    "content": "let's play a game"
  }
]
```

* Then passes the whole [history.json](./files/history.json) file content to the model to generate the assistant response with context
* Appends/writes the generated model response in the [history.json](./files/history.json) with the role "assistant" with
  the generated response

```json
[
  //rest of the system prompts
  {
    "role": "system",
    "content": "You can also provide the user with a random joke, by saying 'Tell me a joke'. When telling a joke, keep it safe and clean, and never tell a joke that is offensive or inappropriate."
  },
  {
    "role": "user",
    "content": "let's play a game"
  },
  {
    "role": "assistant",
    "content": "Sure, let's play Guess the number, are you ready?"
  }
]
```

### Setup

* Install [Ollama](https://ollama.com/download)
* Start Ollama
* Run
  ```shell
  # this may take a while to download the model 
  ollama run llama3.2 
  ```
* Install [Python](https://www.python.org/downloads/)
* Install python virtual environment
  ```shell
  # please use the write python version like so
  # python[version] install virtualenv
  # example
  python3.13 install virtualenv
  ```
* Clone this repository
  ```shell
  git clone https://github.com/vaygeth89/ollama-llama3.2-chat-example.git
  ```
* Install Dependencies
    * By running the terminal commands inside the project/repository fold
      ```shell
      virtualenv venv
      source venv/bin/activate
      pip install -r requirements.txt
      ```

### Running the application

* You can just run the main.py with your favourite editor/IDE or using
  ```shell
  python main.py
  ```
* You can make a POST HTTP Request to test it using cURL command, postman or any tools you prefer
    * I included [request.http](request.http) file to run it using REST Client on VSCode or Jetbrains IDEs

### Troubleshooting

* Adjust the ports found in main.py incase the 3322 port is being used by another process
  ```python
  if __name__ == '__main__':
    # from
    app.run(debug=True, port=3322)
    # for example to
    app.run(debug=True, port=1234)
  ```# ollama-llama3.2-chat-example

### Tweaking the model

You can tweak [history.json](./files/history.json) and adjust the system prompts to suits your expected model behaviour
