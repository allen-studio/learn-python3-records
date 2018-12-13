def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # 把传入的参数stuff通过split进行分词
    return words # 分词方式为split（‘ ’），按照‘ ’中的空格分词,把句子拆成了列表

def sort_words(words):
    """Sort the words."""
    return sorted(words) # 对传入的列表list（words）进行排序,按字母a-z序列

def print_first_word(words):
    """Prints the first words after popping it off."""
    word = words.pop(0) # 选择列表中的第1个元素，列表list第一个元素的顺序是0
    print(word)

def print_last_word(words):
    """Prints the last words after popping it off."""
    word = words.pop(-1) # 选择列表中的最后1个元素，列表list最后一个元素的顺序是-1
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorted the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words) 

# 以下为练习，需要在terminal中运行python，然后把ex25当作模块导入使用
# import ex25
# sentence = "All good things come to those who wait."
# words = ex25.break_words(sentence)
# words
# sorted_words = ex25.sort_words(words) 
# sorted_words
# ex25.print_first_word(words)
# ex25.print_last_word(words)
# words
# ex25.print_first_word(sorted_words)
# ex25.print_last_word(sorted_words)
# sorted_words
# sorted_words = ex25.sort_sentence(sentence) 14 sorted_words
# ex25.print_first_and_last(sentence)
# ex25.print_first_and_last_sorted(sentence)
