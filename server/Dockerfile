FROM sconecuratedimages/apps:python-3.5-alpine

RUN mkdir /test

COPY data_server.py /test

CMD SCONE_MODE=HW SCONE_ALPINE=1 SCONE_VERSION=1 python /test/data_server.py
