# PI_SF_2023

Ссылка на модель: https://huggingface.co/seara/rubert-base-cased-russian-sentiment?text=%D0%A2%D1%8B+%D0%BC%D0%BD%D0%B5+%D0%BD%D1%80%D0%B0%D0%B2%D0%B8%D1%88%D1%8C%D1%81%D1%8F.+%D0%AF+%D1%82%D0%B5%D0%B1%D1%8F+%D0%BB%D1%8E%D0%B1%D0%BB%D1%8E

Это приложение на основе модели Руберта, доработанная для классификации по тональности коротких текстов на русском языке. Задача - многоклассовая классификация со следующими метками:

1. neutral
2. positive
3. negative

Dataset
-----------------------------------

Эта  модель была обучена на основе объединения следующих наборов данных:

* Kaggle Russian News Dataset
* Linis Crowd 2015
* Linis Crowd 2016
* RuReviews
* RuSentiment
