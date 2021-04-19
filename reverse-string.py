def reverse_method(text_string):
	import string   
	upper_letters = string.ascii_uppercase
	lower_letters = string.ascii_lowercase
	letters = lower_letters + upper_letters
	letter_dict = dict(zip(upper_letters, upper_letters[::-1]))
	l_letter_dict = dict(zip(lower_letters, lower_letters[::-1]))
	letter_dict.update(l_letter_dict)
	letter_dict[' '] = ' '
	result = ""
	for c in text_string:
		if c in letters:
			result += letter_dict[c]
		else: 
			result+=c
	return result



reverse_result = ''
with open('/home/arun/Desktop/reverse.txt', 'r') as reader:
    for line in reader.readlines():
         reverse_result += reverse_method(line)

text_file = open("/home/arun/Desktop/result.txt", "w")
n = text_file.write(reverse_result)
text_file.close()
