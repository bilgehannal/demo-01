import message

def test_message():
    assert message.get_message() == 'Hello World', "Message should be 'Hello World'"

if __name__ == "__main__":
    test_message()
    print("Everything passed")