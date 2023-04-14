from config import *


def generation() -> None:
    """
    Generate RSA keys of the provided size
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int)
    args = parser.parse_args()
    size = defaultKeySize
    if args.size is not None:
        size = args.size
    pub, priv = rsa.newkeys(size)
    publicFile = open(publicKeyName, "wb")
    privateFile = open(privateKeyName, "wb")
    publicFile.write(pub.save_pkcs1())
    privateFile.write(priv.save_pkcs1())
    print(
        f"Successfully wrote the public key to the \"{publicKeyName}\" file and the private key to the \"{privateKeyName}\"!")


if __name__ == "__main__":
    generation()
