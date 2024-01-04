import json
from typing import Any

class MyEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        return obj._dict_




with open("/mnt/huoyifu/LLaMA-Efficient-Tuning/data/prm800k/data/phase1_train_best.json", "a") as trg_file:

    obj_list = []
    with open("/mnt/huoyifu/LLaMA-Efficient-Tuning/data/prm800k/data/phase1_train.jsonl") as file:
        lines = file.readlines()

        for line in lines:
            data = {"instruction":"","output":""}
            obj = json.loads(line)
            data["instruction"] = obj['question']['problem']

            for i in range(len(obj['label']['steps'])):
                if(obj['label']['steps'][i]['completions']!=None):
                    if (obj['label']['steps'][i]['chosen_completion']!=None):
                        chosen_completion = obj['label']['steps'][i]['chosen_completion']
                        data['output'] = data['output'] + obj['label']['steps'][i]['completions'][chosen_completion]['text'] + '#Rating:{'+str(obj['label']['steps'][i]['completions'][chosen_completion]['rating'])+"}#"
                    elif(obj['label']['steps'][i]['human_completion']!=None):
                        data["output"] = data["output"] + obj['label']['steps'][i]['human_completion']['text']+'#Rating:{1}#'
                        
            obj_list.append(data)    
    json.dump(obj_list, trg_file, indent=2)        

    # while line != '':
    #     obj = json.loads(line)
    #     print(obj)

