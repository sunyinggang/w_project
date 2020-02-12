import os

import docx
import jieba
from gensim import corpora, models, similarities


def TfIdf(fileUrl):
    UPLOAD_FOLDER = 'static\\upload\\'
    baseUrl = os.path.abspath(os.path.dirname(__file__)).replace("student","")
    file_dir = os.path.join(baseUrl, UPLOAD_FOLDER)
    file_dir = file_dir + fileUrl
    # 读取word文档
    document = docx.Document(file_dir)
    # 读取实验中的表格内容
    tables = document.tables
    #读取第一个表格（默认就一个表格）
    tb = tables[0]
    #读取表格行数
    tb_rows = tb.rows
    result = ""
    for j in range(3, len(tb_rows)):
        result += tb.cell(j, 1).text
    keywords = "我喜欢上海的小吃；在北京；男人"
    all_doc = []
    all_doc.append(result)
    all_doc.append("")


    all_doc_list = []
    for doc in all_doc:
        doc_list = [word for word in jieba.cut(doc)]
        all_doc_list.append(doc_list)

    #1、将【文本集】生产【分词列表】
    doc_test_list = [word for word in jieba.cut(keywords)]
    # 2、基于文件集建立【词典】，并提取词典特征数
    dictionary = corpora.Dictionary(all_doc_list)
    # 3、基于词典，将【分词列表集】转换为【稀疏向量集】，也就是【语料库】
    corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
    # 4、使用“TF-TDF模型”处理【语料库】
    tfidf = models.TfidfModel(corpus)
    # 5、同理，用词典把搜索词也转换为稀疏向量
    doc_test_vec = dictionary.doc2bow(doc_test_list)
    # 6、对稀疏向量建立索引
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    # 7、相似的计算
    sim = index[tfidf[doc_test_vec]]
    t = sorted(enumerate(sim), key=lambda item: -item[1])
    score = int(t[0][1] * 100)
    return score

if __name__ == '__main__':
    score = TfIdf("1580212715.docx")
    print(score)