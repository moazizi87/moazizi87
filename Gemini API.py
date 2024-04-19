'''
First you may need to install the 'google.generativeai' package using pypi:
$ pip install google-generativeai
'''

import google.generativeai as genai

genai.configure(api_key="AIzaSyBA49vGhPzI9cvSqdJk7eawBoDL1PGmCcM")

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "Let's play a food guess game! I have a food in my opinion and want you to guess it.It is a rice dish that is eaten with a stew containing a variety of cooked vegetables. This stew has a muddy green color and contains a lot of beans. Omani lemon and meat may be added to it.\nThis dish is a famous Iranian dish that is world famous.\nFirst guess the name of this dish and then say its recipe.",
  "input: Let's play a food guess game! I have a food in my opinion and want you to guess it.It is a rice dish that is eaten with a stew containing a variety of cooked vegetables. This stew has a muddy green color and contains a lot of beans. Omani lemon and meat may be added to it.\nThis dish is a famous Iranian dish that is world famous.\nFirst guess the name of this dish and then say its recipe.",
  "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text) 
