def encode_better(og_message, key_message):
    message_v2 = []
    key_list = []

    for i in og_message:
        message_v2.append(ord(i) - 65)
    for i in key_message:
        key_list.append(ord(i) - 65)

    for i in range(0, len(message_v2)):
        key_num = i % len(key_list)
        message_v2[i] = (message_v2[i] + key_list[key_num]) % 58

    message_v3 = ""
    for i in range(0, len(message_v2)):
        message_v3 += chr(message_v2[i] + 65)

    return message_v3
