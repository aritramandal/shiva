FROM suhaash02/Dexter_userbot:latest

#clonning repo 
RUN git clone https://github.com/suhaash02/Dexter_userbot.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
