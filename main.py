from datetime import datetime
import string
import secrets

def generate_password(length: int = 12) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))

    return password


def save_password(password: str, filename: str = "passwords.txt") -> None:
    timestamp = datetime.now().strftime("%d-%B-%Y- %H:%M:%S")
    with open(f"{filename}", "a") as f:
        f.write(f"[{timestamp}] {password}\n")
        print(f"Password saved to {filename}.")

password = generate_password()
print(f"Your password is: {password}")
save_password(password)












