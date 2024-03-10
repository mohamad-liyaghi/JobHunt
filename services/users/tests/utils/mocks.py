from faker import Faker

faker = Faker()
USER_PASSWORD = "1234FAKE_pass"


async def create_fake_user_credentials() -> dict:
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "bio": faker.text(max_nb_chars=120),
        "password": USER_PASSWORD,
    }
