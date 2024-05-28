import readline

history = []

def add_command(command):
    history.append(command)
    readline.add_history(command)  # Also add to REPL history



