import json
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# Assuming the environment and paths are correctly set up
try:
    with open('C:/Soufiane/Tools/vm_shares/ocr_output.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found. Please check the file path.")
    data = []

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

translated_contents = []
source_lang = "zh_CN"
target_lang = "en_XX"

for item in data:
    # Check if 'content' key exists in the item
    if 'content' not in item:
        print(f"Item missing 'content' key, skipping: {item}")
        continue  # Skip this item and move to the next one

    try:
        content = item['content']
        tokenizer.src_lang = source_lang
        encoded = tokenizer(content, return_tensors="pt")
        generated_tokens = model.generate(
            **encoded,
            forced_bos_token_id=tokenizer.lang_code_to_id[target_lang]
        )
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        print (translation)
        translated_contents.append({
            'file': item['file'],
            'content': translation[0]
        })
    except Exception as e:
        print(f"Error translating content for file {item['file']}: {e}")

try:
    with open('C:/Soufiane/Tools/vm_shares/translated.json', 'w', encoding='utf-8') as f:
        json.dump(translated_contents, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"Error saving translated contents: {e}")
