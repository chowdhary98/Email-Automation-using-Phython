# Python code to illustrate Sending mail from
# your Gmail account
def send_mail():

    import smtplib

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("sender_email_id", "sender_email_id_password")

    # message to be sent
    message = "Message_you_need_to_send"

    # sending the mail
    s.sendmail("sender_email_id", "receiver_email_id", message)

    # terminating the session
    s.quit()



# Python code to illustrate Sending mail
    # to multiple users
    # from your Gmail account
def send_mail_to_users_containing_same_message():

    import smtplib

    # list of email_id to send the mail
    email_list = ["abcd@gmail.com", "xyz@gmail.com"]

    for email in email_list:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("sender_email_id", "sender_email_id_password")
        message = "Message_you_need_to_send"
        s.sendmail("sender_email_id", email, message)
        s.quit()

# Python code to illustrate Sending mail
    # to multiple users
    # containing different messages
    # from your Gmail account
def  send_mail_to_users_containing_different_message():

    import smtplib

    # list of email_id to send the mail
    email_list = ["abcd@gmail.com", "xyz@gmail.com","zzzz@gmail.com"]
    # list of messages to be send
    message_list=["Good Morning","Good Afternoon","Good Evening"]
    #  email_list and message_List has one to one correspondence

    for i in range(len(email_list)):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("sender_email_id", "sender_email_id_password")
        message = message_list[i]
        s.sendmail("sender_email_id",email_list[i], message)
        s.quit()





if __name__ == '__main__':
    send_mail()
    send_mail_to_users_containing_same_message()
    send_mail_to_users_containing_different_message()


