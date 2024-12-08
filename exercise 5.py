my_list = ["Hello","Morning", "Lazy", "Hello"]
search_string = input("Enter a string you want to search: ")
replace_string = input("Enter a string you want to replace: ")
for i in range(len(my_list)):
  if my_list[i]==search_string:
    my_list[i]=replace_string
print(my_list)
