def chatbot():
    print("Welcome to ShopSmart's Customer Support Chatbot!")
    print("How can I assist you today?")
    print("Type 'exit' anytime to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if 'exit' in user_input:
            print("Bot: Thank you for contacting ShopSmart. Have a great day!")
            break

        elif 'order status' in user_input or 'where is my order' in user_input:
            print("Bot: You can check your order status under 'My Orders' in your account section.")

        elif 'return' in user_input or 'refund' in user_input:
            print("Bot: Our return policy allows you to return items within 10 days of delivery. Would you like help initiating a return?")

        elif 'cancel' in user_input:
            print("Bot: You can cancel your order before it is shipped. Go to 'My Orders' and click 'Cancel Order'.")

        elif 'payment' in user_input or 'not going through' in user_input:
            print("Bot: Please check your internet connection or try a different payment method. Still facing issues? Call our support at 1800-123-456.")

        elif 'contact' in user_input or 'talk to agent' in user_input:
            print("Bot: You can reach us at support@shopsmart.com or call 1800-123-456. Our team is available 24/7.")

        else:
            print("Bot: I'm sorry, I didn't quite get that. Can you please rephrase or ask a different question?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()