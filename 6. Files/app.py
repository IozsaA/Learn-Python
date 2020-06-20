my_file = open(r'C:\Users\WarFish\Documents\Facultate\Python\Files\data.txt')
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name: ')
my_file_writing = open("data.txt", "r")
my_file_writing.write(user_name)

my_file_writing.close()
