if [ "$FLASK_ENV" == "development" ]
then
    python3 wsgi.py
else
    /usr/local/bin/gunicorn wsgi -w 2 -b :5000 --worker-class gevent --reload;
fi
