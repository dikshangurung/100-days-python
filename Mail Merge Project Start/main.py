with open("./Input/Names/invited_names.txt","r") as names:
    name_lists = names.readlines()
    for name in name_lists:
        print(name.strip())

with open("./Input/Letters/starting_letter.txt","r") as letters:
    letter = letters.read()
    with open("./Input/Names/invited_names.txt", "r") as names:
        name_lists = names.readlines()
        for name in name_lists:
            good = name.strip()
            with open(f"./Output/ReadyToSend/{good}.txt","w") as new:
                new.write(letter.replace("[name]",f"{name}"))
# with open("./Input/Letters/starting_letter.txt","r") as letters:
#     with open("test.txt","w") as test:
#         ok = letters.read()
#         test.write(ok.replace("[name]","Hello"))
