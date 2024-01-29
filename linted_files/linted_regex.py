import re


def find_iter_matches(string):
    """
    Find all occurrences of numbers in a string and print them with their index positions.
    """
    for m in re.finditer(r"\\d+", string):
        print(m.group(0))
        print("Index position:", m.start())

# New File


def remove_special_characters(string):
    """
    Remove special characters from a string.
    """
    pattern = re.compile(r'[\\W_]+')
    return pattern.sub('', string)


# Example usage of the function
print(remove_special_characters("**//Python Exercises// - 12. "))

# New File


def extract_urls(text):
    """
    Extract URLs from a given text.
    """
    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    print("Original string: ", text)
    print("Urls: ", urls)


# Example usage of the function
extract_urls('<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>')

# New File


def split_camel_case(text):
    """
    Split a camel case string into individual words.
    """
    return re.findall('[A-Z][^A-Z]*', text)


# Example usage of the function
print(split_camel_case("ThisIsARandomString"))

# New File


def custom_split(text):
    """
    Custom split function to split a text on multiple delimiters.
    """
    return re.split('; |, |\\*|\\n', text)


# Example usage of the function
print(custom_split('The quick brown\\nfox jumps*over the lazy dog.'))

# New File


def match_a_star(text):
    """
    Find matches where 'a' is followed by zero or more 'b's.
    """
    match = re.search("a*", "aaaaab")
    if match:
        print("I've got:", match.group())


def character_match(text):
    """
    Check if a string matches the pattern '^a(b*)$'.
    """
    matching = r"^a(b*)$"
    if re.search(matching, text):
        return "We've got something here"
    else:
        return "No such luck"

# New File


def find_iter_matches(string):
    """
    Find all occurrences of numbers in a string and print them with their index positions.
    """
    for m in re.finditer(r"\d+", string):
        print(m.group(0))
        print("Index position:", m.start())

# New File


def remove_special_characters(string):
    """
    Remove special characters from a string.
    """
    pattern = re.compile(r'[\W_]+')
    return pattern.sub('', string)


# Example usage of the function
print(remove_special_characters("**//Python Exercises// - 12. "))

# New File


def extract_urls(text):
    """
    Extract URLs from a given text.
    """
    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    print("Original string: ", text)
    print("Urls: ", urls)


# Example usage of the function
extract_urls('<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>')

# New File


def split_camel_case(text):
    """
    Split a camel case string into individual words.
    """
    return re.findall('[A-Z][^A-Z]*', text)


# Example usage of the function
print(split_camel_case("ThisIsARandomString"))

# New File


def custom_split(text):
    """
    Custom split function to split a text on multiple delimiters.
    """
    return re.split('; |, |\\*|\\n', text)


# Example usage of the function
print(custom_split('The quick brown\\nfox jumps*over the lazy dog.'))

# New File


def match_a_star(text):
    """
    Find matches where 'a' is followed by zero or more 'b's.
    """
    match = re.search("a*", "aaaaab")
    if match:
        print("I've got:", match.group())


def character_match(text):
    """
    Check if a string matches the pattern '^a(b*)$'.
    """
    matching = r"^a(b*)$"
    if re.search(matching, text):
        return "We've got something here"
    else:
        return "No such luck"

# New File


def find_sequences(string):
    """
    Check if a string matches the pattern '^[a-z]+_[a-z]+$' with case insensitivity.
    """
    pattern = r"^[a-z]+_[a-z]+$"
    return "Yes" if re.search(pattern, string, re.IGNORECASE) else "NO"

# New File


def remove_escape_sequences(text):
    """
    Remove escape sequences from a text.
    """
    reaesc = re.compile(r'\\x1b[^m]*m')
    return reaesc.sub('', text)


# Example usage of the function
text = "\\t\\u001b[0;35mgoogle.com\\u001b[0m \\u001b[0;36m216.58.218.206\\u001b[0m"
print("Original Text: ", text)
print("New Text: ", remove_escape_sequences(text))

# New File


def remove_short_words(text):
    """
    Remove words shorter than four characters from a text.
    """
    shortword = re.compile(r'\\W*\\b\\w{1,3}\\b')
    return shortword.sub('', text)


# Example usage of the function
print(remove_short_words("The quick brown fox jumps over the lazy dog."))

# New File


def capital_words_spaces(str1):
    """
    Insert spaces before capital letters in a string.
    """
    return re.sub(r"(\\w)([A-Z])", r"\\1 \\2", str1)
