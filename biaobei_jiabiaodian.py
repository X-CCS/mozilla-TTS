# This file is used to add 标点 for Biaobei dataset

file_dir = '../Downloads/BZNSYP/ProsodyLabeling/000001-010000.txt'
output_dir = '../Downloads/BZNSYP/ProsodyLabeling/daibiaodian.txt'

def add_biaodian(input_chinese, input_pinyin):
    input_pinyin = input_pinyin.replace('\t', '').replace('\n', '').split(' ')
    index = 0
    for word in input_chinese:
        # print(index, word)
        if word in biaodian_right:
            # print("检测到右标点")
            input_pinyin[index-1] += word
        elif word in biaodian_left:
            # print("检测到左标点")
            input_pinyin[index] = word + input_pinyin[index]
        elif word in ['0','1','2','3','4','5','6','7','8','9','#',' ','\t']:
            # print("Special character detected")
            continue
        elif word == '儿':
            print(input_pinyin[max(0,index-1):min(len(input_pinyin), index+2)])
            # decision = ''
            # while decision != 'y' and decision != 'n':
                # decision = input("\"儿\"detected, index should increase? [y/n]")
            # if decision == 'y':
                # index += 1
            if index == len(input_pinyin):
                print("False")
                pass
            elif input_pinyin[index] == 'er5' or input_pinyin[index] == 'er2':
                index += 1
                print("True")
            else:
                print("False")
        else:
            index += 1
    return ' '.join(input_pinyin)

file = open(file_dir, 'r')
lines = file.readlines()
file.close()

# Create output txt file, empty content
output_file = open(output_dir, 'w')
output_file.close()

biaodian = "！ ？ 。 ＂ ＃ ＄ ％ ＆ ＇ （ ） ＊ ＋ ， － ／ ： ； ＜ ＝ ＞ ＠ ［ ＼ ］ ＾ ＿ ｀ ｛ ｜ ｝ ～ ｟ ｠ ｢ ｣ ､ 、 〃 》 「 」 『 』 【 】 〔 〕 〖 〗 〘 〙 〚 〛 〜 〝 〞 〟 〰 〾 〿 – — ‘ ’ ‛ “ ” „ ‟ … ‧ ﹏ ."
biaodian_left = "＃ ＄ （ ［ ｛ ｟ ｢ 「 『 【 〔 〖 〘 〚 〝 ‘ “ "
biaodian_right = "！ ？ 。 ＂ ％ ＆ ＇ ） ＊ ＋ ， － ／ ： ； ＜ ＝ ＞ ＠ ＼ ］ ＾ ＿ ｀ ｜ ｝ ～ ｠ ｣ ､ 、 〃 》 」 』 】 〕 〗 〙 〛 〜 〞 〟 〰 〾 〿 – — ’ ‛ ” „ ‟ … ‧ ﹏ ."

biaodian = biaodian.split(" ")
print(biaodian)

print("Preview file content:")
#for line in lines:
#    print(line)
print("DONE")

# Analyze file content
for row in range(0,len(lines),2):
    sample1 = lines[row]
    print(sample1)
    sample2 = lines[row+1]
    print(sample2)

    temp_output_str = add_biaodian(sample1, sample2)
    sample2 = '\t' + temp_output_str + '\n'

    # Write into output txt file
    output_file = open(output_dir, 'a')
    output_file.write(sample1)
    output_file.write(sample2)
    output_file.close()


print("DONE")
