# EmailBlaster
Bulk email sender utility with markdown template and multi-language support.

Initially created for sending recruitment follow-up emails for [BIT PoliTO](https://github.com/BITPoliTO) team, can be easily modified to fit your needs. 

## Installation
Python 3 is required
```console
# install required Python 3 modules
$ python -m pip install -r requirements.txt
```

## Setup
The following files should be set up:
- File `export.csv` should contain the columns `name`, `email` and `language`
- File `configuration.json` should be set up with your SMTP server's configuration as well as with the subject of the emails you'd like to send
- File `template_en.md` should contain your *english* email template in valid markdown format
- File `template_it.md` should contain your *italian* email template in valid markdown format

The following keywords can be used in the email templates and will be substituted with the corresponding value:
- `{{ first_name }}` will be substituted with the person's first name retrieved from the first word in the field `name` of the CSV file
- `{{ full_name }}` will be substituted with the full content of the field `name` of the CSV file
- `{{ email }}` will be substituted with the email retrieved from the content of the field `email` of the CSV file
## Usage
### Method 1: Run directly
**EmailBlaster** can be run directly by executing the following command
```console
$ python MailBlaster.py
```
Using this method the program will run with some default parameters:
- File `export.csv` will be used as default csv file
- File `configuration.json` will be used as default configuration file
- File `template_en.md` will be used as default markdown *english* email template file
- File `template_it.md` will be used as default markdown *italian* email template file
### Method 2: Import script
**EmailBlaster** can be imported in your Python script and used in the following way
```python
from EmailBlaster import EmailBlaster
my_sender = EmailBlaster('configuration.json', 'test.csv',
                'template_en.md', 'template_it.md')
my_sender.send()
```  
  
    
  
##### ⚙ Created for the love of task automation by [Lorenzo Callegari](https://github.com/lorcalhost)