import smtplib
import time

my_id = input("Enter your Gmail ID: ")
my_password= input("Enter your Gmail Password: ")
recip = input("Enter reciptent Gmail ID: ")
reciptent = recip.split(",")
print("Enter your message:")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

print("=" * 80)
conn = smtplib.SMTP("smtp.gmail.com", 587)
print("EHLO: ", conn.ehlo())
print("=" * 80)
print("TLS: ", conn.starttls())
print("=" * 80)
conn.login(my_id, my_password)
print("Wait the message is being sent.")
results = conn.sendmail(my_id, reciptent, text)
if results == {}:
    print("RESULT: SUCCESS!")
else:
    print("RESULT: FAIL!")
    print("REASON: ", results)
    time.sleep(5)
conn.quit()
