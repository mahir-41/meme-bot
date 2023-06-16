import error
import meme

class Request:
    def __init__(self, text):
        self.text = text

    def process(self):

        arr = self.text.split("-")

        cmd = arr[0]
        cmd2 = arr[1] if len(arr)>=2 else ""
        cmd3 = arr[2] if len(arr)>=3 else ""
        #to-do: figure out how to destructure arr into respective variables

        cmd = cmd.lower()
        if(cmd == "getinfo"):
            res = Response("text", "Command list ⚙️🤖\n- GetMeme: To generate memes type GetMeme-{template code}-{your text}. Type GetTemplateList to get all templates. Type GetHelp to get more info.\n- GetHelp: Learn how to generate memes.\n- GetTemplateList: Get a list of all meme templates.\n- GetAuthorInfo: Get information about the creator of this app.\n- Notes: 1)Memes currently support only one text. 2)Letter capitalization has been used in commands and templates for readability and is not enforced.(for example 'getmeme' instead of 'GetMeme' is ok 👍")

        elif(cmd == "gettemplatelist"):
            res = Response("text", "Find templates here: https://mahir41.pythonanywhere.com/templates 🎲")

        elif(cmd == "getmeme"):
            res = meme.MemeFactory().createMeme(cmd2, cmd3)
            if type(res) == type(error.Error("null")):
                res = Response("error", (meme.MemeFactory().createMeme(cmd2, cmd3)).print())
            else:
                res = Response("file", (meme.MemeFactory().createMeme(cmd2, cmd3))['data']['url'])

        elif(cmd == "gethelp"):
            res = Response("text", "Use the following format to send meme requests: GetMeme-{template code}-{your text}. Don't miss the dashes! Send GetTemplateList for template codes.")

        elif(cmd == "getauthorinfo"):
            res = Response("text", "👾 This app was created by Mahir Alam. For more info visit: https://mahir41.netlify.app/")

        elif(cmd == ""):
            res = Response("error", error.Error("No argument found!"))

        else:
            res = Response("text", "Command not recognized. Make sure the command is typed correctly, and there is no space within commands ('getMeme' not 'get meme'). Letter capitalization has been used for readability and is not enforced.(for example 'getmeme' instead of 'GetMeme' is ok 👍. If stuck, text GetInfo.👈")

        return res

class Response:
    def __init__(self, type, content):
        self.type = type
        self.content = content