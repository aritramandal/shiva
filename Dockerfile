# Faster & Secure & Special Container #
# Thanks to mkaraniya & zakaryan2004

FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/suhaash02/Dextro_userbot /root/Dextro_userbot
WORKDIR /root/AsenaUserBot/
RUN pip3 install -r requirements.txt
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
CMD ["python3","-m","userbot"]
