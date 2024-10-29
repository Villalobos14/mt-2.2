class TuringMachine:
    def __init__(self, tape_input, equal_symbol="="):
        self.tape = list(tape_input)
        self.equal_symbol = equal_symbol
        self.head_pos = 0
        self.state = 'q0'
        self.transitions = {
            ('q0', '1'): ('1', 'R', 'q1'),
            ('q1', '0'): ('0', 'R', 'q2'),
            ('q2', '0'): ('0', 'R', 'q2'),
            ('q2', '1'): ('1', 'R', 'q2'),
            ('q2', '='): ('=', 'R', 'q3'),
        }
        self.total = 2

    def move(self):
        current_symbol = self.tape[self.head_pos]
        if (self.state, current_symbol) in self.transitions:
            write_symbol, move_dir, next_state = self.transitions[(self.state, current_symbol)]
            self.tape[self.head_pos] = write_symbol
            self.state = next_state
            self.head_pos += 1 if move_dir == 'R' else -1

            if self.head_pos >= len(self.tape):
                self.tape.append(self.equal_symbol)
            elif self.head_pos < 0:
                self.head_pos = 0

            if self.state == 'q2' and current_symbol in '01':
                self.total += int(current_symbol)
        else:
            self.state = 'REJECTED'

    def run(self):
        while self.state not in {'q3', 'REJECTED'}:
            self.move()
        return self.state == 'q3', self.total
