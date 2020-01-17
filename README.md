# Data Doser

This script creates a sequence of test files and delivers doses of them into an S3 bucket at random times over a period of time.

# Prerequisites:

- python3
- A working s3 bucket configured that you can write to.

### To setup
````
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````
### AWS env
Set your default AWS profile to be the one that has your S3 creds. e.g.

``
export AWS_PROFILE=philbart
``
## Usage
To start the data doser:

```
python doser.py 
    --chunks 5                              # 5 * numfiles = total files delivered
    --duration 100                          # seconds duration per chunk, duration * chunks + total duration
    --numfiles 20                           # 20 * chunks = total files delivered
    --template 'templates/template1.txt'
    --bucket 'inbox'
    --subfolder 'gw/opt/queue/pre_emails/'
    --mode 'random_delay'                   # sleep randomly or no sleep
    --prefix 'msg'                          # target file prefix
    --kmskey <key>
```

