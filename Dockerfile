FROM public.ecr.aws/lambda/python:3.12

COPY server.py .

CMD ["server.lambda_handler"]


