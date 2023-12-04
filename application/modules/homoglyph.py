from string import ascii_lowercase, ascii_uppercase
from application.utils.ui import Status

# Define a dictionary of homoglyphs to the Latin alphabet
homoglyphs = {
    'a': ['а', 'ɑ', 'ӑ'],
    'b': ['Ь', 'ɓ'],
    'c': ['ϲ', 'с'],
    'd': ['ԁ', 'ⅾ', 'ɗ'],
    'e': ['е', 'é', 'ê', 'è', 'ë', 'ē', 'ĕ', 'ė', 'ẹ'],
    'f': ['𝓯', '𝔣'],
    'g': ['ɡ', 'ց'],
    'h': ['һ', 'հ'],
    'i': ['і', 'í', 'ï', 'ı', 'ɩ'],
    'j': ['ϳ', 'ј'],
    'k': ['κ', '𝓀'],
    'l': ['ⅼ', 'ӏ'],
    'm': ['ⅿ', 'ｍ'],
    'n': ['ո', '𝓃', '𝔫'],
    'o': ['ο', 'о', 'ó', 'ô', 'ò', 'õ', 'ö', 'ơ', 'ø', 'ọ'],
    'p': ['р', '𝓅', '𝔭'],
    'q': ['զ', 'ԛ'],
    'r': ['г', '𝓇', '𝔯'],
    's': ['ѕ', 'ѕ̆', '𝓈', '𝔰'],
    't': ['т', '𝓉', '𝔱'],
    'u': ['ս', '𝓊', '𝔲'],
    'v': ['𝓋', '𝔳'],
    'w': ['ԝ', 'ѡ', '𝓌', '𝔴'],
    'x': ['х', '𝔁', '𝔵'],
    'y': ['у', 'ү', '𝓎', '𝔂', '𝔶'],
    'z': ['ᴢ', '𝓏', '𝔃', '𝔷'],
}

#def _has_latin_homoglyphs(input_string: str) -> list:
def _has_latin_homoglyphs(self):
    latin_alphabet = set(ascii_lowercase + ascii_uppercase)
    
    # List to store matching homoglyphs
    matching_homoglyphs = []

    # Check for homoglyphs in the input string
    for char in self.targetFileNameOnly:
        if char.lower() in latin_alphabet:
            continue
        else:
            for base_char, glyph_list in homoglyphs.items():
                if char in glyph_list or char.lower() in glyph_list:
                    matching_homoglyphs.append(char)
    
    if matching_homoglyphs:
        print(f"Found Homoglyphs: {matching_homoglyphs}")
        return Status.Warning
    else:
        # No Homoglyphs were found
        return None

    #return matching_homoglyphs