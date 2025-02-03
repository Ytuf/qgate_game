
if __name__ == '__main__':
    print('Please execute \'run.py\' to start the game.')
    exit()


# Python libs
from random import randint
from datetime import datetime
from time import sleep

# Custom libs
from state_solver import apply_gate

# Normal gamemode
def normal_mode(gates, num_gates, gate_time, state):
  score = num_gates
  mistakes = []
  overtime = []
  times = []

  print(f'Normal Mode:')
  print(f'You must apply {num_gates} gates to your qubit initialized at \'{state}\' with {gate_time} seconds per gate.')
  print(f'You must press enter for the next gate to appear, and lose 1 point for each gate that takes more than {gate_time} seconds.')
  print(f'Get ready!')
  sleep(gate_time)

  for i in range(num_gates):
      # Randomly select a gate
      rand_gate = randint(0, len(gates) - 1)
      print(f'{i+1}.\t{gates[rand_gate]}', end='\t')
      
      # Start timer
      start_time = datetime.now()
      input()
      end_time = datetime.now()

      # Update the state
      state = apply_gate(state, gates[rand_gate])

      # Store the response time
      times.append((end_time - start_time).total_seconds())

      # If the response took too long, reduce the score
      if (end_time - start_time).total_seconds() > gate_time:
          score -= 1
          mistakes.append(i+1)
          overtime.append((end_time - start_time).total_seconds() - gate_time)

  # Print the score and mistakes
  print(f'Game complete! Your final state should be \'{state}\'')
  print(f'Your time score is {score}/{num_gates}, {(score/num_gates)*100}%')
  if (len(mistakes) == 1):
      print(f'Took too long on gate {mistakes[0]} by {overtime[0]} seconds')
  elif (len(mistakes) == 2):
      print(f'Took too long on gates {mistakes[0]} by {overtime[0]} seconds and {mistakes[1]} by {overtime[1]} seconds')
  elif (len(mistakes) > 2):
      print(f'Took too long on gates', end=' ')
      for i in range(len(mistakes)):
          if i == len(mistakes) - 1:
              print(f'and {mistakes[i]} by {overtime[i]} seconds')
          else:
              print(f'{mistakes[i]} by {overtime[i]} seconds', end=', ')
  print(f'Average response time: {sum(times)/num_gates} seconds')
  return
