from os import get_terminal_size

def print_princess():
  (columns, _) = get_terminal_size() # não inicializar as váriaveis antes
  columns -= 1 # pois o usuário pode maximizar o terminal
  
  print('    w*W*W*W*w    '.center(columns))
  print('     \\"."."/     '.center(columns))
  print('      //`\\\\      '.center(columns))
  print('     (/a a\\)     '.center(columns))
  print('     (\\_-_/)     '.center(columns))
  print("    .-~'='~-.    ".center(columns))
  print('   /`~`"Y"`~`\\   '.center(columns))
  print('  / /(_ * _)\\ \\  '.center(columns))
  print(' / /  )   (  \\ \\ '.center(columns))
  print(' \\ \\_/\\\\_//\\_/ / '.center(columns))
  print("  \\/_) '*' (_\\/  ".center(columns))
  print('    |       |    '.center(columns))
  print('    |       |    '.center(columns))
  print('    |       |    '.center(columns))
  print('    |       |    '.center(columns))
  print('    |       |    '.center(columns))
  print('    |       |    '.center(columns))
  print('    |       |    '.center(columns))
  print('    |       |    '.center(columns))
  print('    w*W*W*W*w    '.center(columns))
