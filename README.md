# My_py


My_py  上传Git_Hub 文件


Text.py 上传
#上传 下载
git clone url
git status
git add -A
git comment -m "上传描述"

#版本回归

git log 
git log --pretty=oneline  #一行显示

git reset --hard 文件名

#ssh 
生成ssh
ssh-keygen -t rsa -b 4096 -C "1165053882@qq.com"

clip < ~/.ssh/id_rsa.pud
路径
C:\Users\asus\.ssh

#分支
git branch
#查看远程分支
git branch -a
#创建分支
git checkout -b "分支名"
#推送分支
git push --set -upstream origin 分支名

#跳转分支
git checkout 分支名
#合并分支
git merge 分支名




问题 
Commit failed - exit code 128 received, with output: '*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident name (for <>) not allowed'



需要到项目 .git\config文件最后加入

[user]
    name = 你的名字
    email = 你的邮箱
	
	
问题 不能git clone url新获取一个ssh
一般为ssh问题 
