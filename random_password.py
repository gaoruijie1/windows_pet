import random
import string

#随机密码字符串

def get_random_string(length):
    #位数
    num_count = random.randint(1, length - 1)#数字位数
    letter_count = length - num_count#字母位数

    #生成数字(通过遍历获取相应长度的字符串）
    num_list = [random.choice(string.digits) for _ in range(num_count)]
    #string,digits  生成数字

    #生成字母(通过遍历获取相应长度的字符串）
    letter_list = [random.choice(string.ascii_letters) for _ in range(letter_count)]
    #string.ascii_letters 生成大小写字母

    #将数字字母合并
    all_list = num_list + letter_list

    #随机排列
    random.shuffle(all_list)


    #.join用来分割各个元素
    result = " ".join([i for i in all_list])
    return result

#生成十位数密码
password10 = get_random_string(10)
print(password10)