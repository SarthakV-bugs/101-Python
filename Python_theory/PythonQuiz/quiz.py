import pandas as pd
import json
import time

from sympy import false

with open('questions.json', 'r') as f:
    ques = json.load(f)

df = pd.DataFrame(ques)
# print(df)

score_chart = pd.DataFrame(columns=['Name', 'scores', 'Time taken'])
# print(score_chart.columns)



def play_quiz():
    scores= 0
    total_ques = len(df)    #for final score computing

    #iterate to access each row of the df(basically, using iter-rows() or i-loc/loc
    start_time = time.time()
    print('Starting the game...')
    for i in range(len(df)):
        print(f"Question {df.iloc[i,0]}")
        print(f"A): {df.iloc[i,1]}")
        print(f"B): {df.iloc[i,2]}")
        print(f"C): {df.iloc[i,3]}")
        print(f"D): {df.iloc[i,4]}")
        # break
        correct_answer = df.iloc[i, 5]
        # print(correct_answer)
        while True:
            user_answer = input("Enter your answer as A/B/C/D:").upper()
            if user_answer in ["A","B","C","D"]:
                break
            else:
                print("Read the format of answer once again")


        if user_answer == correct_answer:
            scores += 1
            print("Correct")
        else:
            print(f"Incorrect, correct answer is {correct_answer}")

        print()

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Score {scores} out of total questions {total_ques}")
    print(f"Time taken: {time_taken:.2f} secs")

    return scores, time_taken



def main():
    global score_chart

    while True:
        user_name = input("Enter your name, player:") #press exit to quit

        if not user_name.isalnum():
            print("Invalid, name should have alphabet and numbers")

        if user_name == 'exit':
            print("Exiting the game...")
            break



        print(f"Welcome {user_name}, let's start your Python quiz!")
        scores, time_taken = play_quiz()



        new_row = pd.DataFrame({'Name':[user_name], 'scores':[scores], 'Time taken': [time_taken]})
        score_chart = pd.concat([score_chart, new_row], ignore_index=True)
        sorted_score_chart = score_chart.sort_values(by = 'scores', ascending=False)
        # print(sorted_score_chart)
        print(sorted_score_chart.to_string(index=False))
        # print(score_chart)


if __name__ == '__main__':
    main()
