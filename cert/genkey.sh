#!/usr/bin/env bash
rm -rf demoCA
mkdir -p demoCA/newcerts  
mkdir -p demoCA/private  
touch demoCA/index.txt
echo '01' > demoCA/serial

# ----------------------------------------------
SUBJECT="/C=CN/ST=Beijing/L=Beijing/O=gjingxi/OU=gjingxi/CN=center/emailAddress=ibopo@126.com"
openssl genrsa -des3 -out ca.key 2048
openssl rsa -in ca.key -out ca_decrypted.key
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt -subj $SUBJECT

# ----------------------------------------------
SUBJECT="/C=CN/ST=Beijing/L=Beijing/O=gjingxi/OU=gjingxi/CN=*.gjingxi.com/emailAddress=ibopo@126.com"
openssl genrsa -des3 -out server/server.pem 1024
openssl rsa -in server/server.pem -out server/server.key
openssl req -new -key server/server.pem -out server/server.csr -subj $SUBJECT
openssl ca -policy policy_anything -days 3650 -cert ./ca.crt -keyfile ./ca.key -in server/server.csr -out server/server.crt


# cat ./ca.crt >> server.crt

# --------------------------------------------
SUBJECT="/C=CN/ST=Beijing/L=Beijing/O=gjingxi/OU=gjingxi/CN=client/emailAddress=ibopo@126.com"
openssl genrsa -des3 -out client/client.pem 2048 
openssl req -new -key client/client.pem -out client/client.csr -subj $SUBJECT
openssl ca -policy policy_anything -days 3650 -cert ca.crt  -keyfile ca.key -in client/client.csr -out client/client.crt
openssl pkcs12 -export -clcerts -in client/client.crt -inkey client/client.pem -out client/client.p12

# --------------------------------------------
keytool -importcert -v -trustcacerts -alias client -file client/client.crt -keystore client/client.bks -storetype BKS -providerclass org.bouncycastle.jce.provider.BouncyCastleProvider -providerpath ./bcprov-jdk15on-146.jar -storepass xxxxxx
