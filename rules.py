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


def generate_state():
    return ".....0......"

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

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

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
