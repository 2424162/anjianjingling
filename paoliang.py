import re

f = open("C:\\Users\Lenovo\Desktop\\0514data3.txt",'r')
f2 = open("C:\\Users\Lenovo\Desktop\\051111data.txt",'w+')

f_r = f.read()
print(f_r)
g=f_r.split('\"words\": \"')
for cc in g:
  if "log_id" in cc:
     g.remove(cc)
num =0
for x in range(len(g)):
    if g[x]!='':
        if g[x][:2]=='电话':
                 #if len(g[x-2][:-5])<4:
                   #  print("公司:",g[x-2][:-5])
                    # print('公司:',g[x-3][:-5])
                 xingming = g[x-1][:-5]
                 a =xingming.split('注册资本')
                 try:
                     b = a[1].split('成立日期:')
                 except:
                     pass
                 qq = re.search('电话:([\d-]*)',g[x][:-3])
                 try:
                  #print("电话:",qq.group(1))
                  if(len(qq.group(1))<7):
                          print(qq.group(1))
                          print(g[x-2][:-5])

                  if len(g[x-2][:-5]) < 5:
                      f2.write("公司:"+g[x-3][:-5]+',')

                  elif len(g[x-2][:-5]) > 30 :
                     num=num+1
                     continue
                  else :
                      f2.write('公司:'+g[x-2][:-5]+',')
                  f2.write(a[0] + ',')
                  f2.write("注册时间:" + b[1] + ',')
                  f2.write("电话:" + qq.group(1) + '\n')
                 except:
                     print(11)

print(num)

file = open('C:\\Users\Lenovo\Desktop\\0578data.txt','r')
file2 = open('C:\\Users\Lenovo\Desktop\\0616data.txt','w+')
a=set(file.readlines())
print(a)
num = 0
for x in a:
    #print(x)
    file2.write(x)
    num = num +1
print(num)
file2.close()