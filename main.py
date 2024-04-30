import csv
import random

def getContextFromCSV():
    # Open csv
    try:
        # with open('Test.csv', 'r') as file:
        with open('Dataset.csv', 'r') as file:
            reader = csv.DictReader(file)

            # If job_link column is missing in file return an error
            if 'context' not in reader.fieldnames:
                print(f"Error: 'context' column not found in the CSV file.")
                return None
            
            # Store all the about sections in a list
            listOfContext = []
            for row in reader:
                context = row['context']
                listOfContext.append(context)
            return listOfContext

    # If file not found return an error    
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def select_random_words(text):
    # Split the text into words
    words = text.split()
    
    # Check if the number of words in the text is less than 5
    if len(words) < 5:
        return "Text contains fewer than 5 words."
    
    # Randomly select 5 words from the list of words
    selected_words = random.sample(words, 10)
    
    return selected_words

def getAnswerFromCSV():
    # Open csv
    try:
        # with open('Test.csv', 'r') as file:
        with open('Dataset.csv', 'r') as file:
            reader = csv.DictReader(file)

            # If job_link column is missing in file return an error
            if 'answer' not in reader.fieldnames:
                print(f"Error: 'answer' column not found in the CSV file.")
                return None
            
            # Store all the about sections in a list
            listOfAnswers = []
            for row in reader:
                answer = row['answer']
                listOfAnswers.append(answer)
            return listOfAnswers

    # If file not found return an error    
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def select_random_words(text):
    # Split the text into words
    words = text.split()
    
    # Check if the number of words in the text is less than 5
    if len(words) < 10:
        return "Text contains fewer than 10 words."
    
    # Randomly select 5 words from the list of words
    selected_words = random.sample(words, 10)
    
    return selected_words

def getHitRate(selected_words, Answer):
    Answerlist = list(Answer.split(",")) 
    print("AnswerList: ", Answerlist)
    print("----------------------------------------------------------------------------------------------------------")
    Intersection = set(selected_words).intersection(Answerlist)
    HitRate = round(len(Intersection)/len(Answerlist) * 100, 2)
    return HitRate

def main():
    # Create list of context from the csv file
    listOfContext = getContextFromCSV()
    listOfAnswers = getAnswerFromCSV()
    print("Size of listOfContext:", len(listOfContext), "Size of listOfAnswers:", len(listOfAnswers))
    rn = random.randint(1, 600)
    randomContext = listOfContext[rn]
    Answer = listOfAnswers[rn]
    print("----------------------------------------------------------------------------------------------------------")
    print(randomContext)
    print("----------------------------------------------------------------------------------------------------------")
    print("Answer: ", Answer)
    print("----------------------------------------------------------------------------------------------------------")
    selected_words = select_random_words(randomContext)
    print("selected words: ", selected_words, "\n")

    Output = 'C++, Software Quality Engineering, SQL, Java, HTML/CSS'
    RandomOutput = 'Web, people, design, SQL, process'

    HitRate = getHitRate(selected_words, Answer)
    print("\nHitrate:", HitRate, "%")


if __name__ == "__main__":
    main()





