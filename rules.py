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

import random

random.seed(1234)


def generate_state(sym1, sym2):
    string = [sym1]*10
    string_list = list(string)
    string_list[random.randint(0,9)]= sym2     #insert the 0 at a random position using a convertion to a list
    return string_list

def evolve(stato):
    new_stato = ['']*12
    new_stato[0] = '.'
    new_stato[11] = '.'

    for i in range(1,len(stato)-1):
        seq = (stato[i-1], stato[i], stato[i+1])
        terna = ''
        terna = ''.join(seq)
        new_stato[i] = rule30[terna]
    print(''.join(new_stato))
    return ''.join(new_stato)

def simulation(nsteps):
    initial_state = generate_state(".", "0")
    print(initial_state)
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

simulation(10)

########################################################
def test_generation_valid_state():
    """ this tests that the generation function returns valid states when used
    
    GIVEN: the function
    WHEN: I apply it to generate an initial state
    THEN: the resulting state is still a valid one
    """
    state = generate_state()
    assert set(state) == {".","0"}

def test_generation_single_alive():
    """ this tests that the generation function returns only one alive when used
    
    GIVEN: the function
    WHEN: I apply it to generate an initial state
    THEN: the resulting state has only one alive
    """
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1

def is_valid_state(state):
    """this tests that the a general state is valid
    
    GIVEN: a state
    WHEN: I apply it to generate an initial state
    THEN: the resulting state has only one alive
    """
    
    assert len(state)==20 #non so se può essere buona come validità

def test_evolve_valid():
    """ this tests that the evolve function returns valid states when used
    
    GIVEN: a valid state of my simulation
    WHEN: I apply to it the evolve function
    THEN: the resulting state is still a valid one
    """
    state = generate_state() # the validity of this should be tested separetely
    new_state = evolve(state)
    assert is_valid_state(new_state)

    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1

def test_length_evolved_state():
    state = generate_state()
    new_state = evolve(state)
    assert len(state) == len(new_state)

def test_validness_evolved_state():
    state = generate_state()
    new_state = evolve(state)
    assert set(state) == {'.', '0'}

