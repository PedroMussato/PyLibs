import smtplib
import email.message as es


class SendMail(es.Message):
    def __init__(self, server="smtp.gmail.com: 587"):
        """
        Starting the super class and adding the header
        """
        super().__init__()
        self.add_header("Content-Type", "text/html")
        self.srv = smtplib.SMTP(server)
        self.srv.starttls()

    def lgn(self, login, password):
        """
        lgn = LOGIN
        :param login: email to login at the SMTP server
        :param password: password to the e-mail
        """
        self.srv.login(login, password)

    def conf(self, name_from, to, subject):
        """
        this method configure whom is sending the e-mail, whom will receive (can be more than one) and the email subject
        :param name_from: the name of whom is sending
        :param to: the email or emails to deliver (tuple with strings) ("example@gmail.com", "example@outlook.com")
        :param subject: the email subject
        :return: no return
        """
        self['From'] = name_from
        self['To'] = to
        self['Subject'] = subject

    def body(self, content):
        """
        This method captures an HTML objet reads it and configures it into the message object
        :param content: the
        :return:
        """
        self.set_payload(content)

    def snd(self):
        """
        snd = SEND
        """
        self.srv.sendmail(self['From'], self['To'], self.as_string().encode('utf-8'))

    def c(self):
        """
        c = CLOSE
        :return: this method do not return anything
        """
        self.srv.quit()
