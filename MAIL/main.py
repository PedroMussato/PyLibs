from eobj import SendMail

# This is the HTML file with te email content
EMAIL_FILE = open("email.html", "r")

# Server login
LOGIN = "pedro.mussato@visio.com.br"
PASSWORD = "gNTapwERRwXTilD9"

# Email configuration
FROM = "Pedro Mussato"
TO = "tecnologia@pedromussato.com"
SUBJECT = "teste"


def procedures(LOGIN, PASSWORD, FROM, EMAIL_FILE, TO, SUBJECT):
    # as default is the google server
    # you can change this configuration specifying your e-mail server as:
    # e = SendMail("server.server: port")
    e = SendMail("smtp.uhserver.com: 465") # here I use as default the google server
    e.lgn(LOGIN, PASSWORD)
    e.conf(FROM, TO, SUBJECT)
    e.body(EMAIL_FILE)
    e.snd()


procedures(LOGIN, PASSWORD, FROM, EMAIL_FILE.read(), TO, SUBJECT)

EMAIL_FILE.close()
