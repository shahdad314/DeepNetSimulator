def parsing_func(file, keyword, pattern):
    import re
    match = False
    with open(file, 'r') as f:
        searchlines = f.readlines()
        for i, line in enumerate(searchlines):
            result = re.match(keyword, line)
            if result == None:
                continue
            elif result.group(0) == keyword:
                match = True
                break
    if match == True:
        sp_line = searchlines[i+1].splitlines()
        #sp_values = sp_line[0].split(pattern)
        sp_values = [float(i) for i in sp_line[0].split(pattern)]
        return sp_values
    else:
        print('Keyword was not found')


def parsing_func2(file, keyword, pattern, inc_str=False):
    import re
    match = False
    with open(file, 'r') as f:
        searchlines = f.readlines()
        for i, line in enumerate(searchlines):
            result = re.match(keyword, line)
            if result == None:
                continue
            elif result.group(0) == keyword:
                match = True
                break

    if match == True:
        sp_line = searchlines[i + 1].splitlines()
        while (searchlines[i + 1].splitlines() != ['/']):
            i += 1
            sp_line += searchlines[i + 1].splitlines()
        sp_values = [sp_line[i].split(pattern) for i in range(len(sp_line) - 1)]
        if inc_str == False:
            value = ([[float(i) for i in value] for value in sp_values])
        elif inc_str == True:
            for value in sp_values:
                for counter, i in enumerate(value):
                    try:
                        value[counter] = float(i)
                    except ValueError:
                        value[counter] = i
                        # value = [[for i in value] for value in sp_values]:

        if len(value[0]) == 1:
            print('yes')
            value = [item[0] for item in value]
        return value
    else:
        print('Keyword was not found')
