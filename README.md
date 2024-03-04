# Kuper

**A Tool for Backing Up Messages from One Chat to Another**

Kuper is a tool designed to facilitate the backup of messages from one Telegram chat to another designated chat.

# How to Run?

To run Kuper on your Telegram account, you need your `api_id` and `api_hash`, which you can obtain from [my.telegram.org](https://my.telegram.org). However, if for any reason you cannot obtain them yourself, you can use the default values provided inside `config.ini`.

## Run Steps

### Clone the Repository
```bash
git clone https://github.com/0xAFz/kuper.git
cd kuper
```

### Setup Virtual Environment (venv)
```bash
python3 -m venv .venv
```

### Activate the Virtual Environment
```bash
source .venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Setup config.ini
```bash
cp config.ini.example config.ini
```
### Set Your Phone Number
```bash
vim config.ini
```

### Run the Tool
```bash
python3 main.py
```

### Login to Your Account
Telegram will send a code to your Telegram account. Enter this code to log in to your account.


# License
[MIT](https://choosealicense.com/licenses/mit/)