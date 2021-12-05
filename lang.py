from pda import PDA


class Languages:
    languages = {
        "aNbN":
        # L = {aNbN : N >= 0}
        PDA(
            states=['q0', 'q1'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q1', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ]
                    },
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                },
                'q1': {
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q1']
        ),

        "aNb2N":
        # L = {aNb2N : N >= 0}
        PDA(
            states=['q0', 'q1', 'q2'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A', 'A']]
                        ]
                    },
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                },
                'q1': {
                    'b': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q2']
        ),

        "aMbNcM+N":
        # L = {aMbNc(M+N) : M,N >= 0}
        PDA(
            states=['q0', 'q1', 'q2', 'q3'],
            input_symbols=['a', 'b', 'c'],
            stack_symbols=['A', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q3', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ]
                    },
                    'b': {
                        'Z': [
                            ['q1', ['A', 'Z']]
                        ],
                        'A': [
                            ['q1', ['A', 'A']]
                        ]
                    },
                    'c': {
                        'A': [
                            ['q2', '']
                        ],
                    },
                },
                'q1': {
                    'b': {
                        'A': [
                            ['q1', ['A', 'A']]
                        ]
                    },
                    'c': {
                        'A': [
                            ['q2', '']
                        ]
                    },
                },
                'q2': {
                    '': {
                        'Z': [
                            ['q3', 'Z']
                        ]
                    },
                    'c': {
                        'A': [
                            ['q2', '']
                        ]
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q2']
        ),

        "aNbMcMdN":
        # L = {aNbMcMdN : M,N >= 0}
        PDA(
            states=['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'],
            input_symbols=['a', 'b', 'c', 'd'],
            stack_symbols=['A', 'B', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q4', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ],
                    },
                    'b': {
                        'Z': [
                            ['q5', ['B', 'Z']]
                        ],
                        'A': [
                            ['q1', ['B', 'A']]
                        ],
                    },
                    'd': {
                        'A': [
                            ['q3', '']
                        ],
                    },
                },
                'q1': {
                    'b': {
                        'B': [
                            ['q1', ['B', 'B']]
                        ],
                    },
                    'c': {
                        'B': [
                            ['q2', '']
                        ],
                    },
                },
                'q2': {
                    'c': {
                        'B': [
                            ['q2', '']
                        ],
                    },
                    'd': {
                        'A': [
                            ['q3', '']
                        ]
                    },
                },
                'q3': {
                    '': {
                        'Z': [
                            ['q4', 'Z']
                        ],
                    },
                    'd': {
                        'A': [
                            ['q3', '']
                        ]
                    },
                },
                'q5': {
                    'b': {
                        'B': [
                            ['q5', ['B', 'B']]
                        ],
                    },
                    'c': {
                        'B': [
                            ['q6', '']
                        ]
                    },
                },
                'q6': {
                    '': {
                        'Z': [
                            ['q4', 'Z']
                        ],
                    },
                    'c': {
                        'B': [
                            ['q6', '']
                        ]
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q4']
        ),

        "wcwR":
        # L = {wcwR : w ∈ (a+b)*}
        PDA(
            states=['q0', 'q1', 'q2', 'q3'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'B', 'Z'],
            transitions={
                'q0': {
                    'c': {
                        'Z': [
                            ['q3', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']]
                        ],
                        'B': [
                            ['q0', ['A', 'B']]
                        ],
                    },
                    'b': {
                        'Z': [
                            ['q0', ['B', 'Z']]
                        ],
                        'A': [
                            ['q0', ['B', 'A']]
                        ],
                        'B': [
                            ['q0', ['B', 'B']]
                        ],
                    },
                    'c': {
                        'A': [
                            ['q1', 'A']
                        ],
                        'B': [
                            ['q1', 'B']
                        ],
                    },
                },
                'q1': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                    'a': {
                        'A': [
                            ['q1', '']
                        ],
                    },
                    'b': {
                        'B': [
                            ['q1', '']
                        ],
                    },
                },
                'q3': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q2']
        ),

        "wwR":
        # L = {wwR : w ∈ (a+b)*}
        PDA(
            states=['q0', 'q1', 'q2'],
            input_symbols=['a', 'b'],
            stack_symbols=['A', 'B', 'Z'],
            transitions={
                'q0': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ],
                    },
                    'a': {
                        'Z': [
                            ['q0', ['A', 'Z']]
                        ],
                        'A': [
                            ['q0', ['A', 'A']],
                            ['q1', ''],
                        ],
                        'B': [
                            ['q0', ['A', 'B']]
                        ],
                    },
                    'b': {
                        'Z': [
                            ['q0', ['B', 'Z']]
                        ],
                        'A': [
                            ['q0', ['B', 'A']]
                        ],
                        'B': [
                            ['q0', ['B', 'B']],
                            ['q1', ''],
                        ],
                    },
                },
                'q1': {
                    '': {
                        'Z': [
                            ['q2', 'Z']
                        ]
                    },
                    'a': {
                        'A': [
                            ['q1', '']
                        ]
                    },
                    'b': {
                        'B': [
                            ['q1', '']
                        ]
                    },
                },
            },
            initial_state='q0',
            initial_stack_symbol='Z',
            final_states=['q2']
        )
    }

    def get_lang(self, s):
        return self.languages[s]
