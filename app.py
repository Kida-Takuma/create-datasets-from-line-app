import json
import re
import os
from datetime import datetime

def process_line(line):
    match = re.match(r"(\d{4}/\d{2}/\d{2}\(\w{1}\))?\s*(\d{2}:\d{2})?\s*([^\t]+)\t([^\n]+)", line)
    if match:
        time, sender, content = match.groups()[1], match.groups()[2], match.groups()[3]
        return time, sender.strip(), content.strip()
    return None

def create_finetune_dataset(file_path, primary_user="名前"):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    dataset = []
    current_dialogue = []
    previous_sender = None

    for line in lines:
        processed = process_line(line)
        if processed:
            time, sender, content = processed

            if sender == primary_user:
                if previous_sender and previous_sender != primary_user:
                    dataset.append({
                        "prompt": " ".join([message["content"] for message in current_dialogue]),
                        "completion": content
                    })
                    current_dialogue = []
                else:
                    current_dialogue.append({"role": "user", "content": content})
            else:
                if previous_sender and previous_sender == primary_user:
                    dataset.append({
                        "prompt": " ".join([message["content"] for message in current_dialogue]),
                        "completion": content
                    })
                    current_dialogue = []
                else:
                    current_dialogue.append({"role": "assistant", "content": content})

            previous_sender = sender

    output_dir = "datasets"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"finetune_dataset_{current_time}.json")

    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(dataset, out_file, ensure_ascii=False, indent=4)

    print(f"Dataset saved to {output_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        sys.exit(1)
    
    file_path = sys.argv[1]
    create_finetune_dataset(file_path)
