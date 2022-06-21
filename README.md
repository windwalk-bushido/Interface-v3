# Interface v3

Personal collection of websites that I'm using on a daily basis.

## How to clone & use project

Requirements:

- Python (3.6+)
- Pip

**Note**: commands below can be used on Linux. Not sure if it works on Mac/Windows.

```
git clone https://github.com/windwalk-bushido/Interface-v3
cd Interface-v3/
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
flask run
```

##

How to write/edit websites?
Open up any file in "data" directory and write it in format:

- name
- URL
- _empty row_
