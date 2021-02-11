from datetime import datetime

#
# f = open("StrangeFile.txt", "w")
# f.close()


init_print = print

# def logging():
#     with open("StrangeFile.txt", "a", encoding="utf-8") as f:
#         now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
#         f.write(f'{now} User inputted "{input_var}" led to message "{message}"\n')


right_moves = ["right", "right", "right", "up", "level",
               "right", "heart", "right", "right", "down", "heart", "right", "up", "up", "level",
               "left", "up", "up", "level",
               "left", "heart", "left", "left", "left", "left", "up", "heart", "level",
               "left", "up", "up", "heart", "right", "down", "level",
               "right", "right", "right", "right", "right", "heart", "up", "level",
               "left", "left", "left", "left", "left", "heart", "up", "level",
               "right", "right", "up", "level",
               "right", "down", "right"]

dragons_places = [0, 0, 0, "right", "left",
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, "down", "down", "down", "down", 0, 0,
                  "up", 0, "right", 0, "up", 0, 0,
                  "any", 0, 0, 0, 0, 0, "down", 0,
                  "up", "up", 0, 0, 0, 0, 0, 0,
                  "left", 0, 0, 0,
                  0, 0, "down"]

# back_flag = "left"
# level_var = 1


def print(message, input_var=None):
    init_print(message)
    if input_var:
        with open("StrangeFile", "a", encoding="utf-8") as f:
            now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            f.write(f'{now} User inputted "{input_var}" led to message "{message}"\n')


def main(level_var=1):
    back_flag = "left"

    for i in range(len(right_moves)):
        if right_moves[i] == "heart":
            message = "Congratulations, you find heart. That's help you to free the Pegasus!"
            print(message)

            continue
        if right_moves[i] == "level":
            level_var += 1
            message = f"Well done, you you rich level {str(level_var)}"
            print(message)

            continue

        input_var = input("Choose direction (right, up, left, down):")

        if right_moves[i] == input_var:
            message = "Good job! One small step for a hero one giant leap for a python knowledge meaning"
            print(message, input_var)

            if input_var == "right":
                back_flag = "left"
            elif input_var == "left":
                back_flag = "right"
            elif input_var == "up":
                back_flag = "down"
            elif input_var == "down":
                back_flag = "up"
            continue
        elif back_flag == input_var:
            message = "You can't go back to where you were before! Dragons will smell your fear and will find you"
            print(message, input_var)

            break
        elif dragons_places[i] == input_var:
            message = "The hero died. Try to save Pegasus again"
            print(message, input_var)

            break
        elif dragons_places[i] == "any":
            message = "The hero died. Try to save Pegasus again"
            print(message, input_var)

            break
        else:
            message = "Wrong-way to go! You lose one or more hearts"
            print(message, input_var)

            break
    else:
        message = "Congratulation! You have save the Pegasus"
        print(message, input_var)


if __name__ == "__main__":
    f = open("StrangeFile.txt", "w")
    f.close()
    main()
