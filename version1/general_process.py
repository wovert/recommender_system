"""
@author: wovert
"""
import random

albet = ["a", "b", "c", "d", "e", "f", "g", "h"]
albet_num = ["a", "b", "c", "d", "e", "f", "g", "h", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
albet_nums = ["X", "Y", "Z", "O", "P", "Q", "R", "S", "T", "a", "b", "c", "d", "e", "f", "g", "h", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

file_obj = open('./thefile.txt', 'w')
def produce():
  for num in range(0, 100):
    cookie = "".join(random.sample(albet_nums, 10))
    uid = "".join(random.sample(albet_num, 6))
    user_agent = "Mozilla Chrome Safari"
    ip = "1.1.1.1"
    video_id = "23090929"
    topic = "苹果发布会"
    order_id = "0"
    log_type = "1"
    final = cookie + "&" + uid + "&" + user_agent + "&" + ip + "&" + video_id + "&" + topic + "&" + order_id + "&" + log_type + "\n"
    print(final)
    file_obj.write(final)

produce()
file_obj.close()