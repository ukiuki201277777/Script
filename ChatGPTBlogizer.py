#   Script to enhance readability of ChatGPT logs when publishing them on the web
#
#   Usage:
#       1. Paste the log into the input.txt file.
#       2. Execute the script.
#       3. The output will be generated in output.html.
#
#   For more details, please refer to the following link:HobbyAI - How to create a script to format ChatGPT logs.
#   https://hobbyai.blog.jp/archives/19708268.html
#
#   Changelog:
#       Problematic Version
#       The following tag is included in the output, so make sure to remove it when using!! Unwanted lines may appear. You can handle it by running a batch file to remove duplicates or performing replacements! LOL
#       <pre  class="message" style="white-space: pre-wrap; margin-top: 20px; margin-bottom: 20px; font-weight: 400;"><div  class="message" style="font-weight: 400;"></div>
#
#   Fixed Version 5/26/2023
#   Addressed the issue of duplicate tags. Published on GitHub.
#   Script will be published on GitHub, so let's add English support ('ω')
#

CharacterA = "User"
CharacterB = "ChatGPT"

# Problematic Version
# def add_tags(character, text):
#     message_tag = '</pre>\n\n<pre  class="message" style="white-space: pre-wrap; margin-top: 20px; margin-bottom: 20px; font-weight: 400;"><div  class="message" style="font-weight: 400;">{}</div>'.format(character)
#     if text :
#         #author_tag = '<div>{}</div></pre>\n'.format(text)
#         author_tag = '{}\n'.format(text)
#         return message_tag + author_tag
#     else:
#         return message_tag

# Fixed Version 5/26/2023
def add_tags(character, text):
    
    # inline
    message_tag = '</pre>\n<pre  class="message" style="white-space: pre-wrap; margin-top: 20px; margin-bottom: 20px; font-weight: 400;"><div  class="message" style="font-weight: 400;">{}</div>'.format(character)
    # .css file　
    # message_tag = '</pre>\n<pre id="ai_log" class="ai_log"><div id="ai_log_author" class="ai_log_author">{}</div>'.format(character)

    if character == CharacterA or character == CharacterB:
        if text:
            author_tag = '{}\n'.format(text)
            return message_tag + author_tag
        else:
            return message_tag 
    else:
        return text + '\n' 
    
with open('input.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

output_text = ""
current_character = ""
for line in lines:
    line = line.strip()
    if line.startswith(CharacterA):
        if current_character != CharacterA:
            current_character = CharacterA
            output_text += add_tags(CharacterA, line[4:])
        else:
            output_text += add_tags("", line[4:])
    elif line.startswith(CharacterB):
        if current_character != CharacterB:
            current_character = CharacterB
            output_text += add_tags(CharacterB, line[10:])
        else:
            output_text += add_tags("", line[10:])
    else:
        output_text += add_tags("", line)

# 5/26/2023 Added     
output_text = output_text + "</pre>"
output_lines = output_text.split("\n")
output_text = "\n".join(output_lines[1:])

with open('output.html', 'w', encoding='utf-8') as output_file:
    output_file.write(output_text)