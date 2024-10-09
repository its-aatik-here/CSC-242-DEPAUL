def removePunc(astr):
    'remove some punctuation from astr'
    assert type(astr) == str, 'parameter is not a string'
    for ch in '!,:;.':
        astr = astr.replace(ch, ' ')
    return astr

assert removePunc('testing,testing!!') == 'testing testing  '
assert removePunc('?!.') == '', 'question mark example failed'
