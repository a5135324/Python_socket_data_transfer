FROM sconecuratedimages/apps:python-3.5-alpine

RUN apk add --no-cache gcc g++ make libffi-dev openssl-dev
RUN pip install pycrypto
RUN mkdir /test

COPY server.py /test

CMD SCONE_MODE=HW SCONE_ALPINE=1 SCONE_VERSION=1 python /test/server.py
