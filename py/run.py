
from settings import get_settings
from normal import normal_mode
from rapidfire import rapidfire_mode
from menu import main_menu

# Main function
if __name__ == '__main__':
    gates = ['X', 'SX', 'Y', 'Z', 'M', 'I', 'H', 'S']
    num_gates, gate_time, init_state = get_settings()
    state = init_state
    gamemode = 'normal'

    while True:
      state = init_state

      print('\n==========================================')
      print('Welcome to the Quantum Gate Game!')
      print()
      
      num_gates, gate_time, init_state, gamemode = main_menu(num_gates, gate_time, init_state)

      # Game loop
      match gamemode:
          case 'normal':
              normal_mode(gates, num_gates, gate_time, state)
          case 'rapidfire':
              rapidfire_mode(gates, num_gates, gate_time, state)
      
      inp = input('\nPlay again? (y/n)')
      if inp != 'y':
          exit()