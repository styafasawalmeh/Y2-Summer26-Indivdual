import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def run_chat():
    print("You: (type exit to quit)")

    system_message = (
        "Your name is Hiba. You are a helpful and friendly assistant "
        "who helps students learn about anything they ask you to. be friendly, sweet and caring! you're like their best friend"
    )


    history = []

    while True:

        user_input = input(">> ")

        if user_input.lower() == "exit":
            break

        history.append({"role": "user", "content": user_input})
        #print('History:', history)
  # Add this BEFORE the API call to inspect the full response:
# print(response)

# Add this BEFORE the API call to see the full message history:
# print('History so far:', history)

# Parameters you will experiment with:
        response = client.messages.create(
        model='claude-haiku-4-5-20251001',
        max_tokens=300,   # try 50, then 500
        temperature=0.7,  # try 0, then 1
        system=system_message,
        messages=history
    )      
        print(response)
        reply = response.content[0].text
        print(f"Claude: {reply}")

    history.append({"role": "assistant", "content": reply})
run_chat()

    #step 1
    #usage.input_tokens: the text we input yo the AI
    #sage.output_tokens: the response we get back
    #step 3:
    #why does API need the full history very single time?
    #to process the history 

    #reflection_ lab2;
    #1. maybe when you go to a store that is very cheap so you buy this and this and that but the end price is a lot even if individual items are cheap
    #2.prediction, API doesn't work: the history won't hsve the uder's input 
    #3. i encoutred a namerror, an error with the hisroty and an indendation error, 
    #3. the fixes for them were pretty straightfowrward

