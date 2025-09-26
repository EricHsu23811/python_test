# 檔案的讀取、寫入  # https://youtu.be/zdMUJJKFdsU?si=ChvywGijGA-PskYH&t=11422

# open("檔案路徑", mode="開啟模式")

# 絕對路徑  ex: D:/_EricOnly/code4reference/LocalGit_test/_repos_CodeTest/python_test/123.txt
# 相對路徑  以程式的位置做延伸 ex: 123.txt

# mode="r" 讀取
# mode="w" 覆寫
# mode="a" 在原先的資料後加寫

file1 = open("123.txt", mode="r")   # 相對路徑範例
file2 = open("D:/_EricOnly/code4reference/LocalGit_test/_repos_CodeTest/python_test/AbCdE.txt", mode="r") #絕對路徑範例

print(file1.read())    #讀出所有的   #file1.read()之後，print(file1.readlines())會變成空集合[]

file1 = open("123.txt", mode="r")   #再open一次後面print file才會有內容

# print(file2.readline())  #只讀一行

print(file1.readlines())

for line in file2:  # 如果前面的print(file1.read())有執行，這邊會print出來空集合[]
    print(line)     # 如果再做open一次給file1，就會print出來

file1.close()
file2.close()