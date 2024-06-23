# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:20:00 2024
@author: Yu
"""
def get_text(text):
    return f"║{text:^80}║"

def get_center_text(text):
    return f"║{text:^120}║"

def get_only_center_text(text):
    return f"{text:^120}"

def get_empty_bar():
    return f"║{' ':^120}║\n"

def print_empty_bar(amount=1):
    #f"{'JUEGO':_^120\n"
    if amount !=1:        
        print(f"║{' ':^120}║\n"* (amount-1))
        print(f"║{' ':^120}║")
    else:
        print(f"║{' ':^120}║")
    #print(bar)

def print_bar(amount=1):
    #bar= 
    print(f"║{'►◄►◄►◄►◄►◄►◄►◄►◄►◄':═^120}║")
    '''
    if amount!=1:
        print(f"║{'►◄►◄►◄►◄►◄►◄►◄►◄►◄':═^120}║\n"*amount)    
    else:
        print(f"║{'►◄►◄►◄►◄►◄►◄►◄►◄►◄':═^120}║")
    '''
def print_bar_char(char,rep):
    char = char * rep
    bar= f"║{char:═^120}║"
    print(bar)

def print_title(title):
    #title_game = f"|{'LA GRANJA DE RUPELTINSKI':=^120}|\n\n"
    print(f"║{title:_^120}║\n")

#GETS--------------------------------------------------------------------
def get_title(title):
    return f"║{title:_^120}║\n"

def get_corners_line():
    return f"╒{'═':═^120}╕\n"