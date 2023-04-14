from config import *


def verify() -> None:
    """
    Verify the sign of the file
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    parser.add_argument("--sign", type=str)
    parser.add_argument("--key", type=str)
    args = parser.parse_args()
    fileContents = open(args.file, "rb").read()
    sign = open(args.sign, "rb").read()
    filePublic = open(args.key, "rb")
    key = rsa.PublicKey.load_pkcs1(filePublic.read())
    try:
        hashUsed = rsa.verify(fileContents, sign, key)
        print(f"Successfully verified a sign with the \"{hashUsed}\" hash!")
    except rsa.VerificationError:
        print("Verification failed!")


if __name__ == "__main__":
    verify()
