# project-bootstrap
A quick way to bootstrap applications for rapid prototyping.  Creates slack channel, github repo, and dev EC2 instance

## Setup

1. Install Dependencies
```
pip install --user -r requirements.txt
```
1. Configure `.env` file
```
cp .env.sample .env
# edit .env to populate credentials
```

## Running
```
python bootstrap.py
```
