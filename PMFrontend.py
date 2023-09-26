import PMBackend
import PySimpleGUI as sg

def main():
    password = {}
    pm = PMBackend.PasswordManager()

    sg.theme('Dark Blue 3')

    layout = [[sg.Text('Key: NONE LOADED')],
              [sg.Text('Password File: NONE LOADED')],
              [sg.Button('Create new key')],
              [sg.Button('Load Key')],
              [sg.Button('Create new password file')],
              [sg.Button('Load password file')],
              [sg.Button('Add password')],
              [sg.Button('Get password')],
              [sg.Button('Exit')]]
    
    window = sg.Window('Password Manager', layout)
    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                break
            case 'Exit':
                break
            case 'Create new key':
                path = sg.popup_get_text('Enter path (with a .key extension): ')
                pm.create_key(path)
                print(path)
            case 'Load Key':
                path = sg.popup_get_file('Select a file')
                pm.load_key(path)
                print(path)
            case 'Create new password file':
                path = sg.popup_get_text('Enter path: ')
                pm.create_password_file(path, password)
                print(path)
            case 'Load password file':
                path = sg.popup_get_file('Select a file')
                pm.load_password_file(path)
            case 'Add password':
                site = sg.popup_get_text('Enter site')
                password = sg.popup_get_text('Enter password')
                pm.add_password(site, password)
            case 'Get password':
                site = sg.popup_get_text('What site do you want the password for?')
                print(f"Password for {site} is {pm.get_password(site)}")

        print(event, values)
    
    window.close()

    

if __name__ == "__main__":
    main()
