print("Hello! I am a chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    elif user_input == "hello" or user_input == "hi":
        print("Chatbot: Hi! How are you?")
    elif user_input == "how are you":
        print("Chatbot: I am fine, thanks!")
    elif user_input == "what is your name":
        print("Chatbot: My name is CodeAlpha Bot!")
    else:
        print("Chatbot: I don't understand that.")