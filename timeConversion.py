def timeConversion():
    userTimeInput = int(input("Give time in seconds since midnight to be converted. "))

    if(userTimeInput < 0):
        return "Invalid message."

    seconds = userTimeInput
    minutes = seconds/60
    hours = minutes/60 
    meridianTime = ""

    if hours > 12:
        meridianTime = "PM"
    else:
        meridianTime = "AM"

    return(hours, minutes, seconds, meridianTime)