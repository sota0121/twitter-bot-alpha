gcloud functions deploy bot-alpha-basic \
--trigger-http \
--entry-point tweet_from_cloud \
--runtime=python39 \
--project=twitter-bot-positive-demon \
--allow-unauthenticated \
--region=asia-northeast1 \
--env-vars-file .env.yml