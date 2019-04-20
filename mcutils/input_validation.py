def input_validation(user_input, return_type, valid_options):
    if(return_type == int):
        if(not user_input.isnumeric()):
            return False
        user_input = int(user_input)

    # /Contains/ validation
    if(not user_input in valid_options):
        return False

    # /Complex/ validation
