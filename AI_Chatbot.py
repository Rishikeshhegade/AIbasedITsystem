import json
from difflib import get_close_matches
import re
def load_knowlaged_based(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowlaged_based(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file,indent=2)
        
def find_best_match(user_question:str, questions: list[str]) -> str | None:
    matches : list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def find_best_match2(user_question:str, questions2: list[str]) -> str | None:
    matches : list = get_close_matches(user_question, questions2, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowlaged_base: str)-> str| None:
    for q in knowlaged_base["questions"]:
        if q["question"] == question:
            return q["answers"]
        
def get_answer_for_question1(question: str, knowlaged_base: str)-> str| None:
    for q1 in knowlaged_base["questions2"]:
        if q1["question"] == question:
            return q1["answers"]
        
def chat_bot(user_input):
    knowlaged_base : dict = load_knowlaged_based("knowlaged_base.json")

    
              
    best_match : str | None = find_best_match(user_input, [q["question"] for q in knowlaged_base["questions"]])

    if best_match:
        answers: str = get_answer_for_question(best_match, knowlaged_base)
        print(f"bot: {answers}")
        
        print('bot : This anwser is help full or not')
            
        new_answer = input('Enter the yes or no y/n:  ')

        if new_answer.lower() == 'y':
            return "if any question for me?"
        elif new_answer.lower()=='n':
            best_match1 : str | None = find_best_match(user_input, [q1["question"] for q1 in knowlaged_base["questions2"]])
            if best_match1:
                answers2: str = get_answer_for_question1(best_match1, knowlaged_base)
                print(f"bot: {answers2  }")
if __name__ == "__main__":
    user_input = input("USER: ")
    while user_input != 'bye':
        response = chat_bot(user_input)
        print(response)
        user_input = input("USER:")


 
