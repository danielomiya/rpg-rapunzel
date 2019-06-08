from os import get_terminal_size

def print_castle():
  (columns, _) = get_terminal_size() # unpack tuple
  columns -= 1

  print('                     .- ._          *                  '.center(columns))
  print('            .       (   ) `) ._,--.                    '.center(columns))
  print('     _.-.          (      .\' | af }      ._    +       '.center(columns))
  print('   .\'     )         `(_\'-\'   |--\'"        ))        |  '.center(columns))
  print('  (   _.   )                 |           \'"       - * -'.center(columns))
  print(' .-.-\'  )  _)  .        ["I"I"I"I"}   .             .  '.center(columns))
  print('(  `   .)`\'              I_I_I_I_I                     '.center(columns))
  print(' `-. (   )          [UUUUI_I_I_I_I                     '.center(columns))
  print('    `-..\'            |[__I_I_[#]_I .        .          '.center(columns))
  print('              +      |__[I_I_I=I_I                     '.center(columns))
  print('    .       ._    +  |]_ I_[#]-I_I    ._          ;    '.center(columns))
  print('            |~       |_[ I_I=I_I_[,   |~               '.center(columns))
  print('          uuuuu      |__ I_I_I%I_I  uuuuu              '.center(columns))
  print('          | #_|      |[ _$_I_I%%_I  | _ |              '.center(columns))
  print('          |-  [      | [ %%I_g%%_I  |  -|         __a:f'.center(columns))
  print('     ---..|_  |.--,,\'|]_ %_Ia%%I_I -|_- |.------""     '.center(columns))
  print('          |_-#|  ((  |_[ $%I%%_!^!  | _ |      +       '.center(columns))
  print('          |   |   )) |[_ |%.%I_|"|  |_  |    n Am   n  '.center(columns))
  print('        .-[_A_]_ \'/  |_ / _Y_)_|`| -[N__]_        n    '.center(columns))
  print('    ._.\'        `- _.--\'`\'  \' "|\\=\\ \'\'    `-.          '.center(columns))
  print('                 .\'             |\\=\\`-._     `         '.center(columns))
  print('              .-\'                  `:.  `---....__     '.center(columns))
  print('                                      `                '.center(columns))
