from openai import OpenAI
import os
from dotenv import load_dotenv



load_dotenv()

client = OpenAI()

text_to_convert = '''
                30-03-2022 08.30-16.30
                31-03-2022 09.00-17.00
                07-04-2022 09.00-17.00
                10-04-2022 09.00-16.30

                '''
command = '''
    znajdź w poniższym tekście daty i godziny. zwróć je w formacie:
    "date: dd-mm-yyyy, start time: hh:mm, end time: hh:mm, description: description-text"
'''
command += text_to_convert

# '''
# 27-04-2022 08.10-17.00 1 zjazd 1.5 szyby
# 28-04-2022 08.30-16.30 1 zjazd 2 szyby do 6p
# 29-04-2022 09.00-17.00 1 zjazd 2 szyby
#
# 04-05-2022 08.30-16.15 3 zjazdy garaże 1 na łącznik
# 05-05-2022 08.30-17.30 1 zjazd na wnękę
# 06-05-2022 09.00-15.30 1 zjazd 2 szyby południową ściana
# 07-05-2022 09.30-17.30 1 zjazd 2 szyby
# '''

print(command)

# result = client.completions.create(
#     model='gpt-3.5-turbo-instruct',
#     prompt=command,
# )
#
# print(result.choices[0].text)
#
# print(result)


