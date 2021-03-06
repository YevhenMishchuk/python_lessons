def get_input():
  #text entry and split string into the apart words
  command = input(": ").split()
  #assignment a variable (verb_word) to the word which is at position 0 in command ("say")
  verb_word = command[0]
  # condition check: 1. find verb_dict (position 24). 2. if verb_word in verb_dict then assign to variable (verb) the value (say) of the 
  # dictionary (verb_dict) by the key ("say")
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return
  
  # condition check: if length variable command >=2 than assign variable (noun_word) second word in the input string. Then print variable verb with argument
  #(noun_word). For print variable (verb) function (print) need known what it equals variable (verb). Than function find that variable (verb) have a value (say).
  #Then we have - print(say(noun_word)) or if we enter string - "say hello" -> print(say(hello)). Then function print need find what it equal variable (say) with
  #argument (hello). Go to position 23
  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))
#Function (print) find function (say). Function say return - 'You said "{}"'.format(noun). Argument - (noun) is equal (hello). Then function (print) print
# - 'You said "hello"'.
def say(noun):
  return 'You said "{}"'.format(noun)

verb_dict = {
  "say": say,
}

while True:
  get_input()