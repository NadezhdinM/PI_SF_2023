from transformers import pipeline

model = pipeline(model="seara/rubert-base-cased-russian-sentiment")

model("Привет, ты мне нравишься!")
