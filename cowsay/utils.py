import subprocess


def run_cowsay(text_string, picture):
    '''
    Run the cowsay shell command and return the output string

    Params:
        - text_string: the string of text that the cow should say

    Return:
        - the output string of the cowsay command
    '''

    cowsay_process = subprocess.run(
        ['cowsay', '-f', picture, text_string], stdout=subprocess.PIPE)
    return cowsay_process.stdout.decode()


def make_entry_dict(db_entry, picture):
    '''
    Prepare a database entry for template rendering by parsing the
    data into a dictionary

    Params:
        - db_entry: a record retrieved from the database

    Returns:
        - a dictionary with the output string resulting
        from running the cowsay subprocess and the date
        the database record was created
    '''

    return {
        'output': run_cowsay(db_entry.cow_text, picture),
        'date': db_entry.created
    }


# choices for the dropdown menu rendered in history.html
dropdown_choices = [
    'Default',
    'Blowfish',
    'Bong',
    'Bud-Frogs',
    'Bunny',
    'Cheese',
    'Cower',
    'Daemon',
    'Dragon',
    'Dragon-and-Cow',
    'Elephant',
    'Elephant-in-Snake',
    'Eyes',
    'Flaming-Sheep',
    'Ghostbusters',
    'Head-In',
    'HelloKitty',
    'Kiss',
    'Kitty',
    'Koala',
    'Kosh',
    'Luke-Koala',
    'Meow',
    'Milk',
    'Moofasa',
    'Moose',
    'Mutilated',
    'Ren',
    'Satanic',
    'Sheep',
    'Skeleton',
    'Small',
    'Sodomized',
    'Stegosaurus',
    'Stimpy',
    'SuperMilker',
    'Surgery',
    'TeleBears',
    'Three-Eyes',
    'Turkey',
    'Turtle',
    'Tux',
    'Udder',
    'Vader-Koala',
    'Vader',
    'WWW',
    'Zen Beavis'
]
