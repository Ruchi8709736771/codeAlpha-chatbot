import tkinter as tk
from tkinter import scrolledtext
import random
import pyttsx3
import datetime

# Responses dictionary
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "hi": ["Hi!", "Hello!", "Hey!"],
    "how are you": ["I'm doing great! How about you?", "I'm fine, thanks for asking!", "All good here!"],
    "bye": ["Goodbye! Have a nice day!", "See you later!", "Bye! Take care!"],
    "what is your name": ["I am ChatBot!", "You can call me ChatBot!", "I'm your friendly chatbot."],
    "time": [f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}"],
    "date": [f"Today's date is {datetime.datetime.now().strftime('%d-%m-%Y')}"],
    "joke": [
        "Why did the computer go to the doctor? Because it caught a virus!",
        "I would tell you a UDP joke, but you might not get it!",
        "Why do Java developers wear glasses? Because they can’t C#!"
    ]
}

# Function to get bot response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return "Hmm... I didn't understand that. Can you rephrase?"

# Function to speak the text using pyttsx3
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Function triggered when send button is clicked
def send_message():
    user_msg = entry_box.get()
    if user_msg.strip() == "":
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_msg + "\n", "user")

    bot_response = get_response(user_msg)
    chat_log.insert(tk.END, "Bot: " + bot_response + "\n\n", "bot")

    speak_text(bot_response)

    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
    entry_box.delete(0, tk.END)

    if "bye" in user_msg.lower() or "exit" in user_msg.lower():
        root.after(1500, root.destroy)

# Create main window
root = tk.Tk()
root.title("Advanced ChatBot")
root.geometry("500x550")
root.configure(bg="#222831")

# Chat display area
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#393E46", fg="white", font=("Arial", 12))
chat_log.tag_configure("user", foreground="cyan")
chat_log.tag_configure("bot", foreground="lightgreen")
chat_log.config(state=tk.DISABLED)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry area frame
entry_frame = tk.Frame(root, bg="#222831")
entry_frame.pack(fill=tk.X, padx=10, pady=10)

# Input box
entry_box = tk.Entry(entry_frame, font=("Arial", 14), bg="#393E46", fg="white", insertbackground="white")
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

# Send button
send_button = tk.Button(entry_frame, text="Send", font=("Arial", 12), bg="#00ADB5", fg="white", command=send_message)
send_button.pack(side=tk.RIGHT)

# Run the application
root.mainloop()
