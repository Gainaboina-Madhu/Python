
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

 - **1️⃣ Integer (int):**
 - Used for whole numbers
   
       - Example: x = 10 or y = -5 or z = 0
 - **2️⃣ Float (float):**
 - Used for decimal numbers
   
       - Example: a = 3.14 or b = 10.5 or c = -0.99
 - **3️⃣ String (str):**
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
      
           name = "John"
           _age = 20
           user1 = "Admin"
           total_marks = 450
            
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
      
Topic - 4: 📌 Print Condition
-
 - Step 1: Using a comma(,):
 - When using commas in print(), Python automatically adds a space between items.
 - Step 2: Using string concatenation (+):
 - If you want no extra space, you can use + to concatenate strings
 - Step 3: Using old-style string formatting (%):
 - Python allows using format specifiers:(%s → string,%d → integer%f → float)
 - Step 4: Using f-strings (curly braces {}):
 - f-strings let you put variables directly inside a string using {}

Topic - 5: 📌 Python String
-
 - In Python, a string is a sequence of characters enclosed in quotes
 - It can include letters, numbers, symbols or spaces
 - **1. Creating a String :**
 - Strings can be created using either single ('...') or double ("...") quotes.
   
     - **Example**:
  
           str = 'name','123'
   
 - **2. String Immutable**
 - Strings are immutable, which means that they cannot be changed after they are created.
 - To change a string, you need to create a new string.
   
 - **3. Memory Allocation**
 - Strings are stored in memory as a sequence of characters.
 - Each character has an index, starting from 0.
   
 - **4. Indexing**
 - You can access each character of a string using indexing.
 - **Forward Indexing:- Starts from 0,1,2,3 (first character).**
   
     - **Example**:
       
                name = "Madhu"
                print(name[0])  # M
                print(name[1])  # a
       
 - **Backward Indexing:- Starts from -1,-2,-3 (last character).**
   
     -  **Example**
       
                name = "Madhu"
                print(name[-1])  # u
                print(name[-2])  # h
        
- **5. Slicing and Skipping**
- get a part of the string using [start:end]
  
    -  **Example**
      
               name = "Kamal"
               print(name[0:3])  # mad (from index 0 to 2)
               print(name[:3])   # mad (from index 0 to 2)
       
- **Skipping**
- You can skip characters using a step [start:end:skip_value]
  
    -   **Example**
    
               name = "Kamal"
                print(name[0:5:2])  # Kml
        
- **Built in Function**
- 1. capitalize(): Converts the first character to uppercase and the remaining characters to lowercase.
     
     **Example**:
     
              text = "python"
              print(text.capitalize()) #output: Python
     
  2. title(): Converts the first letter of each word to uppercase.

     **Example**:

             text="python programming"
             print(text.title()
             output: Python Programming
     
  3. lower(): Converts all characters to lowercase.

     **Example**:

             a="HELLO"
             print(a.lower())
             output: hello
     
  4. upper(): Converts all characters to uppercase.
      
       **Example**:
     
             a="hello"
             print(a.upper())
             output: HELLO
     
  5. islower(): Checks if all characters are lowercase or not.

     **Example**:
     
             a="python"
             print(a.islower())
             output: True
     
  6. isupper(): Checks if all characters are uppercase or not.

     **Example**:
     
             b="python"
             print(b.isupper())
             output: False
      
  7. isalpha(): Checks if the string contains only alphabets.

     **Example**:
     
             b="python"
             print(b.isalpha())
             output: True
      
  8. isnumeric(): Checks if the string contains only numbers.

      **Example**:
     
             b="123"
             print(b.isnumeric())
             output: True
      
  9. isalnum(): Checks if the string contains alphabets and numbers.

     **Example**:
     
             b="abc123"
             print(b.isnumeric())
             output: True
      
  10. startswith(): Checks if the string starts with a given value.

      **Example**:
     
             b="Python"
             print(b.startswith("Py"))
             output: True
    
  11. endswith(): Checks if the string ends with a given value.

      **Example**:
     
             b="Python"
             print(b.endswith("Py"))
             output: False
    
  12. replace(): Replaces one value with another.

      **Example**:
     
             text="Hello Map"
             print(text.replace("Map", "World"))
             output: "Hello", "World"
    
      
  13. Membership Operator (in, not in): Checks if a character or word exists in a string.

      **Example**:
     
             text = "Python Programming"
             print("Python" in text)
             print("Java" not in text)
             output: True
                     True

    
  14. count(): Counts how many times a character appears.

      **Example**:
      
             text = "banana"
             print(text.count("a"))
             output: 3

  15. index(): Returns the index position of a character.

      **Example**:
      
             text = "Python"
             print(text.index("t"))
             output: 2

  16. ASCII Concepts – ord() and chr()
       ord() – Character to ASCII value
      
      **Example**:
      
              ord("A")
              output: 65
      
       chr() – ASCII value to Character
      
      **Example**:
      
              chr(65)
              output: A
      
  17. split(): Splits a string into a list.

      **Example**:
      
              text = "Hello World"
              print(text.split())
              output: ['Hello', 'World']

  
  18. join(): Joins elements of a list into a string.
      
      **Example**:
      
              words = ["Hello", "Kamal"]
              print(" ".join(words))
              output: Hello Kamal

# Topic - 5: 📌 Python List
 
- List is represented with []
- A list is: Ordered → items keep their position
- Mutable → you can change it after creation
- Indexed → each item has a number (index)
- Heterogeneous → can store different data types

           - my_list = [10, "apple", 3.5, True]

- **Indexing** :
- Forward and Backward indexing
- 
            - fruits = ["apple", "banana", "cherry"]
            - fruits[0]   # "apple"
            - fruits[1]   # "banana"
            - fruits[-1]  # "cherry" (negative index = from the end)

- **Slicing** :
- slicing creates a new list, not a view.
- we can access a sequence a characters
- 
           - nums = [1, 2, 3]
           - nums[0] = 100
           - print(nums)   # [100, 2, 3]
  
- **Built in functions:**
- append() – add one item to the end
- insert() – add at a specific index
- extend() – add multiple items
- remove() – by value
- pop() – by index (returns the item)
- clear() – remove everything

# Topic - 5: 📌 Python Tuple
- A tuple is:
- Ordered → items keep position
- Immutable → cannot be changed after creation
- Indexed → access via index
- Heterogeneous → can store different data types
- 
           - my_tuple = (1, "apple", 3.14, True)
           - t = (1, 2, 3)
           - t = (5,)     # adding a element to tuple

- **Indexing** & **Slicing** :
  
           - t = ("a", "b", "c", "d")
           - t[0]     # 'a'
           - t[-1]    # 'd'
           - t[1:3]   # ('b', 'c')

 - **Built in functions:**
 - count: Counts how many times a value appears in a tuple.
 - index: Returns the index (position) of the first occurrence of a value.

# Topic - 5: 📌 Python Set
- A set is:
- Unordered → no fixed position
- Mutable → can change after creation
- No duplicate values
- Unindexed → no index , no slicing and no skipping.

          - my_set = {1, 2, 3, 4}  #creating a set
          - s = set([1, 2, 2, 3]) 
          -  # {1, 2, 3}

-  **Built in functions:**
- add() – add one element to the set
- update() – add multiple elements (from list, tuple, set)
- remove() – remove a specific element (❌ error if not found)
- discard() – remove a specific element (✅ no error if not found)
- pop() – remove and return a random element
- clear() – remove all elements
- **Set Operations**
- union() – combine all unique elements
- intersection() – common elements
- difference() – elements in first set but not in second
- symmetric_difference() – elements in either set, but not both
 
# Topic - 5: 📌 Python Dictionary
- A dictionary (dict) is:
- Stores data as key : value pairs
- Unordered (in old Python), insertion-ordered 
- Mutable
- Keys must be unique and immutable
- Values can be any type

          - student = {"name": "Alex","age": 20,"marks": 85}
          - d = {}                # empty dictionary
          - d = dict()            # empty dictionary
          - d.pop("age")          # remove key
          - d.popitem()           # remove last inserted pair
          - del d["marks"]        # delete specific key
          - d.clear()             # remove everything
- **Built in functions:**
- keys() – returns all keys
- values() – returns all values
- items() – returns key–value pairs
- get() – safe value access
- update() – add/update pairs
- setdefault() – insert key if missing
- copy() – shallow copy

           - d = {"name": "Alex", "age": 20}
           - d["city"] = "NY"          # add key-value
           - d.update({"age": 21})     # update value
           - removed_value = d.pop("age")  # remove by key
           - last_item = d.popitem()       # remove last pair
          
# Python INTERMEDIATE
# Topic - 1: 📌 Python Conditional & Control statements:


