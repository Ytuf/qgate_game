
if __name__ == '__main__':
    print('Please execute \'run.py\' to start the game.')
    exit()


# Helper function to apply a gate to a state
def apply_gate(state, gate):
    match gate:
        case 'X':
            match state:
                case '0':
                    state = '1'
                case '1':
                    state = '0'
                case '+':
                    state = state
                case '-':
                    state = state
                case 'i':
                    state = '-i'
                case '-i':
                    state = 'i'
                case _:
                    exit(f'\nInvalid state \'{state}\' received.')
        case 'SX':
            match state:
                case '0':
                    state = '-i'
                case '1':
                    state = 'i'
                case '+':
                    state = state
                case '-':
                    state = state
                case 'i':
                    state = '0'
                case '-i':
                    state = '1'
                case _:
                    exit(f'\nInvalid state {state} received.')
        case 'Y':
            match state:
                case '0':
                    state = '1'
                case '1':
                    state = '0'
                case '+':
                    state = '-'
                case '-':
                    state = '+'
                case 'i':
                    state = state
                case '-i':
                    state = state
                case _:
                    exit(f'\nInvalid state {state} received.')
        case 'Z':
            match state:
                case '0':
                    state = state
                case '1':
                    state = state
                case '+':
                    state = '-'
                case '-':
                    state = '+'
                case 'i':
                    state = '-i'
                case '-i':
                    state = 'i'
                case _:
                    exit(f'\nInvalid state {state} received.')
        case 'M': # For predictable results, uncertain measurement always results in 0
            match state:
                case '0':
                    state = state
                case '1':
                    state = state
                case '+':
                    state = '0'
                case '-':
                    state = '0'
                case 'i':
                    state = '0'
                case '-i':
                    state = '0'
                case _:
                    exit(f'\nInvalid state {state} received.')
        case 'I':
            state = state
        case 'H':
            match state:
                case '0':
                    state = '+'
                case '1':
                    state = '-'
                case '+':
                    state = '0'
                case '-':
                    state = '1'
                case 'i':
                    state = '-i'
                case '-i':
                    state = 'i'
                case _:
                    exit(f'\nInvalid state {state} received.')
        case 'S':
            match state:
                case '0':
                    state = state
                case '1':
                    state = state
                case '+':
                    state = 'i'
                case '-':
                    state = '-i'
                case 'i':
                    state = '-'
                case '-i':
                    state = '+'
                case _:
                    exit(f'\nInvalid state {state} received.')
        case _:
            exit(f'\nInvalid gate {gate} received.')
    return state
