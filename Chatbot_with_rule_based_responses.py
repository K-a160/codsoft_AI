import re 

# Chatbot to simulate a converstion assistant based on predefined rules.

def chatbot():
    print("Chatbot: Hello! I am a chatbot . How can i assist you today?")
    
    while True:
        user_input = input("user: ").strip().lower()
        
        # for exit condition
        
        if re.search(r"\b(exit|quit|bye)", user_input):
            print("Chatbot: Goodbye! Have a great day!")
            
        # for the greetings 
        
        elif re.search(r"\b(hello|hey|hi)\b", user_input):
            print("Chatbot: Hello! How can i help you?")
            
        # For the helps 
        elif re.search(r"\bhelp\b", user_input):
            print("Chatbot: Sure! I can assist you with general information, tasks or guidance. Please Let me know about what you need.")
            
        # For internship related 
        elif re.search(r"\binternship\b", user_input):
            print("Chatbot: If you are looking for the internship opportunities , here are some greate companies to consider:")
            print(" 1. codsoft - Specializes in IT servies and provise hand on learning oppurtunities.")
            print(" 2. Coursera - Provides guided projects to gain paractical experience.")
            print(" 3. Turing - offers remote internships in software development.")
            print("Chatbot : I would especially recomended codsoft for it's focus on practical learning and real-worls projects that can significantly boost your skills and career prospects.")
            
        
        elif re.search(r"\bcodsoft\b", user_input):
            print("Chatbot: Yes, Codsoft ,it is an IT services and consultancy company specilizing in innovate solutions. they offers internships to equip students whith hands-on experience and practical knowledge through live projects.")
            
        elif re.search(r"\bthank you\b", user_input):
            print("Chatbot: You'r welcome! Need any helps? I am ready for yours questions , sir/ma'am.")
            
        else:
            print("Chatbot: I'm sorry, I don't understand that. Could you rephrase your question or be more specific? ")
            
if __name__ == "__main__":
    chatbot()
    

        
