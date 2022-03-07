from flask import Flask, jsonify
import hashlib
import requests

app = Flask('app')


@app.route('/')
#sets the default page, we may remove this later
def hello_world():
    return 'This is the opening page'


#takes a string from the url and converts to a hashcode (Problem 1)
@app.route('/md5/<string>')
def md5machine(string):
    #hashes it
    hashed = hashlib.md5(string.encode())
    md5thing = hashed.hexdigest()
    output = {
      "input": string,
      "output": md5thing
    }
    return jsonify(output)


@app.route('/factorial/<num>')  #i don't know how to make exceptions WITHIN the url, so what i'm going to do is take any possible item from the user and then see if it works within normal python code
def fact(num):
    try:  #this exists incase they put in a string, and catches it and makes a different error message then if they had inserted a bad number.
        num = float(num)
    except:
        result = "ERROR: The value you have inserted is not a number! Please insert a integer greater then 0"
        output = {"input": num,"output": result}
        return jsonify(output)
    #okay so in order to check if its a int, we actually do need to make it a float which i know is weird but trust me
    intcheck = num.is_integer()
    if num >= 0 and intcheck:  #for this i'm going to say that 0 counts as a positive, since 1 is the factorial of 0
        fact = 1
        if num == 0:
            result = 1
        else:
            for i in range(1, int(num) + 1):
                fact = fact * i
            #in order to exist in the stame return statement, values are shifted from a number to a string, with num having int first so it loses its decimal places
            result = fact

    else:
        result = "ERROR: That is not a appropriate value! It must be greater then 0 and be a whole number (a integer)"
    output = {"input": num,"output": result}
    return jsonify(output)


@app.route('/fibonacci/<int:n>')
def calcfib(n):
    fiblist = []
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if n <= 0:
        result = "Error! Please enter a positive integer!"
    # if there is only one term, return n1
    elif n == 1:
        result = n1
    # generate fibonacci sequence
    else:
        while n > count:
            nth = n1 + n2
            # update values
            fiblist.append(n1)
            n1 = n2
            n2 = nth
            count += 1
        result = fiblist
    output = {"input": n,"output": result}
    return jsonify(output)


@app.route('/is-prime/<number>')
def prime(number):
    # reusing some parts of the code from the factorial section, as it is effective and useful for the prime section
    try:
        number = int(number)
    except:
        return "ERROR: The value you have inserted is NOT a number! Please insert an INTEGER greater than 0"
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                result = False
                break
        else:
            result = True
    else:
        result = "ERROR: The value you have inserted is not a PRIME number! Please insert an integer GREATER than 1"
    output = {"input": number,"output": result}
    return jsonify(output)
    
@app.route('/slack/<message>')
def slack(message):
  url = 'https://hooks.slack.com/services/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'
  try: 
    requests.post(url, json={'text': message})
    result = True
  except:
    result = False
  output = {"input": message,"output": result}
  return jsonify(output)

app.run(host='0.0.0.0', port=5080)
    
