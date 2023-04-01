import os
import boto3

# Recuperar las credenciales de AWS de las variables de entorno
region = 'us-west-2'
access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Crear una instancia de cliente de S3 con las credenciales recuperadas
s3 = boto3.client('s3', region_name=region, aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Especificar la restricción de ubicación para el bucket
location = {'LocationConstraint': region}

# Crear un bucket
bucket_name = 'mi-bucket-s3-test'
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

# Verificar que el bucket se ha creado correctamente
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]

if bucket_name in buckets:
    print(f"Bucket '{bucket_name}' creado exitosamente")
else:
    print(f"Error al crear el bucket '{bucket_name}'")