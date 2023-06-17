import requests
import error


class MemeFactory:
    def __init__(self):
        pass

    def createMeme(self, template, text):
        if template == "":
            return error.Error(
                "No template was provided! Type getHelp for instructions.👈"
            )

        if text == "":
            return error.Error("No text was provided! Type getHelp for instructions.👈")

        template = template.lower()

        if template == "spongebob":
            return self.getMeme("102156234", text)
        elif template == "bernie":
            return self.getMeme("222403160", text)
        elif template == "lookatme":
            return self.getMeme("29617627", text)
        elif template == "wheremonkey":
            return self.getMeme("316466202", text)
        else:
            return error.Error(
                "Template not found! Check for gaps or misspellings in your template code. Type getHelp for more instructions.👈"
            )

    def getMeme(self, template, text):
        url = "https://api.imgflip.com/caption_image"

        payload = {
            "template_id": template,
            "username": "MahirAlam1",
            "password": "qiNbv56Gt3@wg6G",
            "text1": text,
        }

        response = requests.post(url, data=payload)

        if response.status_code == 200:  # Successful request
            return response.json()
        else:
            return "POST request failed with status code:", response.status_code
