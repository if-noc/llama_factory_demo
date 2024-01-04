import json
from typing import Any

class MyEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        return obj._dict_




with open("/mnt/huoyifu/LLaMA-Efficient-Tuning/data/oaast_sft4rlhf.txt", "a") as trg_file:

    obj_list = []
    with open("/mnt/huoyifu/LLaMA-Efficient-Tuning/data/oaast_sft.json") as file:
        lines = file.read()
        obj_list = json.loads(lines)
    data = [json.dumps(d, ensure_ascii=False)for d in obj_list]
    trg_file.write("\n".join(data))       
