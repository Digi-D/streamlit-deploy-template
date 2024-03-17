# Instructions for deployments

### To deploy to Digital Ocean App Platform

Run `poetry export --without-hashes --format=requirements.txt > requirements.txt`

Add `streamlit run app.py --server.port 8080 --server.headless true` to the App Settings > App Spec > `run` value in the YAML file

Temporarily deployed to https://seahorse-app-rcz8w.ondigitalocean.app/

Thank you
--------
Giant thanks to https://github.com/severinlindenmann/do_streamlit for getting me pointed in the right direction.
