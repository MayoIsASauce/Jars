import msvcrt
import hashlib

def passField(text:str, opt: int=0)->str:
    """
    Creates a secure password field with astricks, and returns the input sha224 hashed.\n
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n 
    text - The text which prompts for user input.\n
    opt - Either '0' or '1'.\n
        '0' - Makes the text overwritable using \\r.
        '1' - Creates a newline after the prompt
    """
    storage = []
    p = ''
    e = ''
    print(text, end="\r", flush=True)
    while True:

        key = msvcrt.getch()
        if key == b'\r':
            if not storage:
                continue
            else:
                if opt == 1:
                    print(text + e, flush=True)
                break
        elif key == b' ':
            continue
        elif key == b'\x03':
            quit()
        elif key == b'\x08':
            if not storage:
                continue
            else:
                storage.pop()
                e = ''
                print("                                             ", end='\r', flush=True)
                for k in storage:
                    e = e + '*'
                print(text + e, end='\r', flush=True)
                continue
        key = key.decode()
        if key.startswith('\\') == True:
            continue
        storage.append(key)
        e = ''
        print("                                                            ", end='\r', flush=True)
        for d in storage:
            e = e + '*'
        print(text + e, end='\r', flush=True)

    for g in storage:
        p = p + g
    storage.clear()
    hash_object = hashlib.sha224(p.encode())
    p = ''
    hexed = hash_object.hexdigest()
    return hexed
    
# Written by MayoIsASauce on github, uploaded 1/28/20
# Feel free to incorporate this into your projects 

password = passField("password: ", 1)
print(password)