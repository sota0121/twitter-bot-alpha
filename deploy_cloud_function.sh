gcloud functions deploy bot-alpha-basic \
--trigger-http \
--source=./bot/core.py \
--entry-point post_rnd_tweet \
--runtime=python39 \
--allow-unauthenticated \
--region=asia-northeast1 \
--env-vars-file .env.yml