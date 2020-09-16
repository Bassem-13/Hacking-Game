# Hacking Version 2
# This is a text-based password guessing game that displays a list of potential
# computer passwords. The player is allowed 1 attempt to guess the password. 
# The game indicates that the player failed to guess the password correctly. 

from uagame import Window
from time import sleep
from random import randint, choice

def main():
    location = [0, 0]
    nb_attempt = 4  
    window = create_window()
    display_header(window, location, nb_attempt)
    password = display_password(window, location)
    guess = prompt_guess(window, location, password, nb_attempt)
    end_game(window, password, guess)
    

def create_window():
    window = Window('Hacking', 600, 500)
    window.set_font_name('couriernew')
    window.set_font_size(18)
    window.set_font_color('green')
    return window

def display_header(window, location, nb_attempt):
    header = ['DEBUG MODE', str(nb_attempt) + ' ATTEMPT(S) LEFT', '']
    for i_header in header:
        display_line(window, i_header, location)

def display_line(window, string, location):
    t = 0.3
    height = window.get_font_height()
    window.draw_string(string, location[0], location[1])
    window.update()
    sleep(t)
    location[1] = location[1] + height
    
def embed_password(window, password, location, champs):

    symbol = '-|[^@]#!§?]}{~'            
    index = randint(0, champs - len(password))
    emb_password = ''
    
    for i_left in range(0, index):
        emb_password = emb_password + choice(symbol)
    emb_password = emb_password + password
    
    for i_right in range(index + len(password), champs):
        emb_password = emb_password + choice(symbol)        
        
    window.draw_string(emb_password, location[0], location[1])
    window.update()
    sleep(0.3)
        
    location[0] = 0
    location[1] = location[1] + window.get_font_height()
            
def display_password(window, location):
    password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'FINDING', 'OVERLAP', 'PUTTING']   
    for i_password in password_list:    
        embed_password(window, i_password, location, 20)
    
    return password_list[7]
  
def prompt_guess(window, location, password, nb_attempt):
    height = window.get_font_height()
    location[1] = location[1] + height
    guess = window.input_string('ENTER PASSWORD >', location[0], location[1])
    
    nb_juste = 0
    coord_hint = [window.get_width() // 2, 0]

    while guess != 'HUNTING' and nb_attempt !=1:
        for i_lettre in range(0, len(password)):
            if guess[i_lettre] == password[i_lettre]:
                nb_juste = nb_juste + 1   
                
        nb_attempt = nb_attempt -1
        if nb_attempt == 1:
            check_warning(window)         
        location[1] = location[1] + height
        window.draw_string(str(nb_attempt) + ' ATTEMPT(S) LEFT', 0, height)
        window.draw_string(guess + ' INCORRECT', coord_hint[0], coord_hint[1])
        window.draw_string(str(nb_juste) + ' /7 IN MATCHING POSITIONS', coord_hint[0], coord_hint[1] + height)
        guess = window.input_string('ENTER PASSWORD >', location[0], location[1])    
    
        coord_hint[1] = coord_hint[1] + 2 * height
        nb_juste = 0
        
    return guess

def check_warning(window):
    height = window.get_font_height()
    lockout_warning = '*** LOCKOUT WARNING ***'
    x_coord_lock = window.get_width() - window.get_string_width(lockout_warning)
    y_coord_lock = window.get_height() - height
    coord_lock = [x_coord_lock, y_coord_lock] 
    display_line(window, lockout_warning, coord_lock)

def end_game(window, password, guess):
    window.clear()
    height = window.get_font_height()
    t = 0.3
    
    if guess == password:
        outcome = [password, '', 'EXISTING DEBUG MODE','','LOGIN SUCCESSFUL - WELCOME BACK','']
        prompt = 'PRESS ENTER TO EXIT'
    else:
        outcome = [password, '', 'LOGIN FAILURE - TERMINAL LOCKED','','PLEASE CONTACT AN ADMINISTRATOR','']
        prompt = 'PRESS ENTER TO EXIT'

    y = (window.get_height() - (len(outcome)+1) * height) // 2
    
    for i_outcome in outcome:
        x = (window.get_width() - window.get_string_width(i_outcome)) // 2
        window.draw_string(i_outcome, x, y)
        window.update()
        sleep(t)
        y = y + height
    
    window.input_string(prompt, (window.get_width() - window.get_string_width(prompt))//2, y)
    window.close()    
    




main()
