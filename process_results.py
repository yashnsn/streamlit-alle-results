from comfy_api_simplified import ComfyApiWrapper, ComfyWorkflowWrapper
import base64
import websockets
import os
from PIL import Image
from io import BytesIO


api = ComfyApiWrapper("https://pgy5qbevi6xwhz-3456.proxy.runpod.net")

wf = ComfyWorkflowWrapper("postprocessing.json")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

root_path = "final_testset_garments_results_V13_lora"

for base_image in os.listdir(root_path):
    if base_image.startswith('.'):
        continue
    for category in os.listdir(f'{root_path}/{base_image}'):
        if category.startswith('.'):
            continue
        for ind_image in os.listdir(f'{root_path}/{base_image}/{category}'):
            if ind_image.startswith('.') or ind_image.endswith('.json') or os.path.exists(f'{root_path}/{base_image}/{category}/processed_{ind_image}') or 'processed' in ind_image:
                continue
            wf.set_node_param('Load Image (Base64)', "base64_data", encode_image(f'{root_path}/{base_image}/{category}/{ind_image}'))
            print(f'Processing {root_path}/{base_image}/{category}/{ind_image}')
            results = api.queue_and_wait_images(wf, 'Save Image')
            for _, image_data in results.items():
                image = Image.open(BytesIO(image_data))
                image.save(f'{root_path}/{base_image}/{category}/processed_{ind_image}')