import hashlib
import sys


def gen_license_key(email):
    hash_input = f"fd330f6f-3f41-421d-9fe5-de742d0c54c0{email}".encode()
    hash_output = hashlib.md5(hash_input).hexdigest()[:25]
    return '-'.join([hash_output[i:i+5] for i in range(0, len(hash_output), 5)])


def main():
    email = sys.argv[1]
    print("Email: " + email)
    print("Monokai Pro License Key: " + gen_license_key(email))


if __name__ == "__main__":
    main()
