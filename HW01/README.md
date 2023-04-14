# Homework 1

## Keys generation
```shell
python3 generateKeys.py [--size]
```
Examples:
```
python3 generateKeys.py
python3 generateKeys.py --size 512
```

## File signing
```shell
python3 generateKeys.py --input inputFile --output outputFile --key privateKeyFile 
```
Example:
```shell
python3 sign.py --input temp --output sign_temp --key private.pem
```

## Sign verification
```shell
python3 verify.py --file inputFile --sign signature --key publicKeyFile
```

Example:
```shell
python3 verify.py --file temp --sign sign_temp --key public.pem
```
