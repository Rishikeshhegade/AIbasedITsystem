import json
from difflib import get_close_matches
import re

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def preprocess_question(user_question: str) -> str:
    # Remove common question phrases
    user_question = re.sub(r'\b(what is|explain|define|how to)\b', '', user_question, flags=re.IGNORECASE)
    # Remove leading/trailing spaces and punctuation
    user_question = user_question.strip(' ?.,!')
    return user_question

def find_best_match(user_question: str, questions: dict) -> str | None:
    matches: list = get_close_matches(user_question, questions.keys(), n=1, cutoff=0.6)
    return matches[0] if matches else None

def chat_bot(user_input: str, knowledge_base: dict):
    user_question = preprocess_question(user_input)
    best_match: str | None = find_best_match(user_question, knowledge_base["questions"])
    
    if best_match:
        answer: str = knowledge_base["questions"][best_match]
        print(f"bot: {answer}")
        print('bot : Is this answer helpful?')
        new_answer = input('Enter yes or no (y/n): ')
        if new_answer.lower() == 'y':
            return "Do you have any other questions?"
        elif new_answer.lower() == 'n':
            best_match2: str | None = find_best_match(user_question, knowledge_base["questions2"])
            if best_match2:
                answer2: str = knowledge_base["questions2"][best_match2]
                print(f"bot: {answer2}")
                
if __name__ == "__main__":
    knowledge_base = load_knowledge_base("knowlaged_base.json")
    user_input = input("USER: ")
    
    while user_input.lower() != 'bye':
        response = chat_bot(user_input, knowledge_base)
        print(response)
        user_input = input("USER: ")
