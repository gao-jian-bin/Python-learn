# import os
import re
#
# s = 'my birthday is 2002-11-21,and my friend is 1992-01-06.'
# r = r'\d{4}-\d{2}-\d{2}'
# result = re.findall(r, s)
# print(result)
# result1 = re.match(r, s)
# print(result1)
text = "123 45 6789 012345 124"
pattern = r'\d{3}'  # 匹配包含3个数字的模式
matches = re.findall(pattern, text)
print(matches)


text = "This is a <div>example</div> of HTML."

pattern = r'<.*?>'  # 非贪婪匹配，匹配最短的标签
matches = re.findall(pattern, text)
print(matches)

