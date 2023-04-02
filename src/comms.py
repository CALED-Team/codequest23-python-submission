import json
import typing


def post_message(message: typing.Dict):
    """
    Converts the given message to a JSON and prints it for the game server.
    :param message: Message to be printed - it should be a dict and should convert to JSON without error.
    """
    print(json.dumps(message))


def read_message() -> typing.Optional[typing.Dict]:
    """
    Reads the next message from the game server.
    :return: a dict containing two keys, time and message. Time key will show how much time the bot has
        to print a response. Message key will have any information the game server has sent about the game.
        If the game has ended, the returned object will be None.
    """
    input_line = json.loads(input())
    if input_line == "END":
        return None
    return input_line
