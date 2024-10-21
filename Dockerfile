FROM public.ecr.aws/lambda/python:3.8

COPY server.py .

CMD ["server.lambda_handler"]


