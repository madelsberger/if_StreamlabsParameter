ScriptName = "if"
Website = "https://github.com/madelsberger/if_StreamlabsParameter"
Description = "immediate-if parameter - $if('expr', 'trueMsg', 'falseMsg')"
Creator = "madelsberger"
Version = "1.0.0"

def Init():
    pass

def Parse(parseString, user, target, message):
    old = parseString
    new = ""
    while '$if' in old:
        i = old.index('$if')
        new += old[:i]
        old = old[i+3:]
        arg = eatSpaces(old)
        if arg[0] != '(':  # this instance is no good, but keep looking
            new += '$if'
            continue
        arg = eatSpaces(arg[1:])
        if arg[0] != '\'':  # this instance is no good, but keep looking
            new += '$if'
            continue
        i = findClosingTick(arg)
        if i == -1:        # there can be no valid instances; abort the search
            return parseSting
        if i == 1:
            expr = "False"
        else:
            expr = arg[1:i].replace("\\'", "'")
        arg = eatSpaces(arg[i+1:])
        if arg[0] != ',':  # this instance is no good, but keep looking
            new += '$if'
            continue
        arg = eatSpaces(arg[1:])
        if arg[0] != '\'':  # this instance is no good, but keep looking
            new += '$if'
            continue
        i = findClosingTick(arg)
        if i == -1:        # there can be no valid instances; abort the search
            return parseSting
        trueMsg = arg[1:i].replace("\\'", "'");
        arg = eatSpaces(arg[i+1:])
        if arg[0] != ',':  # this instance is no good, but keep looking
            new += '$if'
            continue
        arg = eatSpaces(arg[1:])
        if arg[0] != '\'':  # this instance is no good, but keep looking
            new += '$if'
            continue
        i = findClosingTick(arg)
        if i == -1:        # there can be no valid instances; abort the search
            return parseSting
        falseMsg = arg[1:i].replace("\\'", "'");
        arg = eatSpaces(arg[i+1:])
        if arg[0] != ')':  # this instance is no good, but keep looking
            new += '$if'
            continue
        try:
            if eval(expr):
                new += trueMsg
            else:
                new += falseMsg
            old = arg[1:]
        except:
            new += '$if'
            continue
    else:
        new += old
    return new

def eatSpaces(s):
    i = 0
    while(s[i] in " \t"):
        i += 1
    return s[i:]

def findClosingTick(s):
    esc = False
    for i in range(1,len(s)):
        if esc:
            esc = False
        else:
            if s[i] == '\'':
                break
            if s[i] == '\\':
                esc = True
    else:
        i = -1
    return i
