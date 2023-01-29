import openai

def narrate(plant_detected):
    print("[DEBUG]", plant_detected)
    prompt = f"Tell me about {plant_detected['common_names'][0]}, is it edible?"

    result = openai.Completion.create(
        # (for use during testing: curie is faster/cheaper than davinci but not as high quality)
        engine=["text-curie-001", "text-davinci-002"][1],
        prompt=prompt,
        max_tokens=200,
        temperature=1,  # Value 0 to 1 -- Higher values means the model will take more risks
        presence_penalty=0,  
        frequency_penalty=2,  
    )

    # print(result["choices"][0]["text"])
    return result["choices"][0]["text"]
