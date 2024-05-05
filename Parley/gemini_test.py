import os

import google.generativeai as genai

# Replace with your Gemini API key
API_KEY = "AIzaSyAkJik7N15J_knNLcpt7yEZbmCXjJN_SY4"

# Initialize the GenerativeAI client
genai.configure(api_key = API_KEY)

# Get the Gemini Pro model
model = genai.GenerativeModel('gemini-pro')
genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences=['x'],
        max_output_tokens=10,
        temperature=1.0)

def chat(user_input):
    """Handles user input and generates responses using Gemini."""
     # Start a new chat session

    while True:
        # Get user input
        user_message = user_input or input("You: ")

        # Send user message to Gemini model
        response = model.generate_content(user_message)
        response = response.text  # Get the text response

        # Print Gemini's response
        print("Gemini:", response)

        # Check for exit signal
        if response.lower() == "bye":
            break

        # Update chat history
        #chat_history = chat_history.update(text=user_message)

    print("Chat ended.")

# Start the chat loop
if __name__ == "__main__":
    chat(None)  # Start with an optional greeting message
