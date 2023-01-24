import datetime as dt
import pandas
import random
import smtplib

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
my_password = "the_app_password"
sender_email = "leumaselulakk@gmail.com"

data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

for bd in birthday_dict:
    # Check if today matches a birthday in the birthdays.csv
    if bd["month"] == month and bd["day"] == day:

        # pick a random letter from letter templates and replace the [NAME]
        # with the person's actual name from birthdays.csv
        random_letter = random.choice(letter_list)
        with open(f"letter_templates/{random_letter}") as letter:
            draft = letter.read()
            edited_letter = draft.replace("[NAME]", f"{bd['name']}")

        # Send the letter generated to the receiver's email address.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=my_password)
            connection.sendmail(from_addr=sender_email,
                                to_addrs="samuelkibirigek@gmail.com",
                                msg=f"Subject:Happy Birthday {bd['name']}\n\n{edited_letter}"
                                )
