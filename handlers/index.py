import handlers

class IndexHandler(handlers.Handler):
    def get(self):
        self.write("hello World b2a !!")
