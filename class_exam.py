import random
from states import states as capitals


# Generate 35 quiz files
for quizNum in range(35):

    # Create the quiz and answer key files
    quizFile = open(f'quizes/quiz{quizNum + 1}.rtf', 'a')
    # A Header In Every File
    quizFile.write(
        """
Name:                 Class period: \n
Date: \n
        """
    )
    quizFile.write(
        (' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1}) \n'
    )

    # Create answer file
    ansFile = open(f'quizesAns/quizAns{quizNum + 1}.rtf', 'a')
    # A Header For Every Answers File
    ansFile.write(
        (' ' * 20) +
        f'State Capitals Quiz Model Answer (Form {quizNum + 1}) \n'
    )

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)  # States list is shuffled evertime

    # Questions in the files
    for count, state in enumerate(states):

        # # #   creating choices
        capitalsValues = list(capitals.values())
        random.shuffle(capitalsValues)
        choices = []
        choices.append(capitals[state])
        for i in range(2):
            choices.append(capitalsValues[i])
        random.shuffle(choices)
        # # #   end

        quizFile.write(
            f"""
{count + 1}. What is the capital of {state}? \n
    a. {choices[0]}\n
    b. {choices[1]}\n
    c. {choices[2]}\n
\n
            """
        )
        ansFile.write(f"{count + 1}. {capitals[state]}\n")
    quizFile.close()
    ansFile.close()
