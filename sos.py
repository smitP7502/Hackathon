from twilio.rest import Client
import key


def func():
    client = Client(key.accound_sid, key.auth_token)

    message = client.messages.create(
        body="This is message",
        from_=key.twilio_number,
        to=key.phone_number,
    )


if __name__ == "__main__":
    func()
