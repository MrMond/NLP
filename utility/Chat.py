class Chat:
    def __init__(self):
        self.converstation_history = []

    def add_message(self, role, content):
        message = {'role': role, 'content': content}

        self.converstation_history.append(message)
