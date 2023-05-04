import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'levyborgesvitoria@gmail.com' # substitua com seu próprio endereço de e-mail
smtp_password = 'souvitorioso'

# Criação da mensagem de e-mail
msg = MIMEMultipart()
msg['From'] = 'levyborgesvitoria@gmail.com' # substitua com seu próprio endereço de e-mail
msg['To'] = 'levyborgesvitoria@gmail.com' # substitua com o endereço de e-mail para o qual deseja enviar a mensagem
msg['Subject'] = 'Novo formulário enviado'

message = "Nome: " + form_data['nome'] + "\n" + \
          "E-mail: " + form_data['email'] + "\n" + \
          "Mensagem: " + form_data['mensagem']

msg.attach(MIMEText(message))

# Criação da conexão SMTP e envio do e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, msg['To'], msg.as_string())

print('Obrigado por entrar em contato conosco!')
