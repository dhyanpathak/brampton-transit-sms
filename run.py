from flask import Flask, request, redirect
import twilio.twiml
from scraper import schedule

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms():
    """Respond with schedule times."""
    body = str(request.values.get('Body', None))
    schedule(body)
    from scraper import message
    text = message
    resp = twilio.twiml.Response()
    resp.message(text)
    message = ""
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
