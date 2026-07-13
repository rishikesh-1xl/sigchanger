# import time
# import random
# import string


# class TestDataGenerator:

#     @staticmethod
#     def generate_company_data():

#         timestamp = str(int(time.time()))

#         company_name = f"Auto{timestamp}"

#         domain = f"auto{timestamp}.com"

#         email = f"admin@{domain}"

#         first_name = (
#             "FN" +
#             ''.join(
#                 random.choices(
#                     string.ascii_letters,
#                     k=5
#                 )
#             )
#         )

#         last_name = (
#             "LN" +
#             ''.join(
#                 random.choices(
#                     string.ascii_letters,
#                     k=5
#                 )
#             )
#         )

#         designation = (
#             "QA" +
#             ''.join(
#                 random.choices(
#                     string.ascii_letters,
#                     k=3
#                 )
#             )
#         )

#         department = (
#             "Dept" +
#             ''.join(
#                 random.choices(
#                     string.ascii_letters,
#                     k=3
#                 )
#             )
#         )

#         return {

#             "company_name": company_name,

#             "domain": domain,

#             "email": email,

#             "first_name": first_name,

#             "last_name": last_name,

#             "designation": designation,

#             "department": department

#         }

import time
import random
import string


class TestDataGenerator:

    @staticmethod
    def generate_company_data():

        timestamp = str(int(time.time()))

        random_suffix = ''.join(
            random.choices(string.ascii_lowercase + string.digits, k=6)
        )

        unique_id = f"{timestamp}{random_suffix}"

        company_name = f"Auto{unique_id}"

        domain = f"auto{unique_id}.com"

        email = f"admin@{domain}"

        first_name = (
            "FN" +
            ''.join(random.choices(string.ascii_letters, k=5))
        )

        last_name = (
            "LN" +
            ''.join(random.choices(string.ascii_letters, k=5))
        )

        designation = (
            "QA" +
            ''.join(random.choices(string.ascii_letters, k=3))
        )

        department = (
            "Dept" +
            ''.join(random.choices(string.ascii_letters, k=3))
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
    
    @staticmethod
    def generate_user_data():

        timestamp = str(int(time.time()))

        first_name = (
            "FN" +
            ''.join(random.choices(string.ascii_letters, k=5))
        )

        last_name = (
            "LN" +
            ''.join(random.choices(string.ascii_letters, k=5))
        )

        email = f"user{timestamp}@mailinator.com"

        designation = (
            "QA" +
            ''.join(random.choices(string.ascii_letters, k=3))
        )

        department = (
            "Dept" +
            ''.join(random.choices(string.ascii_letters, k=3))
        )

        phone = "9876543210"

        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "designation": designation,
            "department": department
        }