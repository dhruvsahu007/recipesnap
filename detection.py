from transformers import DetrImageProcessor, DetrForObjectDetection, VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch

# Load models once globally
caption_model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
caption_processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
caption_tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

detr_processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
detr_model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

def detect_with_caption(image: Image.Image):
    # Caption generation (fixed: no beam search)
    pixel_values = caption_processor(images=image, return_tensors="pt").pixel_values
    output_ids = caption_model.generate(
        pixel_values,
        max_length=16,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=1.0,
        num_return_sequences=1
    )
    caption = caption_tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Object detection
    inputs = detr_processor(images=image, return_tensors="pt")
    outputs = detr_model(**inputs)
    target_sizes = torch.tensor([image.size[::-1]])
    results = detr_processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    labels = [detr_model.config.id2label[label.item()] for label in results["labels"]]
    return list(set(labels)), caption
