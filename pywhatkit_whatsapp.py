import pywhatkit as pwk

count_up=7
count_down=5
body="\n The number of people entered the mall is "+str(count_up)+"\n"+ "The number of people left the mall is "+str(count_down)

# using Exception Handling to avoid unexpected errors
try:
    # sending message in Whatsapp in India so using Indian dial code (+91)

    # pwk.sendwhatmsg("mobile number with +91", message, time in hrs(24 hr), time in minutes)
    # pwk.sendwhatmsg("+91701*******", "Hi, how are you?", 9, 34)

    #pwk.sendwhatmsg("mobile number with +91", body, time in hrs(24 hr), time in minutes)
    # pwk.sendwhatmsg("+91701*******", body, 15, 4) # 3:04 pm

    # sending message instantly
    pwk.sendwhatmsg_instantly("+919400******", body)

    print("Message Sent Successfully!")  # Prints success message in console

    # error message
except:
    print("Error in sending the message")


# code for sending a whatsap message on a particular date and time

# import pywhatkit as pwk
# from datetime import datetime, timedelta
# import time
#
# # Set the target date and time
# target_date = "2024-09-20"
# target_time = "14:30"  # Time in HH:MM (24-hour format)
#
# # Convert strings to datetime objects
# target_datetime = datetime.strptime(f"{target_date} {target_time}", "%Y-%m-%d %H:%M")
# current_datetime = datetime.now()
#
# # Calculate the time difference
# time_difference = (target_datetime - current_datetime).total_seconds()
#
# # Message content
# count_up = 7
# count_down = 5
# body = "\n The number of people entered the mall is " + str(count_up) + "\n" + "The number of people left the mall is " + str(count_down)
#
# # Wait until the target time
# if time_difference > 0:
#     print(f"Waiting for {time_difference} seconds...")
#     time.sleep(time_difference)  # Wait until the specified date and time
#
# # Send the message at the target time
# try:
#     pwk.sendwhatmsg("+917012299397", body, target_datetime.hour, target_datetime.minute)
#     print("Message Sent Successfully!")
# except Exception as e:
#     print("Error in sending the message:", e)
