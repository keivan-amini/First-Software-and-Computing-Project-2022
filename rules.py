import random

rules = {
    30 : {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         },

    90 : {"...": "0",
          "..0": ".", 
          ".0.": "0", 
          ".00": ".",
          "0..": ".", 
          "0.0": "0", 
          "00.": ".", 
          "000": "0"
          },

    110 : {"...": '0',
           "..0": '.',
           ".0.": '.',
           ".00": '0',
           "0..": '.',
           "0.0": '.', 
           "00.": '.', 
           "000": '0'
           },

    184 : {"...": ".",
           "..0": "0", 
           ".0.": ".", 
           ".00": ".",
           "0..": ".", 
           "0.0": "0", 
           "00.": "0", 
           "000": "0"
           }
}

random.seed(1234)
def generate_state():
    state_list = ['.']*11
    state_list.insert(random.randint(0,10),'0')
    state = ''.join(state_list)
    return state

def evolve(stato, rule_number):
    new_stato = ['']*12
    new_stato[0] = '.'
    new_stato[11] = '.'

    for i in range(1,len(stato)-1):
        seq = (stato[i-1], stato[i], stato[i+1])
        terna = ''
        terna = ''.join(seq)
        new_stato[i] = rules[rule_number][terna]
    print(''.join(new_stato))
    return ''.join(new_stato)

def simulation(nsteps, rule_number):
    initial_state = generate_state()
    print(initial_state)
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state, rule_number)
        states_seq.append(new_state)
    return states_seq


simulation(10, rule_number=30)

########################################################

def is_valid_state(state):
    """this function returns true if the given state is of formed by only . and 0, false otherwise
    
    GIVEN: a state
    WHEN: I apply it to generate an initial state
    THEN: the result is true if it contains only . and 0
    """
    return set(state) == {".","0"}

def is_length_valid(state):
    """this function returns true if the given state is of the correct length, false otherwise
    
    GIVEN: a state
    WHEN: I apply it to generate an initial state
    THEN: the result is true if the length is 12 
    """
    return len(state) == 12 

def test_generation_valid_state():
    """ this tests that the generation function returns valid states when used
    
    GIVEN: the function
    WHEN: I apply it to generate an initial state
    THEN: the resulting state is still a valid one
    """
    state = generate_state()
    assert is_valid_state(state)

def test_generation_single_alive():
    """ this tests that the generation function returns only one alive when used
    
    GIVEN: the function
    WHEN: I apply it to generate an initial state
    THEN: the resulting state has only one alive
    """
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
 
def test_evolve_valid():
    """ this tests that the evolve function returns valid states when used
    
    GIVEN: a valid state of my simulation
    WHEN: I apply to it the evolve function
    THEN: the resulting state is still a valid one
    """
    state = generate_state() # the validity of this should be tested separetely
    new_state = evolve(state, rule_number=30)
    assert is_valid_state(new_state)

def test_length_evolved_state():
    state = generate_state()
    new_state = evolve(state, rule_number=30)
    assert is_length_valid(new_state)