from email_ai import rewrite_email

email = input("Enter your email : \n")
tone = input("Choose your tone : \n")

result = rewrite_email(email, tone)
print(result)

