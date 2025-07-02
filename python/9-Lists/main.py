'''
We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:

1. A list of the same messages but with all instances of the word dang removed.
2. A list containing the number of dang words that were removed from the message at that particular index.
'''

'''
ListOfWords => ListOfWords
" ".join([]) converts array into string
'''
def filter_messages(messages):
    filtered_list = []
    word_count = []

    for message in messages: #split list of messages into individual message 
        temp_list = []
        count = 0
    
        for word in message.split(): #split into individual words
            if word == "dang":
                count += 1
            else:
                temp_list.append(word)
        word_count.append(count)
        filtered_list.append(" ".join(temp_list))
    
    return filtered_list, word_count