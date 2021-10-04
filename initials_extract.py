# Extract every first initials from given strings or list of string.
def initials_extract(phrase):
    # check if given prhase is of type string.
    if type(phrase) is str:
        #print('Extracted from string')
        words = phrase.split()
        result = ""
        for word in words:
            result += ''.join(word[0])
            stand_for = str(phrase)
        
        return result.upper() + ' stand for ' + stand_for +'.'
    
    # check if given phrase is of type list.
    else:
        #print('========== Extracted from list:==========')
        for lst in phrase:
            words = lst.split()
            #print(lst)
            #print(words)
            result = ""
            for word in words:
                result += ' '.join(word[0])
                stand_for = str(words).lstrip('[').rstrip(']').replace("'","").replace(",","").capitalize()
            print(result.upper(),'stand for', stand_for + '.')
            #print()
        
        return 'Done!'

print(initials_extract("Universal Serial Bus")) # Should be: USB
print(initials_extract("local area network")) # Should be: LAN
print(initials_extract("Operating system")) # Should be: OS
print(initials_extract(['Red hat linux','ubuntu linux','debian linux','linux mint',
                        'fedpra linux','SuSe linux','centos linux','slackware linux']))
