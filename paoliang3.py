import re

f = open("C:\\Users\Lenovo\Desktop\\quanguodata10.txt",'r')
f2 = open("C:\\Users\Lenovo\Desktop\\qewdata2.txt",'w+')
#print(f.read())
f_r = f.readlines()
#print(f_r)
num1 = 0
for line in f_r:
    num1=num1+1
   # print(line)
    g=line.split('\"words\": \"')
    #print(g)
    for cc in g:
       if "log_id" in cc :
          g.remove(cc)
       for x in range(len(g)):
          # print(x)
           if g[x]!='':
               if g[x][:2]=='电话' and g[x-2] !='':
                   print('公司:',g[x-2][:-5])
                   xingxi = g[x-1][:-5].split("注册资本:")
                   xingming = xingxi[0]
                   try:
                       time = xingxi[1].split('成立日期:')
                       #print("日期:", time[1])
                   except:
                       pass
                   qq = re.search('电话:([\d-]*)', g[x][:-3])
                   #print(xingxi[0])
                   #print(qq.group(1))
                   if len(g[x-2][:-5])<6:
                       f2.write("公司:"+g[x-3][:-5]+",")
                   elif len(g[x-2][:-5])>35:
                       gongsi = g[x-2][:-5].split(',')
                       print(gongsi)
                       continue
                       f2.write("公司:"+gongsi[-1]+',')

                   else:
                       f2.write("公司:" +g[x-2][:-5]+',')
                   f2.write(xingming+',')
                   try:
                      f2.write("注册时间:" + time[1] + ',')
                   except:
                       pass

                   f2.write("电话:" + qq.group(1) + '\n')




file = open('C:\\Users\Lenovo\Desktop\\qewdata2.txt','r')
file2 = open('C:\\Users\Lenovo\Desktop\\0616data2.txt','w+')
a=set(file.readlines())
#print(a)
num = 0
for x in a:
    #print(x)
    file2.write(x)
    num = num +1
print(num)
file2.close()
print(num1)