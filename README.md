# ChatterMate 🤖

**ChatterMate** is a Python-based chatbot that uses a neural network to process user inputs and provide smart responses. It leverages natural language processing (NLP) with spaCy and intent recognition to engage in conversations, offer educational support, and deliver funny replies. The chatbot is trained on a custom dataset in `intents.json` and uses PyTorch for its machine learning model.

---

## Features ✨

- **Intent Recognition:** Understands user intents with a trained neural network model. 🧠  
- **Educational Support:** Explains programming languages like Python, Java, JavaScript, C#, C++, HTML, CSS, and SQL. 📚  
- **Humorous Responses:** Shares jokes to make you smile! 😄  
- **NLP Processing:** Uses spaCy for tokenization and bag-of-words for text processing. 🗣️  
- **Custom Responses:** Delivers dynamic replies based on `intents.json`. 💬  
- **Context Awareness:** Maintains user context for personalized chats (extendable for future features). 🤝  

---

## Available Intents and Responses 🎉

### Greeting 👋
(e.g., "Hi", "Hello", "Good morning")

- "Hello! How can I assist you today?"
- "Hi there, what can I do for you?"
- "Hey! Need help with something?"

### Goodbye 👋
(e.g., "Bye", "Goodbye", "See you later")

- "Goodbye! Have a great day."
- "See you soon!"
- "Take care, feel free to ask me anytime."

### Thanks 🙏
(e.g., "Thanks", "Thank you", "Appreciate it")

- "You're welcome!"
- "Happy to help!"
- "Anytime!"

### Funny 😂
(e.g., "Tell me a joke", "Make me laugh")

- "Why did the scarecrow win an award? Because he was outstanding in his field."
- "Why don't scientists trust atoms? Because they make up everything!"
- "What do you call fake spaghetti? An impasta!"

### Study Help 📖
(e.g., "Can you help me study?", "Help me with my studies")

- "Of course! Tell me the topic or subject you'd like help with."
- "I'm here to support your learning. What do you need assistance with?"
- "I can provide notes on different programming languages like Python, Java, JavaScript, C Sharp, CPP, also HTML, CSS and more."

### Python Help 🐍
(e.g., "What is Python?", "Explain Python basics")

- "Python is a versatile programming language known for its simplicity and readability. What specific topic would you like to learn about?"
- "To write a function in Python, use the 'def' keyword. For example: `def my_function():`. Need a deeper example?"
- "Sure, I can help with Python! Do you need help with syntax, libraries, or debugging?"
- "Python basics include variables, data types, loops, and functions. Where should we start? You can install Python from the official website: https://www.python.org. Need help setting it up?"

### Java Help ☕
(e.g., "What is Java?", "Teach me about Java programming")

- "Java is a high-level, object-oriented programming language used for developing platform-independent applications. What specific area are you interested in?"
- "To write a class in Java, use the `class` keyword. For example: `class MyClass {}`. Want to know more about constructors?"
- "Yes, I can assist with Java! Do you need help with OOP concepts, libraries, or debugging?"
- "Java basics include classes, objects, methods, and loops. Let me know where to start! You can download and install the Java Development Kit (JDK) from https://www.oracle.com/java. Need guidance?"

### JavaScript Help 🌐
(e.g., "What is JavaScript?", "Explain JavaScript basics")

- "JavaScript is a versatile language for web development, enabling dynamic content on websites. What do you want to learn about?"
- "To write a function in JavaScript, use `function myFunction() {}`. Do you need an example with parameters?"
- "Sure, I can assist with JavaScript! Are you looking for help with DOM manipulation, ES6 features, or debugging?"
- "JavaScript basics include variables, functions, and event handling. Where would you like to start?"
- "Java and JavaScript are different. Java is object-oriented and used for apps, while JavaScript is mostly for interactive web content."

### C# Help #️⃣
(e.g., "What is C#?", "Teach me about C# programming")

- "C# is a modern, object-oriented programming language designed for the .NET platform. What aspect would you like to explore?"
- "To write a method in C#, use: `public void MyMethod() {}`. Need an example with parameters?"
- "Yes, I can assist with C#! Are you learning about .NET, LINQ, or Windows application development?"
- "C# basics include variables, classes, and inheritance. Let me know what to focus on!"
- "C is a procedural language, while C# is object-oriented and used for modern app development."

### C++ Help ➕
(e.g., "What is C++?", "Explain C++ basics")

- "C++ is an extension of C with object-oriented features. It's widely used for system programming and game development. What do you need help with?"
- "To write a function in C++, use: `void myFunction() {}`. Do you need an example with return values?"
- "Sure, I can assist with C++! Are you working on algorithms, classes, or memory management?"
- "C++ basics include classes, objects, and pointers. Let me know your focus area!"
- "C++ is object-oriented, while C is procedural. C++ allows you to use classes and features like inheritance."

### HTML Help 📄
(e.g., "What is HTML?", "How do I create a webpage?")

- "HTML (HyperText Markup Language) is the standard language for creating webpages. What do you want to learn about?"
- "To create a basic webpage, start with: `<html><head></head><body></body></html>`. Want help adding elements?"
- "Yes, I can assist with HTML! Are you learning about forms, tables, or semantic tags?"
- "HTML basics include tags like `<div>`, `<p>`, and `<a>`. Where do you want to start?"
- "HTML works by structuring content on the web using elements and attributes. Do you need a deeper dive?"

### CSS Help 🎨
(e.g., "What is CSS?", "How do I style a webpage?")

- "CSS (Cascading Style Sheets) is used to style and layout webpages. What specific feature do you want to learn about?"
- "To style a webpage, you can use inline, internal, or external CSS. Need an example of CSS syntax?"
- "Sure, I can help with CSS! Do you need assistance with selectors, flexbox, or grid?"
- "CSS basics include properties like `color`, `font-size`, and `margin`. What would you like to explore?"
- "HTML structures content, while CSS styles it. For example, HTML creates a heading, and CSS changes its color."

### SQL Help 🗄️
(e.g., "What is SQL?", "How do I query a database?")

- "SQL (Structured Query Language) is used to manage and query relational databases. What do you need help with?"
- "To query a database, use a SELECT statement. Example: `SELECT * FROM table_name;`. Want to know about joins?"
- "Yes, I can assist with SQL! Are you learning about queries, indexing, or database design?"
- "SQL basics include SELECT, INSERT, UPDATE, and DELETE statements. Let me know where to start!"
- "SQL works by interacting with databases using structured commands. Do you want an example?"

---

## Prerequisites 🛠️

Make sure you have the following installed:

- Python 3.8+ 🐍  
- PyTorch: `pip install torch` 🔥  
- spaCy: `pip install spacy` 📝  
  - Download the English model: `python -m spacy download en_core_web_sm`  
- NLTK: `pip install nltk` 📚  
- (Optional) Google API Client: `pip install google-api-python-client` 🌐  
- (Optional) CUDA-enabled GPU for faster inference 💻  

---

## Installation ⚙️

```bash
# Clone the Repository
git clone https://github.com/Jitenrai21/ChatterMate.git
cd ChatterMate

# Install Dependencies
pip install -r requirements.txt

# Download spaCy Model
python -m spacy download en_core_web_sm
````

Make sure `data.pth` (trained model) and `intents.json` are present in the project directory. 📂

---

## Usage 🚀

```bash
python chatbot.py
```

**Interact with ChatterMate:**

* Type your message and press Enter. 💬
* Example:

  * `"Hello"` → Triggers a greeting 👋
  * `"Tell me a joke"` → Shares a funny response 😂
  * `"Explain Python basics"` → Educational response 🐍
* Type `Q` to quit the chatbot. 🚪

---

## Project Structure 📁

```
ChatterMate/
│
├── chatbot.py           # Main script to run the chatbot 🤖
├── intents.json         # JSON file containing intent patterns and responses 📜
├── data.pth             # Pre-trained model data 💾
├── model.py             # Neural network model definition 🧠
├── nltk_utils.py        # NLP utilities for tokenization and bag-of-words 📝
├── README.md            # Project documentation 📖
└── requirements.txt     # List of dependencies 📋
```

---

## Training the Model 🏋️

To retrain the model or generate a new `data.pth` file:

1. Update `intents.json` with new intents, patterns, and responses. ✍️
2. Run a training script (to be created) that:

   * Tokenizes text using `nltk_utils.py` 📝
   * Creates a bag-of-words 🗣️
   * Trains `NeuralNet` using PyTorch 🔥
3. Save the model state and metadata to `data.pth`. 💾

---

## Extending ChatterMate 🌟

* **Add New Intents:** Edit `intents.json` ➕
* **Integrate APIs:** Add logic in `chatbot.py` for Google Search, weather, etc. 🌐
* **Improve NLP:** Use advanced models or techniques 🧠
* **Add Context Awareness:** Expand `user_context` management 📚

---

## Contributing 🤝

Contributions are welcome!

1. Fork the repository 🍴
2. Create a new branch: `git checkout -b feature-branch` 🌿
3. Make your changes and commit: `git commit -m "Add feature"` 💾
4. Push to the branch: `git push origin feature-branch` 🚀
5. Open a Pull Request 📬

---

## Acknowledgments 🙌

* Built with [PyTorch](https://pytorch.org) 🔥
* Uses [spaCy](https://spacy.io) for NLP 📝
* Inspired by open-source chatbot projects 🌍

---

For any issues or questions, please open an issue on the [GitHub repository](https://github.com/Jitenrai21/ChatterMate/issues). 🐛

```

