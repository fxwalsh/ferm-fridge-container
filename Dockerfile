FROM fxwalsh/py-ard-cli as builder

WORKDIR /app

FROM builder

COPY arduino /app/ferm_controller
COPY python /app/pyBlynk

COPY run.sh /app/run.sh

ENTRYPOINT ["./run.sh"]

CMD ["echo","Image created"]