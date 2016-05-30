class Automaton(object):

    def __init__(self):
        self.states = {}
        self.states['q1'] = {0: 'q1', 1: 'q2'}
        self.states['q2'] = {0: 'q3', 1: 'q2'}
        self.states['q3'] = {0: 'q2', 1: 'q2'}

    def read_commands(self, commands):
        self.commands = [command for command in commands]
        current_state = 'q1'
        for item in self.commands:
            current_state = self.states[current_state][int(item)]
        return True if current_state is 'q2' else False


my_automaton = Automaton()

# Test Cases
print my_automaton.read_commands(["1"]), True
print my_automaton.read_commands(["1", "0", "0", "1"]), True
print my_automaton.read_commands('10010'), False
