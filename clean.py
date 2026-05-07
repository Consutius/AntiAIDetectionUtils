import re

def cleanComments(file):
    with open(file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Remove triple-quoted strings (multi-line comments) - both ''' and """
    content = re.sub(r'(\'\'\'[\s\S]*?\'\'\'|\"\"\"[\s\S]*?\"\"\")', '', content)

    # Remove full-line # comments
    lines = content.splitlines(keepends=True)
    cleaned_lines = [line for line in lines if not line.lstrip().startswith('#')]
    content = ''.join(cleaned_lines)

    # Remove emojis and other non-BMP unicode symbols
    emoji_pattern = re.compile(
        "[\U00010000-\U0010FFFF"  # Non-BMP (most emojis)
        "\U00002700-\U000027BF"  # Dingbats
        "\U0001F300-\U0001FAFF"  # Misc symbols, emoticons, transport, etc.
        "\U00002600-\U000026FF"  # Misc symbols
        "\U00002300-\U000023FF"  # Misc technical
        "]+",
        flags=re.UNICODE
    )
    content = emoji_pattern.sub('', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)