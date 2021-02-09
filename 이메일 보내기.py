import smtplib
from email.mime.text import MIMEText
a = input("보낼 내용을 입력하세요:")
b = input("제목을 입력하세요:")
c = input("보낼 사람을 입력하세요:")
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('메일 이름', '비밀번호')
msg = MIMEText(a)
msg['Subject'] = b
s.sendmail("보낸 사람", c, msg.as_string())
s.quit()
