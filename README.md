# meme-bot
**Intro**
With this meme-bot you can create memes from the convenience of your favourite messaging apps with simple text-based commands! Currently, it's a minimum viable product, so there won't be any advanced features. This is a python, flask application, hosted on Pythonanywhere. 

**Installation** 📀
To take a quick look at the application, visit the test client I made at this [link](http://mahir41.pythonanywhere.com/test-client). You can also install the necessary dependencies and run the flask application locally, maybe even hook it up with messenger webhooks service with your own tokens.

**Command list** ⚙️🤖<br>- GetMeme: To generate memes type GetMeme-{template code}-{your text}.<br>- GetInfo: Get a list of all commands. <br>- GetHelp: Learn how to generate memes.<br>- GetTemplateList: Get a list of all meme templates.<br>- GetAuthorInfo: Get information about the creator of this app.

**Endpoints** <br>- "/": Receive messages from messenger.<br>- "/process": Returns json object with keys "type" and "content" after processing request. The type value tells us the type of content produced by the method; the possible types are "file", "text" and "error". <br>- "/test-client": Testing client site.<br>- "/templates": Templates site.

**Development**: 
Classes and methods:
`1) Request class`
`- Constructor method: Request(), Constructor Args: command(String) - The command to be processed by the process method of the Request class.`
`- process() method: NoArgs; Description: Returns a Response object after processing the command specified to the instance of Request. Command is split into three parts, using "-" as the delimiter. All commands are one word(for example: "getInfo") except for getMeme which uses the format "GetMeme-{template code}-{your text}". The capitalization for the command/template does not matter as .lower() is applied on the command before processing. (For example GETINFO would work). Camel case is used just for readability.`

`2) Response class`
`- Constructor method: Response(), Constructor Args: type(String) - The type of content returned; content(String) - The content returned after processing the input. Works in conjunction with the Request class`

`3) MemeFactory class`
`- Constructor method: MemeFactory()`
`- createMeme() method: Args: template(String) - The template string for the template to be used in the meme as provided in the url from getTemplateList command; text(String) - The text to be used in the meme; Description: Makes a fetch call to the imgflip api with a template code. The template code is determined based on the template 'template' argument provided by the caller. For example 'spongebob' is resolved to code'102156234'. If the fetch call succeeds, the response is returned to the invoker of the method as json object which contains a url to the meme as an attribute.`

`4) Error class`
`- Constructor method: Error(), Constructor Args: text(String) - The error warning to be displayed to the user.`
`- print() method: Prints the error message.`

**Design Patterns** 🧩
In this project, I've tried to take advantage of Object Oriented Programming patterns and concepts on a very basic level to gain more practical experience with design patterns by myself, outside of a CS class. 

The Request class here makes use of the command design pattern. It encapsulates the request made by the client. It determines what to do with the command text and if needed, carries it over to the receiver class for further processing. Once the processing is complete, it puts the output in a Response object and returns it to the client for displaying to the user or whatever.

The aforementioned 'receiver' class in my project is the MemeFactory class which (given away by the name) follows the factory pattern. This class is going to act as the generator of the output files. I used this pattern considering the different types of memes, like memes with mutiple text boxes, that I might want to create in the future. Seems like the perfect use case for some subtype polymorphism.
The Error and Response classes were spontaneous ideas that I came up with. 

In conclusion, the use of these patterns did make the development process very streamlined. It was easier to validate inputs, reuse code and test the program compared to other projects I have worked on where OOP ideas were not used very much. Furthermore, I have also noticed this approach helps to intuitively identify what areas need to be worked on next. 

**Front-end testing client**:
Developed with HTML, CSS and JavaScript. 
Link: http://mahir41.pythonanywhere.com/test-client

**Deployment and Documentation**
This app is deployed on pythonanywhere.com for public access and version controlled with git.