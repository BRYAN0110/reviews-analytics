
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)

wc = {}
for line in data:
    words = line.split()   # split 的預設值為空白鍵 若使用split() 可避免掉空字串
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 

#for word in words:
#	print(word, wc[word])
#print(len(wc))

while True:
    find = input('請輸入欲查找的單字:')   
    if find in wc:
        print(find, '出現的次數為:', wc[find])
    elif find == 'QQQ':
    	break
    else:
        print('無此單字')