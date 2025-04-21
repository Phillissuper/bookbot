def word_count(text):
    count_of_text = len(text.split())
    return print(f"Found {count_of_text} total words")

def number_for_each_character(text):
    Dict_count = {}
    text_to_evaluate = list(text.lower())

    for c in text_to_evaluate:
        if c.isalpha():
            if c in Dict_count:
                Dict_count[c] += 1
            else:
                Dict_count[c] = 1
    
    return sort_Dict(Dict_count)

def sort_Dict(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key = lambda item:  item[1], reverse=True))
    return sorted_dict

def print_dict(my_dict):
    result = []
    for key, value in my_dict.items():
        result.append(f"{key}: {value}")
    return "\n".join(result)