from config import *


def sign() -> None:
    """
    Sign the provided file
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    parser.add_argument("--key", type=str)
    args = parser.parse_args()
    fileIn = open(args.input, "rb")
    fileOut = open(args.output, "wb")
    filePrivate = open(args.key, "rb")
    key = rsa.PrivateKey.load_pkcs1(filePrivate.read())
    signed = rsa.sign(fileIn.read(), key, hashAlgorithm)
    fileOut.write(signed)
    print(f"Successfully signed and written to the \"{args.output}\" file!")


if __name__ == "__main__":
    sign()
