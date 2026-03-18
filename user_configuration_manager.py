test_settings = { 
    'theme': 'Dark', 
    'notifications': 'enabled', 
}

# add settings
def add_setting(settings, keyval_tuple):

    key, val = keyval_tuple
    key = key.lower()
    val = val.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = val
        return f"Setting '{key}' added with value '{val}' successfully!"


#update setting
def update_setting(settings, keyval_pair):

    key, val = keyval_pair
    key = key.lower()
    val = val.lower()

    if key in settings:
        settings[key] = val
        return f"Setting '{key}' updated to '{val}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


#delete settings
def delete_setting(settings, key):
    
    key = key.lower()
    
    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'


#view settings
def view_settings(settings):

    if not settings:
        return "No settings available."
    else:
        test_settings = "Current User Settings:\n"
        for key, value in settings.items():
            test_settings += f"{key.capitalize()}: {value}\n"
        return test_settings


# tests
print(add_setting({'theme':'light'},('THEME','dark')))
print(update_setting({'theme': 'light'}, ('theme', 'dark')))
print(update_setting({'theme': 'light'}, ('volume', 'high')))
print(delete_setting({'theme': 'light'}, 'theme'))
#final settings
print(view_settings(test_settings))