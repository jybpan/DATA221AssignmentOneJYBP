def timeConversion():
    userTimeInput = int(input("Give time in seconds since midnight to be converted. "))

    seconds = userTimeInput
    minutes = seconds/60
    hours = minutes/60 
    meridianTime = ""

    if hours > 12:
        meridianTime = "PM"
    else:
        meridianTime = "AM"

    return(f"\nIt has been {seconds} seconds since Midnight, or:\n{round(minutes, 4)} Minutes\n{round(hours, 4)} Hours\nAnd it is in the {meridianTime}.")