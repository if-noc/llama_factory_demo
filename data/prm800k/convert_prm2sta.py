import json
from typing import Any

class MyEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        return obj._dict_




with open("/mnt/huoyifu/LLaMA-Efficient-Tuning/data/prm800k/data/phase1_train_for_llama.json", "a") as trg_file:

    obj_list = []
    with open("/mnt/huoyifu/LLaMA-Efficient-Tuning/data/prm800k/data/phase1_train.jsonl") as file:
        lines = file.readlines()

        for line in lines:
            data = {"instruction":"","output":""}
            obj = json.loads(line)
            data["instruction"] = obj['question']['problem']
            for i in range(len(obj['label']['steps'])):
                if(obj['label']['steps'][i]['completions']!=None):
                    for j in range(len(obj['label']['steps'][i]['completions'])):
                        data["output"] = data["output"] + obj['label']['steps'][i]['completions'][j]['text'] + '#Rating:{'+str(obj['label']['steps'][i]['completions'][j]['rating'])+"}#"
                    if(obj['label']['steps'][i]['human_completion']!=None):
                        data["output"] = data["output"] + obj['label']['steps'][i]['human_completion']['text']+'#Rating:{1}#'
            obj_list.append(data)    
    json.dump(obj_list, trg_file, indent=2)        

    # while line != '':
    #     obj = json.loads(line)
    #     print(obj)

