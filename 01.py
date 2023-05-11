def compress_str(string):
    validation = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    if not set(string).issubset(validation):
        return "невалидная строка"
    result = []
    count = 0
    last_index = len(string) - 1
    for i in range(len(string)):
        current_char = string[i]
        if i != last_index and current_char != string[i + 1]:
            result.append(current_char)
            if count != 0:
                result.append(count + 1)
                count = 0
        else:
            count += 1
            if i == last_index:
                result.append(f"{current_char}{count}")
    return result


input_str = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
print(*compress_str(input_str), sep="")