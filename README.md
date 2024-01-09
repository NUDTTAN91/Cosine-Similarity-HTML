# 比较两个`html`文件的相似度



​		使用余弦相似度（Cosine Similarity）算法来计算两个HTML文件的相似度。

​		首先使用正则表达式去除了HTML文件中的所有HTML标签，只保留了纯文本内容。然后，使用了`CountVectorizer`将文本转换为向量形式将文本中的每个单词视为一个特征，并计算每个单词在文本中出现的次数。

​		最后使用余弦相似度来计算两个向量的相似度。



> [!IMPORTANT]
>
> 余弦相似度是一种衡量两个向量方向相似度的度量，它的值范围在-1到1之间，1表示两个向量完全相同，0表示两个向量完全不相关，-1表示两个向量完全相反。



# HTML Similarity Checker

## Description

HTML Similarity Checker is a Python tool that calculates the similarity between two HTML documents. It strips the HTML tags and computes the textual content similarity using Cosine Similarity algorithm.

## Features

- Remove HTML tags to extract text content.
- Calculate text similarity using Cosine Similarity.
- Easy to use with a simple Python script.

## Installation

To use HTML Similarity Checker, you need to have Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone this repository to your local machine:

```bash
git clone https://github.com/NUDTTAN91/Cosine-Similarity-HTML.git
cd Cosine-Similarity-HTML
```

## Usage

To compare two HTML files, simply run the `similarity_checker.py` script with the paths to the files you want to compare:

```bash
python3 similarity_checker.py /path/to/Old.html /path/to/New.html
```

The script will output the similarity score between the two HTML files.



`similarity_checker.py`：

```python
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
```

