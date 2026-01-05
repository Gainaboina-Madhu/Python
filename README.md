
<h1>Python</h1>
<ul>
    <li>Python is a high-level, interpreted, and general-purpose programming language.</li>
    <li><strong>Interpreted</strong> means Python code is executed line by line by an interpreter.</li>
    <li>Python does not need to be compiled into machine code before execution.</li>
</ul>

<h2>History of Python</h2>
<ul>
    <li>Python was created by <strong>Guido van Rossum</strong>.</li>
    <li>Development started in the late <strong>1980s</strong>.</li>
    <li>Python was first released in <strong>1991</strong>.</li>
</ul>

<h2>Uses of Python</h2>

<h3>Web Development</h3>
<ul>
    <li>Python is used to create websites and web applications.</li>
    <li>Frameworks: <strong>Django, Flask, FastAPI</strong></li>
    <li>Used for backend development and APIs.</li>
</ul>

<h3>Data Analysis</h3>
<ul>
    <li>Involves collecting, cleaning, and studying data.</li>
    <li>Libraries: <strong>NumPy, Pandas</strong></li>
    <li>Examples: Sales analysis, student result analysis, business reports.</li>
</ul>

<h3>Data Science</h3>
<ul>
    <li>Uses data analysis, statistics, and machine learning.</li>
    <li>Examples: Analyzing patterns and making predictions.</li>
    <li>Libraries: <strong>Scikit-learn, TensorFlow</strong></li>
</ul>

<h3>Machine Learning & Artificial Intelligence</h3>
<ul>
    <li>Widely used due to simple syntax and strong libraries.</li>
    <li>Libraries: <strong>TensorFlow, PyTorch, Scikit-learn</strong></li>
    <li>Examples: Chatbots, recommendation systems, face recognition.</li>
</ul>

<h3>Software & Desktop Applications</h3>
<ul>
    <li>Used to build desktop-based software.</li>
    <li>Examples: Calculator apps, billing systems, desktop management software.</li>
</ul>

<h3>Game Development</h3>
<ul>
    <li>Used to create simple games and prototypes.</li>
    <li>Library: <strong>Pygame</strong></li>
    <li>Examples: 2D games, quiz games, educational games.</li>
</ul>

<h3>Internet of Things (IoT)</h3>
<ul>
    <li>Used in hardware and IoT projects.</li>
    <li>Works with <strong>Raspberry Pi</strong> and sensors.</li>
    <li>Examples: Smart home systems, temperature monitoring, automation projects.</li>
</ul>

<h2>Python Installation (Windows)</h2>
<ol>
    <li>Go to <strong>https://www.python.org/downloads/</strong></li>
    <li>Download the latest Python version for Windows.</li>
    <li>Run the installer.</li>
    <li>Check the box <strong>“Add Python to PATH”</strong>.</li>
    <li>Click <strong>Install Now</strong>.</li>
    <li>Verify installation using Command Prompt:</li>
</ol>

<code>python --version</code>

</body>
</html>

BASIC PYTHON
-

Topic -1 : 📌 Data Types in Python
-
    - Data types are used to communicate with the Python programming language.
    - Python mainly understands the following basic data types:
        1. int
        2. flaot
        3. string

    - 1️⃣ Integer (int):
     - Used for whole numbers
     - Example: x = 10 or y = -5 or z = 0
    - 2️⃣ Float (float):
     - Used for decimal numbers
     - Example: a = 3.14 or b = 10.5 or c = -0.99
    - 3️⃣ String (str):
     - Used for text or characters
     - Written inside single quotes (' ') or double quotes (" ") or triple quotes (''' ''')
     - Example: name = 'Python' or message = "Hello World" or language = '''Programming'''

Topic -2 : 📌 Variables in Python
-
    - Variables are used to store data in a program.
    - A variable acts like a container that holds a value.
    - In Python, you do not need to declare the data type.
    - Python automatically understands the type based on the value.

**📝 Rules for Naming Variables in Python**
    - 1. Variable names must start with a letter (a–z, A–Z) or an underscore (_)
    - 2. Variable names cannot start with a number
    - 3. Variable names can contain letters, numbers, and underscores only (no spaces or special characters)
    - 4. Variable names are case-sensitive (age, Age, and AGE are different)
    **Examples** :
        - name = "John"
        - _age = 20
        - user1 = "Admin"
        - total_marks = 450
        
**📌 Address of a Variable in Python**
    - In Python, every variable is stored in memory, and each value has a unique address.
    - We can find the memory address of a variable using the built-in id() function.
    **Example** :
       x = 10
       print(id(x))

       output : 1289

Topic -3 : 📌 Type Conversion in Python
-
    - Type conversion means changing one data type into another.
    - 1. Implicit Type Conversion 
    - 2. Explicit Type Conversion

    1. Integer to Float (int → float)
    - An integer can be converted into a float using the float() function.
      x = 10            # int
      y = float(x)      # int to float
      print(y)          # 10.0
      print(type(y))    # <class 'float'>

    2. Integer to String (int → str)
    - An integer can be converted into a string using the str() function.
      num = 25           # int
      text = str(num)    # int to string
      print(text)        # '25'
      print(type(text))  # <class 'str'>
    3. Float to Integer (float → int)
    - A float can be converted into an integer using the int() function
      x = 9.8           # float
      y = int(x)        # float to int
      print(y)          # 9
      print(type(y))    # <class 'int'>
    4. Float to String (float → str)
    - A float can be converted into a string using the str() function.
      price = 99.99       # float
      text = str(price)   # float to string
      print(text)         # '99.99'
      print(type(text))   # <class 'str'>
    5. String to Integer (str → int)
    - A string can be converted into an integer using the int() function.
    -⚠️ The string must contain only numbers.
      num = "50"          # string
      value = int(num)    # string to int
      print(value)        # 50
      print(type(value))  # <class 'int'>
    6. String to Float (str → float)
    - A string can be converted into a float using the float() function.
    - The string can contain decimal numbers.
      price = "99.99"       # string
      amount = float(price) # string to float
      print(amount)         # 99.99
      print(type(amount))   # <class 'float'>
      
Print Condition:
-
     - 1. joined (+):
      - Numbers are converted into strings so they can be joined with text.
      - ➡️ Use this when working with the + operator.
       - age = 25
         print("Your age is " + str(age))

        ouput - Your age is25

