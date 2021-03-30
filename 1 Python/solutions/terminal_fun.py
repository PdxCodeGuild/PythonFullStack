


# import time
# def slow_print(text):
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(0.05)
#     print()

# slow_print('Hello welcome to the wonderful fantasy world of Mordor!')


from colorama import Fore, Back, Style

snowman = r'''
                 _...Q._
               .'       '.
              /           \
             ;.-""""--.._ |
            /'-._____..-'\|
          .' ;  o   o    |`;
         /  /|   ()      ;  \
    _.-, '-' ; '.__.-'    \  \
.-"`,  |      \_         / `'`
 '._`.; ._    / `'--.,_=-;_
    \ \|  `\ .\_     /`  \ `._
     \ \    `/  ``---|    \   (~
      \ \.  | o   ,   \    (~ (~  ______________
       \ \`_\ _..-'    \  (\(~   |.------------.|
        \/  ``        / \(~/     || FREE  SNOW ||
         \__    __..-' -   '.    || """"  """" ||
          \ \```             \   || shovel all ||
          ;\ \o               ;  || you  want! ||
          | \ \               |  ||____________||
          ;  \ \              ;  '------..------'
           \  \ \ _.-'\      /          ||
            '. \-'     \   .'           ||
           _.-"  '      \-'           .-||-.
      jgs  \ '  ' '      \           '..---.- '
            \  ' '      _.'
             \' '   _.-'
              \ _.-'
               `
'''
print(Fore.BLUE + snowman + Style.RESET_ALL)




# header = '''
#  _______  ___      _______  _______  _______    _______  __   __  __   __  _______  ___      _______    _______  _______  _______ 
# |       ||   |    |   _   ||       ||       |  |  _    ||  | |  ||  |_|  ||  _    ||   |    |       |  |  _    ||       ||       |
# |       ||   |    |  |_|  ||  _____||  _____|  | |_|   ||  | |  ||       || |_|   ||   |    |    ___|  | |_|   ||    ___||    ___|
# |       ||   |    |       || |_____ | |_____   |       ||  |_|  ||       ||       ||   |    |   |___   |       ||   |___ |   |___ 
# |      _||   |___ |       ||_____  ||_____  |  |  _   | |       ||       ||  _   | |   |___ |    ___|  |  _   | |    ___||    ___|
# |     |_ |       ||   _   | _____| | _____| |  | |_|   ||       || ||_|| || |_|   ||       ||   |___   | |_|   ||   |___ |   |___ 
# |_______||_______||__| |__||_______||_______|  |_______||_______||_|   |_||_______||_______||_______|  |_______||_______||_______|
# '''
# print(header)







# def get_large_letter_width(letter):
#     special_letters = {
#         'i': 1,
#         'j': 2,
#         'q': 4,
#         'v': 4,
#         'x': 4
#     }
#     if letter in special_letters:
#         return special_letters[letter]
#     return 3

# regular_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '

# large_letters = """
# ┌─┐┌┐ ┌─┐┌┬┐┌─┐┌─┐┌─┐┬ ┬┬ ┬┬┌─┬  ┌┬┐┌┐┌┌─┐┌─┐┌─┐ ┬─┐┌─┐┌┬┐┬ ┬┬  ┬┬ ┬─┐ ┬┬ ┬┌─┐╔═╗╔╗ ╔═╗╔╦╗╔═╗╔═╗╔═╗╦ ╦╦ ╦╦╔═╦  ╔╦╗╔╗╔╔═╗╔═╗╔═╗ ╦═╗╔═╗╔╦╗╦ ╦╦  ╦╦ ╦═╗ ╦╦ ╦╔═╗
# ├─┤├┴┐│   ││├┤ ├┤ │ ┬├─┤│ │├┴┐│  │││││││ │├─┘│─┼┐├┬┘└─┐ │ │ │└┐┌┘│││┌┴┬┘└┬┘┌─┘╠═╣╠╩╗║   ║║║╣ ╠╣ ║ ╦╠═╣║ ║╠╩╗║  ║║║║║║║ ║╠═╝║═╬╗╠╦╝╚═╗ ║ ║ ║╚╗╔╝║║║╔╩╦╝╚╦╝╔═╝
# ┴ ┴└─┘└─┘─┴┘└─┘└  └─┘┴ ┴┴└┘┴ ┴┴─┘┴ ┴┘└┘└─┘┴  └─┘└┴└─└─┘ ┴ └─┘ └┘ └┴┘┴ └─ ┴ └─┘╩ ╩╚═╝╚═╝═╩╝╚═╝╚  ╚═╝╩ ╩╩╚╝╩ ╩╩═╝╩ ╩╝╚╝╚═╝╩  ╚═╝╚╩╚═╚═╝ ╩ ╚═╝ ╚╝ ╚╩╝╩ ╚═ ╩ ╚═╝
# """.split('\n')
# large_letters = [t for t in large_letters if t != '']

# def get_large_text(text):
#     output = ['', '', '']
#     for char in text:
#         if char == ' ':
#             output[0] += '   '
#             output[1] += '   '
#             output[2] += '   '
#         index = regular_letters.index(char)
#         large_index = 0
#         for i in range(index):
#             large_index += get_large_letter_width(regular_letters[i].lower())
#         for row in range(len(large_letters)):
#             output[row] += large_letters[row][large_index: large_index + get_large_letter_width(char)]
#     return '\n'.join(output)

# if __name__ == '__main__':
#     text = input('enter some text: ')
#     print(get_large_text(text))
