import csv
import json
import markdown
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from jinja2 import Template


class EmailBlaster():

    def __init__(self, config_path, csv_path, template_en_path, template_it_path, verbose=False):
        with open(config_path, encoding='utf-8') as f:
            self.config = json.load(f)
        self.csv_path = csv_path
        with open(template_en_path, 'r', encoding='utf-8') as md_en:
            self.template_en = Template(md_en.read())
        with open(template_it_path, 'r', encoding='utf-8') as md_it:
            self.template_it = Template(md_it.read())
        self.verbose = verbose

    def __login(self):
        try:
            s = smtplib.SMTP_SSL(host=self.config["server"], port=self.config["port"], timeout=10)
            s.login(self.config["username"], self.config["password"])
            return s
        except smtplib.SMTPAuthenticationError:
            print('[SMTP ERROR]: Unable to login, credentials may be wrong.')
            s.close()
            exit(-1)

    def send(self):
        server = self.__login()

        with open(self.csv_path, encoding='utf-8') as f:
            for r in csv.DictReader(f):
                if self.verbose:
                    print(f'Sending email to {r["email"]}')
                
                # Get correct template and render
                if r['language'] == 'English':
                    chosen_s = self.config['template']['subject_en']
                    chosen_t = self.template_en
                else:
                    chosen_s = self.config['template']['subject_it']
                    chosen_t = self.template_it
                rendered = chosen_t.render(
                    first_name=r['name'].split(' ')[0],
                    full_name=r['name'].split(' ')[1],
                    email=r['email']
                )
                html = markdown.markdown(rendered)

                # Format Email
                msg = MIMEText(html.encode('utf-8'), 'html', _charset='utf-8')
                msg['Subject'] = chosen_s
                msg['From'] = formataddr((self.config['display_name'], self.config['username']))
                msg['To'] = r['email']
                
                # Send Email
                server.sendmail(self.config['username'], [r['email']], msg.as_string())
                time.sleep(1)
            server.close()


if __name__ == '__main__':
    EmailBlaster('configuration.json', 'export.csv',
                'template_en.md', 'template_it.md', verbose=True).send()
