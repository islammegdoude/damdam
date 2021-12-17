woker_File = open("woker.txt", "a")
list_of_lines = ["\nThis is a first line ", "\nThis is a second line ", "\nThis is a third line "]
woker_File.writelines(list_of_lines)
woker_File.close()
