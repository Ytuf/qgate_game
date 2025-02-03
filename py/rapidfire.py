
if __name__ == '__main__':
    print('Please execute \'run.py\' to start the game.')
    exit()


# Python libs
from random import randint
from time import sleep

# Custom libs
from state_solver import apply_gate

# Rapidfire gamemode
def rapidfire_mode(gates, num_gates, gate_time, state):
  print(f'Rapidfire Mode:')
  print(f'You must apply {num_gates} gates to your qubit initialized at \'{state}\' with {gate_time} seconds per gate.')
  print(f'Get ready!')
  sleep(gate_time)
  for i in range(num_gates):
      # Randomly select a gate
      rand_gate = randint(0, len(gates) - 1)
      print(f'{i+1}.\t{gates[rand_gate]}', end='\t\n')
      
      # Update the state
      state = apply_gate(state, gates[rand_gate])
      
      # Wait to display the next gate
      sleep(gate_time)
  
  # Print the score and mistakes
  print(f'\n\nGame complete! Your final state should be \'{state}\'')
  return
