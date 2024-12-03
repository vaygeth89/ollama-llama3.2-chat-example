# Lama 3.2 as an API Using Ollama

This is a simple web application that exposed a POST endpoint using flask that accepts a question to converse with

### Setup

* Install [Ollama](https://ollama.com/download)
* Start Ollama
* Run
  ```shell 
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
  ```