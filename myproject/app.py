from flask import Flask, request, abort

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, Flask!'

# if __name__ == '__main__':
#     app.run()

api_endpoint = "https://live-server-10651.wati.io"
access_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyNjU4ZDM3Yi1kZDg0LTRkZDMtYWNjMC1hZjdjNjVlZGU5MTEiLCJ1bmlxdWVfbmFtZSI6Im1hcmtldGluZ0BtbTkuY29tLmhrIiwibmFtZWlkIjoibWFya2V0aW5nQG1tOS5jb20uaGsiLCJlbWFpbCI6Im1hcmtldGluZ0BtbTkuY29tLmhrIiwiYXV0aF90aW1lIjoiMTAvMTEvMjAyMyAwMzoxNjo1MCIsImRiX25hbWUiOiIxMDY1MSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlBBUlRORVJfQURNSU5JU1RSQVRPUiIsImV4cCI6MjUzNDAyMzAwODAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.2r3sykzvLygs73coC30EWFIfWCNQOUBzFqFd4-6E7cc"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
      
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)Message
    return 'OK'
        
@handler.add(MessageEvent, message=Text)
def handle_message(event_):
    line_bot_api.reply_message(
         event.reply_token,
         TextSendMessage(text=event.message.text))


if __name__ == "__main__":
        app.run()