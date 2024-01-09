from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def read_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_similarity(text1, text2):
    documents = [text1, text2]
    count_vectorizer = CountVectorizer().fit_transform(documents)
    vectors = count_vectorizer.toarray()
    return cosine_similarity(vectors)[0][1]

# 读取两个HTML文件
html1 = read_html('Old.html')
html2 = read_html('New.html')

# 清洗HTML标签，只保留文本内容
cleaned_html1 = clean_html(html1)
cleaned_html2 = clean_html(html2)

# 计算两个HTML文件的相似度
similarity = calculate_similarity(cleaned_html1, cleaned_html2)
print(f'The similarity between the two HTML files is: {similarity:.2f}')