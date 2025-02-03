
if __name__ == '__main__':
    print('Please execute \'run.py\' to start the game.')
    exit()

from settings import set_settings

def settings_menu(num_gates, gate_time, init_state):
    valid_states = ['0', '1', '+', '-', 'i', '-i']
    in_settings_menu = True

    while in_settings_menu:
        print('\n==========================================')
        print ('\nSettings Menu')
        print('Current settings:')
        print(f'Number of gates: {num_gates} gates')
        print(f'Gate time: {gate_time} seconds')
        print(f'Initial state: {init_state}')
        print()
        print('Please select an option:')
        print()
        print('1. Change number of gates')
        print('2. Change gate time')
        print('3. Change initial state')
        print('4. Save changes for next launch')
        print('5. Back')
        print()
        inp = input('User selection: ')
        match inp:
            case '1':
                num_gates = int(input('Desired number of gates: '))
            case '2':
                gate_time = int(input('Desired gate time in seconds: '))
            case '3':
                print('Please select an initial state from the following options: ')
                print('0, 1, +, -, i, -i')
                init_state = input('Desired initial state: ')
                if (init_state not in valid_states):
                    init_state = '0'
                    print('Invalid state. Defaulting to 0.')
            case '4':
                set_settings(num_gates, gate_time, init_state)
                print('Settings saved.')
            case '5':
                in_settings_menu = False
            case _:
                print('\nInvalid input. Please try again.\n')
    print('\n==========================================')
    return num_gates, gate_time, init_state
                

def main_menu(num_gates, gate_time, init_state):
    in_main_menu = True

    while in_main_menu:
        print('\nMain Menu')
        print('Please select an option:')
        print()
        print('1. Normal Mode : Press enter to get the next gate. You are scored on time.')
        print('2. Rapidfire Mode : Gates are displayed automatically. You must score yourself based on the final state.')
        print('3. Settings')
        print('4. Exit')
        print()
        inp = input("User selection : ")
        match inp:
            case '1':
                gamemode = 'normal'
                in_main_menu = False
            case '2':
                gamemode = 'rapidfire'
                in_main_menu = False
            case '3':
                num_gates, gate_time, init_state = settings_menu(num_gates, gate_time, init_state)
            case '4':
                exit()
            case _:
                print('\nInvalid input. Please try again.\n')
    print('\n==========================================')
    return num_gates, gate_time, init_state, gamemode
