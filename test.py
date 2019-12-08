import message


def test_message():
    warning = "Message should be 'Hello World'"
    assert message.get_message() == 'Hello World 2', warning


if __name__ == "__main__":
    test_message()
    print("Everything passed")
