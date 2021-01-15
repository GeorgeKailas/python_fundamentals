'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''
def p_tag(func): 
    def wrapped_func(*args): 
        return f"<p>{func(*args)}</p>"
    return wrapped_func


# espn_output = html_tag("""Photo by Robin Alam/Icon Sportswire
# Who’s in the QB market? What every NFL team needs this offseason
# What does each franchise have to have over the next few months?

# 2dNFL Nation

# Why Deshaun Watson is unhappy with Texans, and what comes next""")
# https://realpython.com/primer-on-python-decorators/

espn_output2 = """Photo by Robin Alam/Icon Sportswire
Who’s in the QB market? What every NFL team needs this offseason
What does each franchise have to have over the next few months?

2dNFL Nation

Why Deshaun Watson is unhappy with Texans, and what comes next"""

@p_tag
def all_caps(text):
    return text.upper()

print(all_caps(espn_output2))


    

