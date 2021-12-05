import logging


class RunningConfig:
    def __init__(self, input_str, stack_symbol, initial_state):
        self.stack = stack_symbol
        self.state = initial_state
        self.remaining_input = input_str

    def printState(self):
        print("")
        print(f"Current state: {self.state}")
        print(f"Remaining input: {self.remaining_input}")
        print(f"Current stack: {self.stack}")
        print("")


class PDA:
    def __init__(self, states, input_symbols, stack_symbols,
                 transitions, initial_state,
                 initial_stack_symbol, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.stack_symbols = stack_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.initial_stack_symbol = initial_stack_symbol
        self.final_states = final_states
        self.validate()

    def validate(self):
        # Make sure PDA is consistent

        # Check whether or not initial state is valid
        if self.initial_state not in self.states:
            logging.error(f"Initial state {self.initial_state} is invalid!")

        # CHeck whether or not final state is valid
        for f in self.final_states:
            if f not in self.states:
                logging.error(f"Final state {f} is invalid!")

        # Check whether or not initial stack symbol is valid
        if self.initial_stack_symbol not in self.stack_symbols:
            logging.error(f"Invalid initial stack symbol")

    def exec(self, input_str):

        current_config = []
        current_config.append(RunningConfig(
            input_str, [self.initial_stack_symbol], self.initial_state))

        # Print initial configuration
        print("\x1b[32mInitial configuration: \x1b[0m")
        current_config[0].printState()

        while current_config != []:

            new_config = []

            for idx, c in enumerate(current_config):

                new = 0

                # If current configuration is accepted
                if self.accepted(c):
                    print("\x1b[35mAccepted!\x1b[0m")
                    return

                print(f"\x1b[32mRunning for configuration {idx + 1}:\n\x1b[0m")

                if c.remaining_input:
                    new = self.update_configs(c)

                # If there are lambda transitions (and no remaining input)
                elif (c.state in self.transitions and
                      '' in self.transitions[c.state] and
                      c.stack[-1] in self.transitions[c.state]['']):
                    new = self.update_configs(c)

                if new:

                    new_config += new

                    # Print all the possible configurations obtained
                    for i, n in enumerate(new):
                        print(f"\x1b[34mOutput configuration {i + 1}:\x1b[0m")
                        n.printState()

            current_config = new_config

        print("\x1b[31mRejected!\x1b[0m")
        return

    def accepted(self, config):

        # If there is still remaining input, return False
        if config.remaining_input:
            return False

        # If stack only has initial symbol and we are in final state, return True
        if config.state in self.final_states and config.stack == [self.initial_stack_symbol]:
            return True

        return False

    def update_configs(self, config):

        transitions = []

        # Get all possible transitions, both for cases when we don't take input and when we do (empty string and non-empty)
        if config.remaining_input:
            transitions += self.get_transitions(config.state,
                                                config.remaining_input[0], config.stack[-1])

        transitions += self.get_transitions(config.state, "", config.stack[-1])

        new_configs = []

        for transition in transitions:

            input_symbol = transition[0]
            new_state = transition[1]
            new_stack_top = transition[2]

            remaining_input = config.remaining_input

            # If input is not lambda
            if input_symbol:
                remaining_input = remaining_input[1:]

            # Add new config based on transition
            new_configs.append(RunningConfig(remaining_input, self.stack_replace_top(
                config.stack.copy(), new_stack_top), new_state))

        return new_configs

    def get_transitions(self, state, symbol, stack_symbol):

        # Get transitions for given state, symbol and stack symbol (All possible transitions)

        out = []

        if state in self.transitions and symbol in self.transitions[state] and stack_symbol in self.transitions[state][symbol]:

            for transition in self.transitions[state][symbol][stack_symbol]:
                out.append([symbol, transition[0], transition[1]])

        return out

    def stack_replace_top(self, stack, stack_top):

        # If element to replace is empty
        if stack_top == "":
            stack.pop()

        # Else replace in reverse order
        else:
            stack.pop()
            for j in range(len(stack_top) - 1, -1, -1):
                stack.append(stack_top[j])

        return stack
