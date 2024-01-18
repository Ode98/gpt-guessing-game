import openai

openai.organization  = 'your organization id'
openai.api_key = "your api key"
openai.Model.list()


# Set 'gpt-3.5-turbo' or 'gpt-4', gpt 3.5 is faster and cheaper, gpt-4 is more accurate
gptModel = 'gpt-4'

def getResponse(game_round, questions_and_answers):
    questions_and_answers_readable = "\n".join(f"{dct}" for dct in questions_and_answers)

    if game_round == 1:
        return openai.ChatCompletion.create(
            model=gptModel,
            messages=[{"role" : f"system", "content" : f"You are playing a guessing game where you have to ask questions and narrow down what thing the user is thinking of. The question has to be able to be answered with yes or no. Ask your first question to narrow possibilities as much as possible."},],
        )
    else:   
        return openai.ChatCompletion.create(
            model=gptModel,
            messages=[{"role" : "system", "content" : f"You are playing a guessing game against an user where you have to ask questions and narrow down what thing the user is thinking of, it can be very specific thing like 'Godfather the movie', or it can very broad like 'war'. The previous questions and answers where q=question,a=answer,y=yes,n=no,x=don't know or it depends: {questions_and_answers_readable}. Now ask the next question that narrows down the possible answers as much as possible, you can also try to guess the thing based on the previous answers provided to you. The question has to be able to be answered with yes or no."},],
            temperature=0.5,
        )
    
def generateWord(difficulty_level = 1):
    return openai.ChatCompletion.create(
        model=gptModel,
        messages=[{"role" : "system", "content" : f"Make up some thing, object or concept, this is for a guessing game, let's use difficulty levels 1-3 where 1 is easy and 3 is hard, this time the difficulty level is {difficulty_level}, provide your answer in this format: your word here",}],
        temperature=1,
    )

def answerQuestion(word, question):
    return openai.ChatCompletion.create(
        model=gptModel,
        messages=[{"role" : "system", "content" : f"I give you a thing, object or concept and you have to answer the question regarding that. Your thing is '{word}', The question is {question}, answer with y, n or x where y=yes, n=no, x = it depends, or hard to say",}],
        temperature=1,
    )

     
def chooseGameMode(game_mode):
    if game_mode == "g":
        return "c"
    if game_mode == "c":
        return "g"
    if game_mode == "a":
        return "a"

def main():
    game_running = True
    game_round = 1
    questions_and_answers = []

    game_mode = input("Choose game mode: c = Answer questions, g = Ask questions, a = Make the ai play itself")

    word = ""
    if (game_mode == "g" or game_mode == "a"):
        word = generateWord().choices[0].message.content
        print(word)

    if game_mode == "c":
        print('Answer the questions with "y" for yes, "n" for no and "x" for I don\'t know or you are not sure. Input q to quit.')
        while game_running:
            question = getResponse(game_round, questions_and_answers).choices[0].message.content
            input_text = input(f"Round: {game_round}: {question}: ")

            if input_text == "q":
                game_running = False
            else:
                questions_and_answers.append({"q": question, "a" :input_text})
            game_round += 1

    if game_mode == "g":
        while game_running:
            question = input('Ask a question: ')
            answer = answerQuestion(word, question).choices[0].message.content
            print(answer)
            if (question == 'q'):
                game_running = False
    if game_mode == 'a':
        while game_running:
            question = getResponse(game_round, questions_and_answers).choices[0].message.content
            print(question)
            answer = answerQuestion(word, question).choices[0].message.content
            print(answer)

            if game_round > 25:
                game_running = False
            else:
                questions_and_answers.append({"q": question, "a" : answer})

            game_round += 1

    while game_running:
        chooseGameMode(game_mode)
        game_round += 1


if __name__ == "__main__":
    main()