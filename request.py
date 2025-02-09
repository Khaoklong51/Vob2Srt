import requests
import base64
import argument
import os

def request_json(image_content):
    if argument.lang:
        request_payload = {
        "requests": [
            {
                "image": {
                    "content": image_content
                },
                "features": [
                    {
                        "type": "TEXT_DETECTION"
                    }
                ],
                "imageContext": {  
                    "languageHints": [argument.lang]
                }
            }
        ]
    }

    else:
        request_payload = {
            "requests": [
                {
                    "image": {
                        "content": image_content
                    },
                    "features": [
                    {
                        "type": "TEXT_DETECTION"
                    }
                    ],
                }
            ]
        }

    return request_payload

def request_text(img_path:str):
    with open(img_path, "rb") as image_file:
        image_content = base64.b64encode(image_file.read()).decode("utf-8") # google cloud vision ai api required base64 encode
    url = f"https://vision.googleapis.com/v1/images:annotate?key={argument.key}"

    headers = {
        "Content-Type": "application/json"
    }

    request_payload = request_json(image_content)

    # Make the request
    response = requests.post(url, json=request_payload, headers=headers)
    result = response.json()

    # Check for errors
    if "error" in result:
        raise Exception(f"Error: {result['error']['message']}")
    
    # Process the response
    texts = result.get("responses", [])[0].get("textAnnotations", [])
    if texts:
        ftext = texts[0]["description"]
        return ftext
    else:
        msg = f"No text detected for {os.path.basename(img_path)}"
        print(msg)
        return msg

