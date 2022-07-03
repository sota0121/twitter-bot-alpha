# twitter-bot-alpha
A fanny twitter bot


## Deploy to Google Cloud Functions

```bash
cp .env-template .env
# set env vars to .env
deploy_cloud_function.sh
trigger_cloud_function.sh
```


## Usage on local machine

```bash
# =======
# setup
# =======
cp .env-template .env
# set env vars to .env
python -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt

# =======
# run
# =======
python -m bot
```
