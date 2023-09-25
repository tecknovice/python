from question import Question

question_prompts = [
    "What color are apples? \n(a)Red \n(b)Purple \n(c)Orange\n",
    "What color are bananas? \n(a)Green \n(b)Yellow \n(c)Orange\n",
    "What color are strawberries? \n(a)Black \n(b)Purple \n(c)Blue\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),

]

# print(questions)


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) +"/"+ str(len(questions)) +" correct")

run_test(questions)