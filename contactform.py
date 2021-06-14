from flask import Flask, request, redirect
import yagmail
app = Flask("contactform")


@app.route('/send', methods=['POST'])
def signup():
    message = request.form['Message']
    from_email = request.form['Email']
    name = request.form["Name"]
    content = "The message is '" + message + "' from " + name + " at " + from_email
    print(content)
    content = f"The message is '{message}' from  {name} at {from_email}"
    print(content)
    yag_client = yagmail.SMTP('jtrip.sending', 'yntUu73PQGAeu6i')
    yag_client.send('adrienne.patterson.24@gmail.com', 'new contact entry', content)
    return redirect(request.referrer)


@app.route('/', methods=['GET'])
def contact():
    return '''
    <form action="/send" method="POST">
    <input name="Name" type="text">
    <input name="Email" type="text">        
    <input name="Message" type="text">
    <button type="submit">Submit</button>
    </form>
    '''

