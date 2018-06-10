# Quiz = {
#     "Question": "A study at Techkid. Techkid has tradition of night coding. Do A night coding?",
#     # "Choice A": " A. Có",
#     # "Choice B": " B. Không",
#     "Choices": ["A. Có", "B. Không", "C. Không biết", "D. Không trả lời"],
#     "Right choice": "A"
# }




question_pack = [
    # 1
    {
       "question": "Có nhận ra giảng viên không?",
        "choices": ["A. Có", "B. Không", "C. Không biết", "D. Không trả lời"],
        "right_choice":"D"
    },
    {
        "question": "Có đi muộn ko?",
        "choices": ["A. Có", "B. Không", "C. 100k", "D. 200k"],
        "right_choice": "A"
    },
    {
        "question": "Trợ giảng có đẹp trai ko?",
        "choices": ["A. Có", "B. Không", "C. Anh là ai", "D. Trợ giảng là ai"],
        "right_choice": "C"
    }
]

q = question_pack[0]
# choices = q["choices"]
# for choice in choices:
#     print(choices)
# print(question_pack[-1]["choices"][1])
correct_answer_count = 0
for q in question_pack:
    print(q["question"])
    print()
    # print(Quiz["Choice A"])
    # print(Quiz["Choice B"])
    choices = q["choices"]
    print(*q["choices"], sep="\n")
    print()
    User_choice = input("Your answer? ").upper()
    # Users answer
    # Check user answer
    if User_choice == q["right_choice"]:
        print("Bingo")
        correct_answer_count +=1
    else:
        print("Nah")
print("{0} correct answers".format(correct_answer_count))
# percent = correct_answer_count / len(question_pack) * 100
# print("{0} % percent".format(percent))
print("{0} % là phần trăm câu đúng".format((correct_answer_count/len(question_pack))*100))

# BTVN
#  rút gắn phần thập phân số phần trăm
# Review : sai ở đâu và tại sao sai/đúng

