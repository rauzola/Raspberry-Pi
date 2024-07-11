def webpage(temperature, state):
    # Template HTML
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Control Page</title>
    </head>
    <body>
        <form action="./lighton">
            <input type="submit" value="Light on" />
        </form>
        <form action="./lightoff">
            <input type="submit" value="Light off" />
        </form>
        <p>LED is {state}</p>
        <p>Temperature is {temperature}</p>
    </body>
    </html>
    """
    
    return str(html)
