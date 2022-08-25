def common_end(a, b):
    
    # could use any all for this case but codingbat runs on python 2
    # so this is not an option for any of the python files
    
    
    return True if len(a) >= 1 and len(b) >= 1 and a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1] else False
