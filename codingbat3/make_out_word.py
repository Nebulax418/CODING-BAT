def make_out_word(out, word):
    
    # important
    if len(out) < 4:
        return 0
    
    return out[:2] + word + out[2:]

print(make_out_word("[[]]", "Yay"))
    
    

