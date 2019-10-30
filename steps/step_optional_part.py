from behave import register_type
import parse


@parse.with_pattern(r"simple\s+")
def parse_word_simple(text):
    """Type converter for "simple " (followed by one/more spaces)."""
    return text.strip()


register_type(simple_=parse_word_simple)
