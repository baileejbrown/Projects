HEX_COLOURS = {"aquamarine4": "#458b74", "BlanchedAlmond": "ffebcd", "burlywood3": "#cdaa7d", "CadetBlue1": "#98f5ff",
               "CornFlowerBlue": "#6495ed", "DarkGreen": "#006400", "FloralWHite": "#fffaf0", "firebrick": "#b22222",
               "gold1": "#ffd700", "IndianRed": "#cd5c5c"}

colour = input("Enter colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print("Hex code for {} is {}".format(colour, HEX_COLOURS[colour]))
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")
