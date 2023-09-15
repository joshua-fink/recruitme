
'''

input = "Write three sentences about Sam Altman. End paragraph saying 'requested by Joshua Fink'"
# create a chat completion
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": input}])

# print the chat completion
print(chat_completion.choices[0].message.content)
'''