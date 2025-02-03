
if __name__ == '__main__':
    print('Please execute \'run.py\' to start the game.')
    exit()

# Read from settings.ini
def get_settings():
  with open ('settings.ini', 'r') as r_f:
    lines = r_f.readlines()

  for line in lines:
    if 'num_gates' in line:
      num_gates = int(line.split('=')[1])
    if 'gate_time' in line:
      gate_time = int(line.split('=')[1])
    if 'init_state' in line:
      init_state = str(line.split('=')[1].strip())

  return num_gates, gate_time, init_state

# Update settings.ini
def set_settings(num_gates, gate_time, init_state):
  with open ('settings.ini', 'r') as r_f:
    lines = r_f.readlines()

  with open ('settings.ini', 'w') as w_f:
    for line in lines:
      if 'num_gates' in line:
        w_f.write(f'num_gates={num_gates}\n')
      elif 'gate_time' in line:
        w_f.write(f'gate_time={gate_time}\n')
      elif 'init_state' in line:
        w_f.write(f'init_state=\'{init_state}\'\n')
      else:
        w_f.write(line)
