import textwrap


# textwrap.fill(text, width=70, **kwargs)
# Wraps the single paragraph in text, and returns a single string containing the wrapped paragraph. fill() is shorthand for
# "\n".join(wrap(text, ...))


def wrap(string, max_width):
    return textwrap.fill(string,max_width)