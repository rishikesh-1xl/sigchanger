import time
import random
import string


class TestDataGenerator:

    @staticmethod
    def generate_company_data():

        timestamp = str(int(time.time()))

        company_name = f"Auto{timestamp}"

        domain = f"auto{timestamp}.com"

        email = f"admin@{domain}"

        first_name = (
            "FN" +
            ''.join(
                random.choices(
                    string.ascii_letters,
                    k=5
                )
            )
        )

        last_name = (
            "LN" +
            ''.join(
                random.choices(
                    string.ascii_letters,
                    k=5
                )
            )
        )

        designation = (
            "QA" +
            ''.join(
                random.choices(
                    string.ascii_letters,
                    k=3
                )
            )
        )

        department = (
            "Dept" +
            ''.join(
                random.choices(
                    string.ascii_letters,
                    k=3
                )
            )
        )

        return {

            "company_name": company_name,

            "domain": domain,

            "email": email,

            "first_name": first_name,

            "last_name": last_name,

            "designation": designation,

            "department": department

        }