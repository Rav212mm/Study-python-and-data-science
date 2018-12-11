def string_length(mystring):
    
    print('\nKlasa obiektu typu: ',type(mystring))
    
    if type(mystring) == str:
        return print('\nIlość znaków: ',len(mystring),'\n')
    elif type(mystring) == float:
        return '\nWprowadziles liczbe po przecinku.\nWprowadz string\n'
    else:
        return 'Wprowadz string'
