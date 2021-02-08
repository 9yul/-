import smtplib
from email.mime.text import MIMEText
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('계정 이름', '계정 비밀번호')
msg = MIMEText('내용 : 내용.')
msg['Subject'] = '제목 : 제목.'
s.sendmail("보내는 메일.", "받는 메일.", msg.as_string())
s.quit()