class Command(object):
    def __init__(self):
        super(Command, self).__init__() # Call super to make multiple inheritence work.
        
    def exec(self):
        raise NotImplementedError("Command is not correctly implemented")
    